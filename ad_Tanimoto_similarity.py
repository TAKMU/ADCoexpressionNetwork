
import pandas as pd
import numpy as np
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
import altair as alt

df = pd.read_csv('./data/LINCS_ad_gene_nw_modified_with_symbols.csv')
ad = pd.DataFrame(df['ad'].unique(), columns=['ad'])


def smiles(ad):
    drugs = pcp.get_compounds(ad, 'name')
    smiles = drugs[0].canonical_smiles
    mol = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(mol, isomericSmiles=True)

ad['canonical_SMILES_stereo'] = ad['ad'].apply(smiles)
fingerprints = ad['canonical_SMILES_stereo'].apply(lambda x: AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(x), 2))

## creates a Tanimoto similarity matrix
tanimoto_similarities = np.array([DataStructs.BulkTanimotoSimilarity(fp, fingerprints) for fp in fingerprints])
tanimoto_df = pd.DataFrame(tanimoto_similarities, index=ad['ad'], columns=ad['ad'])
tanimoto_df.index.name = None
tanimoto_df.to_csv('./data/tanimoto_matrix.csv')

tanimoto_long_df = tanimoto_df.reset_index().melt(id_vars='index')
tanimoto_long_df.columns = ['node_1', 'node_2', 'Tan']
tanimoto_long_df['Tan'] = tanimoto_long_df['Tan'].round(3)

base = alt.Chart(tanimoto_long_df).encode(
    alt.X('node_1:O', title=None),
    alt.Y('node_2:O', title=None)
)

heatmap = base.mark_rect().encode(
    alt.Color('Tan:Q', scale=alt.Scale(scheme='viridis'), legend=alt.Legend(title=None)),
    tooltip=['node_1:N', 'node_2:N', 'Tan:Q']
).properties(
    title='Tanimoto similarity of antidepressants based on canonical SMILES with stereochemistry',
    width=1000,
    height=900
)

text = base.mark_text(baseline='middle').encode(
    text='Tan:Q',
    color=alt.condition(
        alt.datum.Tan > 0.5,
        alt.value('black'),
        alt.value('white')
    )
)

tanimoto_heatmap = heatmap + text
tanimoto_heatmap.save("./img/tanimoto_similarity.png")