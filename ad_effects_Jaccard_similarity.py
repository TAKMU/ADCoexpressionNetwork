import pandas as pd
import numpy as np
import altair as alt

global_df = pd.read_csv('./data/global_ad_ars_network.csv')
local_df = pd.read_csv('./data/local_ad_ars_network.csv')

adjacency_matrix_global = pd.crosstab(global_df['ad'], global_df['ars'])
intersection_global = adjacency_matrix_global.dot(adjacency_matrix_global.T)
union_global = adjacency_matrix_global.sum(axis=1).values[:, None] + adjacency_matrix_global.sum(axis=1).values - intersection_global
jaccard_matrix_values_global = intersection_global / union_global
np.fill_diagonal(jaccard_matrix_values_global.values, 1)

jaccard_global_matrix = pd.DataFrame(jaccard_matrix_values_global, index=adjacency_matrix_global.index,  columns=adjacency_matrix_global.index.copy())
jaccard_global_matrix.index.name = 'node_2'
jaccard_global_matrix.columns.name = 'node_1'

jaccard_global_matrix.to_csv('./data/jaccard_global_matrix.csv')

jaccard_long_df_global = jaccard_global_matrix.reset_index().melt(id_vars='node_2')
jaccard_long_df_global.columns = ['node_1', 'node_2', 'Jaccard']

jaccard_long_df_global['Jaccard'] = jaccard_long_df_global['Jaccard'].round(3)

base_global = alt.Chart(jaccard_long_df_global).encode(
    alt.X('node_1:O', title=None),
    alt.Y('node_2:O', title=None)
)

heatmap_global = base_global.mark_rect().encode(
    alt.Color('Jaccard:Q', scale=alt.Scale(scheme='viridis'), legend=alt.Legend(title=None)),
    tooltip=['node_1:N', 'node_2:N', 'Jaccard:Q']
).properties(
    title='Jaccard similarity of antidepressants based on adverse effects for global network',
    width=1000,
    height=900
)

text_global = base_global.mark_text(baseline='middle').encode(
    text='Jaccard:Q',
    color=alt.condition(
        alt.datum.Jaccard > 0.5,
        alt.value('black'),
        alt.value('white')
    )
)

heatmap_global_text = heatmap_global + text_global
heatmap_global_text.save("./img/global_heatmap.png")

adjacency_matrix_local = pd.crosstab(local_df['ad'], local_df['ars'])


################################################################################
# Jaccard similarity calculation for local network
################################################################################

intersection_local = adjacency_matrix_local.dot(adjacency_matrix_local.T)
union_local = adjacency_matrix_local.sum(axis=1).values[:, None] + adjacency_matrix_local.sum(axis=1).values - intersection_local
jaccard_matrix_values_local = intersection_local / union_local
np.fill_diagonal(jaccard_matrix_values_local.values, 1)
jaccard_local_matrix = pd.DataFrame(jaccard_matrix_values_local, index=adjacency_matrix_local.index,  columns=adjacency_matrix_local.index.copy())
jaccard_local_matrix.index.name = 'node_2'
jaccard_local_matrix.columns.name = 'node_1'
jaccard_local_matrix.to_csv('./data/jaccard_local_matrix.csv')

jaccard_long_df_local = jaccard_local_matrix.reset_index().melt(id_vars='node_2')
jaccard_long_df_local.columns = ['node_1', 'node_2', 'Jaccard']


jaccard_long_df_local['Jaccard'] = jaccard_long_df_local['Jaccard'].round(3)

base_local = alt.Chart(jaccard_long_df_local).encode(
    alt.X('node_1:O', title=None),
    alt.Y('node_2:O', title=None)
)

heatmap_local = base_local.mark_rect().encode(
    alt.Color('Jaccard:Q', scale=alt.Scale(scheme='viridis'), legend=alt.Legend(title=None)),
    tooltip=['node_1:N', 'node_2:N', 'Jaccard:Q']
).properties(
    title='Jaccard similarity of antidepressants based on adverse effects for local network',
    width=1000,
    height=900
)

text_local = base_local.mark_text(baseline='middle').encode(
    text='Jaccard:Q',
    color=alt.condition(
        alt.datum.Jaccard > 0.5,
        alt.value('black'),
        alt.value('white')
    )
)

heatmap_local_text = heatmap_local + text_local
heatmap_local_text.save("./img/local_heatmap.png")