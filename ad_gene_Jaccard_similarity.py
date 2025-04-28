import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv('./data/LINCS_ad_gene_nw_modified_with_symbols.csv')


top_df = df[df['value'] == 1]
bottom_df = df[df['value'] == -1]

adjacency_matrix = pd.crosstab(top_df['ad'], top_df['gene'])
intersection = adjacency_matrix.dot(adjacency_matrix.T)
union = adjacency_matrix.sum(axis=1).values[:, None] + adjacency_matrix.sum(axis=1).values - intersection
jaccard_matrix_values = intersection / union
np.fill_diagonal(jaccard_matrix_values.values, 1)

jaccard_top_matrix = pd.DataFrame(jaccard_matrix_values, index=adjacency_matrix.index,  columns=adjacency_matrix.index.copy())
jaccard_top_matrix.index.name = 'node_2'
jaccard_top_matrix.columns.name = 'node_1'

jaccard_top_matrix.to_csv('./data/jaccard_top_matrix.csv')

jaccard_long_df = jaccard_top_matrix.reset_index().melt(id_vars='node_2')
jaccard_long_df.columns = ['node_1', 'node_2', 'Jaccard']
jaccard_long_df['Jaccard'] = jaccard_long_df['Jaccard'].round(3)
base = alt.Chart(jaccard_long_df).encode(
    alt.X('node_1:O', title=None),
    alt.Y('node_2:O', title=None)
)

heatmap = base.mark_rect().encode(
    alt.Color('Jaccard:Q', scale=alt.Scale(scheme='viridis'), legend=alt.Legend(title=None)),
    tooltip=['node_1:N', 'node_2:N', 'Jaccard:Q']
).properties(
    title='Jaccard similarity of antidepressants based on targeted genes for top network',
    width=1000,
    height=900
)

text = base.mark_text(baseline='middle').encode(
    text='Jaccard:Q',
    color=alt.condition(
        alt.datum.Jaccard > 0.5,
        alt.value('black'),
        alt.value('white')
    )
)

top_heatmap = heatmap + text
top_heatmap.save("./img/top_gene_heatmap.png")


################################################################################
# Jaccard similarity calculation for bottom network
################################################################################
adjacency_matrix = pd.crosstab(bottom_df['ad'], bottom_df['gene'])
intersection = adjacency_matrix.dot(adjacency_matrix.T)
union = adjacency_matrix.sum(axis=1).values[:, None] + adjacency_matrix.sum(axis=1).values - intersection
jaccard_matrix_values = intersection / union
np.fill_diagonal(jaccard_matrix_values.values, 1)
jaccard_bottom_matrix = pd.DataFrame(jaccard_matrix_values, index=adjacency_matrix.index,  columns=adjacency_matrix.index.copy())
jaccard_bottom_matrix.index.name = 'node_2'
jaccard_bottom_matrix.columns.name = 'node_1'
jaccard_bottom_matrix.to_csv('./data/jaccard_bottom_matrix.csv')

jaccard_long_df = jaccard_bottom_matrix.reset_index().melt(id_vars='node_2')
jaccard_long_df.columns = ['node_1', 'node_2', 'Jaccard']

jaccard_long_df['Jaccard'] = jaccard_long_df['Jaccard'].round(3)

base = alt.Chart(jaccard_long_df).encode(
    alt.X('node_1:O', title=None),
    alt.Y('node_2:O', title=None)
)

heatmap = base.mark_rect().encode(
    alt.Color('Jaccard:Q', scale=alt.Scale(scheme='viridis'), legend=alt.Legend(title=None)),
    tooltip=['node_1:N', 'node_2:N', 'Jaccard:Q']
).properties(
    title='Jaccard similarity of antidepressants based on targeted genes for bottom network',
    width=1000,
    height=900
)

text = base.mark_text(baseline='middle').encode(
    text='Jaccard:Q',
    color=alt.condition(
        alt.datum.Jaccard > 0.5,
        alt.value('black'),
        alt.value('white')
    )
)

bottom_heatmap = heatmap + text
bottom_heatmap.save("./img/bottom_heatmap.png")