import pandas as pd
lincs_df = pd.read_csv('./data/LINCS_ad_gene_nw_modified.csv')
gene_info_df = pd.read_csv('/datos/LINCS/GSE92742_Broad_LINCS_gene_info.txt', sep='\t')

gene_dict = dict(zip(gene_info_df['pr_gene_id'].astype(str), gene_info_df['pr_gene_symbol']))
lincs_df['rid'] = lincs_df['rid'].astype(str)
lincs_df['rid'] = lincs_df['rid'].map(gene_dict)


lincs_df.rename(columns={'rid': 'gene', 'cid': 'ad', 'value': 'value'}, inplace=True)

lincs_df.to_csv('./data/LINCS_ad_gene_nw_modified_with_symbols.csv', index=False)
