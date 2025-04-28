# ----------------------------------------------------------------------------
# Script Title: Unique Neighbors
# Author: Silvana Yalú Cristo Martínez
# Creation Date: 2024-09-26
# Last Update: 2024-09-26
# Version: 1.0
# Description: 
# This script filters unique neighbor genes affected by a specific antidepressant (AD)
#
# ----------------------------------------------------------------------------
# Changes:
# - [2024-09-26] Script creation. (Silvana Yalú Cristo Martínez)
# ----------------------------------------------------------------------------

library(tidyverse)
library(dplyr)

ruta <- "./data/LINCS_ad_gene_nw_modified_with_symbols.csv"
df <- read_csv(ruta)

genes_unicos <- df %>%
  group_by(gene) %>%
  summarise(num_ADs = n_distinct(ad)) %>%
  filter(num_ADs == 1) %>%  
  dplyr::select(gene)


df_genes_unicos <- df %>%
  filter(gene %in% genes_unicos$gene)


df_top_unicos <- df_genes_unicos %>% filter(value == 1)
df_bottom_unicos <- df_genes_unicos %>% filter(value == -1)


write_csv(df_top_unicos, "./data/genes_top_unicos.csv")
write_csv(df_bottom_unicos, "./data/genes_bottom_unicos.csv")


head(df_top_unicos)
head(df_bottom_unicos)

