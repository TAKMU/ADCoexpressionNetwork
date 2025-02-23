# ----------------------------------------------------------------------------
# Script Title: Enrichment Analysis (GSEA) for Clusters
# Author: Silvana Yalú Cristo Martínez
# Creation Date: 2024-10-07
# Last Update: 2025-02-21
# Version: 1.1
# Description: 
# This script performs a functional enrichment analysis (GSEA) of genes 
# associated with antidepressants classified into clusters based on several networks, 
# including top and bottom Jaccard, local and global adverse effects, and Tanimoto similarity.
# The clusters were generated from a hierarchical dendrogram based on these networks. 
# The enrichment is performed on biological processes (GO:BP).
#
# ----------------------------------------------------------------------------
# Changes:
# - [2024-10-07] Script creation. (Silvana Yalú Cristo Martínez)
# - [2025-02-21] Merged four scripts into one for improved organization and efficiency. (Allan Ken Miyazono Ushijima)
# ----------------------------------------------------------------------------

library(clusterProfiler)
library(org.Hs.eg.db)
library(dplyr)
library(ggplot2)



# Load the dataframe (network) listing links between antidepressants (AD) and genes
df_gene <- read.csv("./data/LINCS_ad_gene_nw_modified_with_symbols.csv", 
                    header = TRUE, 
                    stringsAsFactors = FALSE) 

# Different types of networks used for clustering
type_cluster <- c("tanimoto", "top", "bottom", "global", "local")

# Define file paths dynamically
file_paths <- list(
  "tanimoto" = "./data/structural_ad_clustering.csv",
  "top" = "./data/functional_top_ad_clustering.csv",
  "bottom" = "./data/functional_bottom_ad_clustering.csv",
  "global" = "./data/functional_global_ad_clustering.csv",
  "local" = "./data/functional_local_ad_clustering.csv"
)

# Loop to apply the same process for each clustering method
for (name in type_cluster) {
  output_dir <- paste0("./data/", name, "/")
  if (!dir.exists(output_dir)) dir.create(output_dir, recursive = TRUE)
  img_dir <- paste0("./img/", name, "/")
  if (!dir.exists(img_dir)) dir.create(img_dir, recursive = TRUE)
  
  # =========== 1. Load Cluster Assignments ===========
  df_cluster <- read.csv(file_paths[[name]], header = TRUE, stringsAsFactors = FALSE)
  
  # =========== 2. Merge Gene Data with Clusters ===========
  result <- inner_join(df_gene, df_cluster, by = c("ad" = "AD"))
  
  # =========== 3. Process Each Cluster ===========
  max_cluster <- max(df_cluster$Cluster, na.rm = TRUE)  # Handle NA values
  
  if (!is.na(max_cluster) && max_cluster > 0) {
    

    genes_cluster_list <- list()
    enrich_cluster_list <- list()
    
    for (i in 1:max_cluster) {
      
      # =========== 3.1. Filter Genes for Each Cluster ===========
      genes_cluster_list[[paste0(name, "_c", i)]] <- result |>  
        filter(Cluster == i) |> 
        distinct(gene) |>  
        pull(gene) |> 
        as.list()
      
      # =========== 3.2. Perform Enrichment Analysis ===========
      enrich_cluster_list[[paste0(name, "_", i)]] <- enrichGO(
        gene = genes_cluster_list[[paste0(name, "_c", i)]],  
        OrgDb = org.Hs.eg.db,
        keyType = "SYMBOL",
        ont = "BP",
        pvalueCutoff = .05,
        qvalueCutoff = .05
      )
      
      df_enrich <- as.data.frame(enrich_cluster_list[[paste0(name, "_", i)]])
      
      # =========== 3.3. Save Enrichment Results ===========
      
      write.csv(df_enrich, 
                file = paste0(output_dir, "GSEA_cluster_", name, "_", i, ".csv"), 
                row.names = FALSE)
      
      # =========== 3.4. Generate and Save cnetplot ===========
      cnet <- cnetplot(enrich_cluster_list[[paste0(name, "_", i)]], 
                       layout = 'circle', 
                       showCategory = 5, 
                       color_edge = "category")
      

      if (name %in% c("top", "bottom")) {
        title_chart <- paste0("GSEA circular plot of cluster ", i, " based on ", name , " Jaccard similarity clustering")
      } else if (name %in% c("global", "local")) {
        title_chart <- paste0("GSEA circular plot of cluster ", i, " based on ", name , " PRR-based clustering")
      } else {
        title_chart <- paste0("GSEA circular plot of cluster ", i, " based on ", name , " similarity clustering")
      }
      
      cnet <- cnet + ggplot2::ggtitle(title_chart)
      

      
      ggplot2::ggsave(paste0(img_dir, "cnetplot_", name, "_", i, ".png"), cnet, width = 15, height = 15)
      
    }  # End cluster loop
  }  # End if max_cluster > 0
}  # End type_cluster loop





