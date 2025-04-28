import pandas as pd
import numpy as np
prr_filtered = pd.read_csv('./data/prr_filtered.csv')
ad = pd.read_csv('antidepressants.tsv', sep='\t')
filtered_prr = prr_filtered[prr_filtered['prod_ai'].isin(ad['pert_iname'])]

filtered_prr['pt'] = filtered_prr['pt'].str.lower()
################################################################################
# data ranking and transformations for global prr
################################################################################
result_df = pd.DataFrame(columns=['ars', 'ad', 'value'])
for antidepressant in filtered_prr['prod_ai'].unique():
    ad_data = filtered_prr[filtered_prr['prod_ai'] == antidepressant]
    percentile_90 = np.percentile(ad_data['prr_global'], 90)
    top_decile_data = ad_data[ad_data['prr_global'] >= percentile_90]
    result_df = pd.concat([result_df, top_decile_data[['pt', 'prod_ai', 'prr_global']]], ignore_index=True)
result_df = result_df[['pt', 'prod_ai', 'prr_global']]
result_df.columns = ['ars', 'ad', 'value']

result_df.to_csv('./data/global_ad_ars_network.csv', index=False)

################################################################################
# data ranking and transformations for local prr
################################################################################

result_df = pd.DataFrame(columns=['ars', 'ad', 'value'])
for antidepressant in filtered_prr['prod_ai'].unique():
    ad_data = filtered_prr[filtered_prr['prod_ai'] == antidepressant]
    percentile_90 = np.percentile(ad_data['prr_local'], 90)
    top_decile_data = ad_data[ad_data['prr_local'] >= percentile_90]
    result_df = pd.concat([result_df, top_decile_data[['pt', 'prod_ai', 'prr_local']]], ignore_index=True)

result_df = result_df[['pt', 'prod_ai', 'prr_local']]
result_df.columns = ['ars', 'ad', 'value']
result_df.to_csv('./data/local_ad_ars_network.csv', index=False)


