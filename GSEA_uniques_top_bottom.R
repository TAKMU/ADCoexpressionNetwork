# ----------------------------------------------------------------------------
# Script Title: GSEA Enrichment Analysis for Unique Neighborhoods
# Author: Silvana Yalú Cristo Martínez
# Creation Date: 2024-09-26
# Last Update: 2025-02-21
# Version: 1.1
# Description: This script performs a GO (Gene Ontology) enrichment analysis
# for genes in unique neighborhoods, divided into top and bottom, using the 
# clusterProfiler library. Two independent GSEA analyses are generated: 
# one for positively regulated genes (top) and one for negatively regulated 
# genes (bottom).
#
# ----------------------------------------------------------------------------
# Changes:
# - [2024-09-26] Script creation. (Silvana Yalú Cristo Martínez)
# - [2025-02-21] Improved script efficiency by optimizing data processing and GSEA execution. (Allan Ken Miyazono Ushijima)
# ----------------------------------------------------------------------------
library(clusterProfiler)
library(org.Hs.eg.db)
library(dplyr)
library(ggplot2)

# Different types of networks used for clustering
position <- c("top", "bottom")

# Define file paths dynamically
file_paths <- list(
  "top" = "./data/genes_top_unicos.csv",
  "bottom" = "./data/genes_bottom_unicos.csv"
)


# Loop to apply the same process for either top or bottom
for (name in position) {
  
  # =========== 1. Load Top or Bottom ===========
  df_nw <- read.csv(file_paths[[name]], header = TRUE, stringsAsFactors = FALSE)
  genes_list <- df_nw$gene
  
  # =========== 2. GSEA ===========
  enrich_results <- enrichGO(
    gene = genes_list,      
    OrgDb = org.Hs.eg.db,            
    keyType = "SYMBOL",         
    ont = "BP",                 
    pvalueCutoff = 0.05,        
    qvalueCutoff = 0.05         
  )
  
  # =========== 3. Save data ===========
  df_result <- as.data.frame(enrich_results)
  
  write.csv(df_result, file = paste0("./data/enr_", name, "_genes.csv"), row.names = FALSE)
  ggplot2::ggsave(paste0("./img/cnetplot_", name, ".png"), cnetplot(enrich_results, layout= 'circle', showCategory=5, color_edge = "category"), width = 10, height = 10)
 
}  



