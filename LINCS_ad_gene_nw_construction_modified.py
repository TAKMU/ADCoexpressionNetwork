import pandas as pd
import numpy as np
from cmapPy.pandasGEXpress import parse

gctx_file_path = '/datos/LINCS/GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx'
df = parse.parse(gctx_file_path)
inst = pd.read_csv("/datos/LINCS/GSE92742_Broad_LINCS_inst_info.txt", sep="\t", low_memory=False)
ad = pd.read_csv('antidepressants.tsv', sep='\t')


inst_ad = inst[inst['pert_iname'].isin(ad['pert_iname'])]
inst_ad_npc = inst_ad[inst["cell_id"]=="NPC"] 
max_values = inst_ad_npc.groupby('pert_iname').agg({'pert_dose': 'max', 'pert_time': 'max'}).reset_index()
filtered_inst_ad_npc = inst_ad_npc.merge(max_values, on=['pert_iname', 'pert_dose', 'pert_time'])
columns_to_keep = filtered_inst_ad_npc["inst_id"].tolist()
lincs_df = df.data_df[columns_to_keep]

column_to_pert_iname = dict(zip(filtered_inst_ad_npc['inst_id'], filtered_inst_ad_npc['pert_iname']))
subset_data_df = df.data_df[filtered_inst_ad_npc['inst_id'].tolist()]
subset_data_df = subset_data_df.rename(columns=column_to_pert_iname)
median_df = subset_data_df.groupby(level=0, axis=1).median()
top_bottom = pd.DataFrame(0, index=median_df.index, columns=median_df.columns)

for col in median_df.columns:
    deciles = pd.qcut(median_df[col], 100, labels=False, duplicates='drop')
    top_bottom.loc[deciles == 99, col] = 1
    top_bottom.loc[deciles == 0, col] = -1

top_bottom_reset = top_bottom.reset_index().rename(columns={"index": "rid"})
long_format_df = top_bottom_reset.melt(id_vars='rid', var_name='cid', value_name='value')
long_format_df[long_format_df['value'] != 0].to_csv(path_or_buf = './data/LINCS_ad_gene_nw_modified_1.csv', index=False)
