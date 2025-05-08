# ADCoexpressionNetwork
Scripts (Python and R) for article <b>Network analysis of potential antidepressant gene mechanisms and side effects </b>

# Index
1. [Requirements](#Requirements)
2. [First steps](#first-steps-downloading-essential-files)
3. [Obtaining results](#obtaining-results)
4. [Scripts](#scripts-explanation)
    1. [R](#r)
        1. [Starting_Script_R.R](#starting_script_rr)
        2. [Vecindarios_Unicos.R](#vecindarios_unicosr)
        3. [GSEA_uniques_top_bottom.R](#gsea_uniques_top_bottomr)
        4. [GSEA_vecindarios_all.R](#gsea_vecindarios_allr)
    2. [Python](#python)
        1. [LINCS_ad_gene_nw_construction_modified.py](#lincs_ad_gene_nw_construction_modifiedpy)
        2. [LINCS_ad_gene_nw_symbol_mapping.py](#lincs_ad_gene_nw_symbol_mappingpy)
        3. [LINCS_ad_effects_nw_construction.py](#lincs_ad_effects_nw_constructionpy)
        4. [ad_Tanimoto_similarity.py](#ad_tanimoto_similaritypy)
        5. [ad_gene_Jaccard_similarity.py](#ad_gene_jaccard_similaritypy)
        6. [ad_effects_Jaccard_similarity.py](#ad_effects_jaccard_similaritypy)
        7. [ad_nsh_clustering.py](#ad_nsh_clusteringpy)
        8. [ad_gene_nw_analysis.ipynb](#ad_gene_nw_analysisipynb)
        9. [ad_adr_local_nw_analysis.ipynb](#ad_adr_local_nw_analysisipynb)
        10. [ad_adr_global_nw_analysis.ipynb](#ad_adr_global_nw_analysisipynb)
    3. [Bash](#bash)
        1. [download_LINCS.sh](#download_lincssh)
        2. [python_scripts.sh](#python_scriptssh)
        3. [Additional_Scripts/install_dependencies.sh](#additional_scriptsinstall_dependenciessh)

## Requirements
<ul>
  <li> <b>105 GB of storage</b> approximately ( 100Gb for GEO Series GSE92742 & 5Gb for FAERS DB 2014-2023)
  </li>
  <li> <b>Python 3.7</b> <i>using conda as python and package versioning</i>,  used Python 3.7 because of issues with the package cmapPy with newer versions. You could try also with pip installation of cmapPy.
  </li>
  <li> <b>R 4.5</b> </br>
  The renv.lock file was based on R (v = 4.5) and BiocManager(v = 3.21) for Linux Ubuntu. We will list the necessary packages so that you may run the script with different R and BiocManager versions: 
    <ul>
      <li>renv (not necessary if you are not going to generate reproducible environments)</li>
      <li>tidyverse</li>
      <li>dplyr</li>
      <li>ggplot2</li>
      <li>tidyverse</li>
      <li>BiocManager
        <ul>
          <li>clusterProfiler</li>
          <li>org.Hs.eg.db</li>
        </ul>
      </li>
    </ul>
  </li>
  <li> <b>PRR data</b> obtained from a repository  <a href="https://github.com/TAKMU/FAERS"> FAERS_database </a>
  </li>
</ul>

## First steps, downloading essential files:
<ol>
  <li> <b>Run scrip <i>download_LINCS.sh</i></b> </br> Use this script to download essential files (GEO Series GSE92742) for the project. If there are issues with the bash script, please download the following files (decompress and place them in data directory) from this <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742">link</a>:
    <ul>
      <li>GSE92742_Broad_LINCS_Level3_INF_mlr12k_n1319138x12328.gctx.gz</li>
      <li>GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx.gz</li>
      <li>GSE92742_Broad_LINCS_gene_info.txt.gz</li>
      <li>GSE92742_Broad_LINCS_pert_info.txt.gz</li>
      <li>GSE92742_Broad_LINCS_inst_info.txt.gz</li>
    </ul>
  </li>
  <li> <b>Obtain PRR values from FAERS 2014-2023.</b> Filter all the inf values (from results of https://github.com/TAKMU/FAERS), the resulting file is <i>prr_filtered.csv</i>
  </li>
  <li> <b>Activate conda environment cmapPy3</b> The environment file is <i>environment.yml.</i></br>
    <code> conda env create -f environment.yml </code>
    </br>In case that you are having difficulties with the conda environment, we are listing all the necessary packages. Please use Python 3.7 to run these scripts as cmapPy requires this Python version. 
    <ul>
      <li>cmapPy (in windows, please download the package with pip).</li>
      <li>pandas</li>
      <li>numpy</li>
      <li>altair</li>
      <li>vl-convert-python</li>
      <li>scipy</li>
      <li>matplotlib</li>
      <li>pubchempy</li>
      <li>rdkit</li>
      <li>networkx</li>
    </ul>
  </li>
  <li>In case that you are having difficulties with renv, we are listing all the necessary libraries. Please consider that we used R 4.5 to run these scripts. In case it is your first time using these libraries, it may be necessary to install some dependencies on Linux. We added a bash script for ubuntu to download these dependencies <code>./Additional_Scripts/install_dependencies.sh</code> 
    <ul>
      <li>tidyverse</li>
      <li>dplyr</li>
      <li>clusterProfiler</li>
      <li>org.Hs.eg.db</li>
      <li>ggplot2</li>
    </ul>
  </li>
  </ol>
  
 ## Obtaining results:
 Please consider that all the results and essential data will be located in the directories ./data and ./img. Csv files will be located in data and heatmaps, gsea or hierarchical clustering will be located on img. 
  <ol>
  <li>Run script python_scripts.sh</li>
  <li>Run Starting_script_R.R</br>
  If you are not planning on applying reproducible environment, please delete the following line (17-18) </br>
    <code>if (!requireNamespace("renv", quietly = TRUE)) install.packages("renv")
    renv::restore()</code>
  </li>
  <li>Run jupyter notebook: ad_adr_local_nw_analysis.ipynb</li>
  <li>Run jupyter notebook: ad_gene_nw_analysis.ipynb</li>
</ol>

## Scripts (explanation):
### R

#### Starting_Script_R.R
<ul>
  <li><b>Details:</b> This script runs all the scripts necessary to do GSEA analysis for top and bottom expressed genes; GSEA analysis of clusters according to tanimoto, jaccard top and bottom expressed genes, and jaccard local and global PRR.</li>    
  <li>Input: 
    <ul>
      <li>./data/LINCS_ad_gene_nw_modified_with_symbols.csv</li>
      <li>./data/structural_ad_clustering.csv</li>
      <li>./data/functional_top_ad_clustering.csv</li>
          <li>./data/functional_bottom_ad_clustering.csv</li>
          <li>./data/functional_global_ad_clustering.csv</li>
          <li>./data/functional_local_ad_clustering.csv</li>
        </ul>
      </li>
      <li>Output
        <ul>
          <li>./data/genes_top_unicos.csv</li>
          <li>./data/genes_bottom_unicos.csv</li>
          <li>./data/enr_top_genes.csv</li>
          <li>./data/enr_bottom_genes.csv</li>
          <li>./img/cnetplot_top.png</li>
          <li>./img/cnetplot_bottom.png</li>
          <li>GSEA csv files of clusters ("./data/GSEA_cluster_DATA-TYPE_CLUSTER-NUMBER.csv", data type can be top, bottom, global, local, tanimoto)</li>
          <li>GSEA png files of clusters("./img/cnetplot_DATA-TYPE_CLUSTER-NUMBER.png", data type can be top, bottom, global, local, tanimoto)</li>
        </ul>
      </li>
    </ul>
  </li>

#### Vecindarios_Unicos.R
<ul>
  <li><b>Details:</b> This script filters the top and bottom expressed unique genes from the dataframe of LINCS only including the 28 antidepressants.</li>    
  <li>Input: 
    <ul>
      <li>./data/LINCS_ad_gene_nw_modified_with_symbols.csv</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./data/genes_top_unicos.csv</li>
      <li>./data/genes_bottom_unicos.csv</li>
    </ul>
  </li>
</ul>

#### GSEA_uniques_top_bottom.R
  <ul>
    <li><b>Details:</b> This script generates GSEA analysis of the top and bottom unique genes obtained from Vecindarios_Unicos.R</li>    
    <li>Input: 
      <ul>
        <li>./data/genes_top_unicos.csv</li>
        <li>./data/genes_bottom_unicos.csv</li>
      </ul>
    </li>
    <li>Output
      <ul>
        <li>./data/enr_top_genes.csv</li>
        <li>./data/enr_bottom_genes.csv</li>
        <li>./img/cnetplot_top.png</li>
        <li>./img/cnetplot_bottom.png</li>
      </ul>
    </li>
  </ul>

#### GSEA_vecindarios_all.R 
  <ul>
    <li><b>Details:</b> This script generates GSEA analysis for each cluster grouped by similarities with different criteria: tanimoto, jaccard of top and bottom expressed genes, and jaccard of local and global PRR (adverse events of antidepressants).</li>     
    <li>Input: 
      <ul>
        <li>./data/LINCS_ad_gene_nw_modified_with_symbols.csv</li>
        <li>./data/structural_ad_clustering.csv</li>
        <li>./data/functional_top_ad_clustering.csv</li>
        <li>./data/functional_bottom_ad_clustering.csv</li>
        <li>./data/functional_global_ad_clustering.csv</li>
        <li>./data/functional_local_ad_clustering.csv</li>
      </ul>
    </li>
    <li>Output
      <ul>
        <li>GSEA csv files of clusters ("./data/GSEA_cluster_CRITERIA_CLUSTER-NUMBER.csv", criteria can be top, bottom, global, local, tanimoto)</li>
        <li>GSEA png files of clusters("./img/cnetplot_CRITERIA_CLUSTER-NUMBER.png", criteria can be top, bottom, global, local, tanimoto)</li>
      </ul>
    </li>
  </ul>


### Python
#### LINCS_ad_gene_nw_construction_modified.py
<ul>
  <li><b>Details:</b> This script filters only the antidepressants from LINCS to obtain expressed genes from AD.</li>     
  <li>Input: 
    <ul>
      <li>./data/GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx</li>
      <li>./data/GSE92742_Broad_LINCS_inst_info.txt</li>
      <li>antidepressants.tsv</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./data/LINCS_ad_gene_nw_modified.csv</li>
    </ul>
  </li>
</ul>

#### LINCS_ad_gene_nw_symbol_mapping.py
<ul>
  <li><b>Details:</b> This script translates de gene id into gene symbols.</li>     
  <li>Input: 
    <ul>
      <li>./data/LINCS_ad_gene_nw_modified.csv</li>
      <li>./data/GSE92742_Broad_LINCS_gene_info.txt</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./data/LINCS_ad_gene_nw_modified_with_symbols.csv</li>
    </ul>
  </li>
</ul>
  
#### LINCS_ad_effects_nw_construction.py
<ul>
  <li><b>Details:</b> This script generates a network based on the PRR (Proportional Reporting Ratio of FAERS, https://github.com/TAKMU/FAERS/)</li>     
  <li>Input: 
    <ul>
      <li>antidepressants.tsv</li>
      <li>./data/prr_filtered.csv</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./data/global_ad_ars_network.csv</li>
      <li>./data/local_ad_ars_network.csv</li>
    </ul>
  </li>
</ul>

#### ad_Tanimoto_similarity.py
<ul>
  <li><b>Details:</b> This script generates Tanimoto similarity matrix and a heatmap of it.</li>     
  <li>Input: 
    <ul>
      <li>./data/LINCS_ad_gene_nw_modified_with_symbols.csv</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./data/tanimoto_matrix.csv</li>
      <li>./img/tanimoto_similarity.png</li>
    </ul>
  </li>
</ul>

#### ad_gene_Jaccard_similarity.py
<ul>
  <li><b>Details:</b> This script generates Jaccard similarity matrix and heatmaps of top and bottom expressed genes.</li>     
  <li>Input: 
    <ul>
      <li>./data/LINCS_ad_gene_nw_modified_with_symbols.csv</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./data/jaccard_top_matrix.csv</li>
      <li>./data/jaccard_bottom_matrix.csv</li>
      <li>./img/top_gene_heatmap.png</li>
      <li>./img/bottom_gene_heatmap.png</li>
    </ul>
  </li>
</ul>

#### ad_effects_Jaccard_similarity.py
<ul>
  <li><b>Details:</b> This script generates Jaccard similarity matrix and heatmaps of global and local PRR values.</li>     
  <li>Input: 
    <ul>
      <li>./data/global_ad_ars_network.csv</li>
      <li>./data/local_ad_ars_network.csv</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./data/jaccard_local_matrix.csv</li>
      <li>./data/jaccard_global_matrix.csv</li>
      <li>./img/local_heatmap.png</li>
      <li>./img/global_heatmap.png</li>
    </ul>
  </li>
</ul>

#### ad_nsh_clustering.py
<ul>
  <li><b>Details:</b> This script clusters group of antidepressants according to different criteria (tanimoto, jaccard top and bottom expressed genes, and jaccard local and global PRR values.). It saves the hierarchical clustering and the labelling of the antidepressants according to the criteria.</li>     
  <li>Input: 
    <ul>
      <li>./data/tanimoto_matrix.csv</li>
      <li>./data/jaccard_top_matrix.csv</li>
      <li>./data/jaccard_bottom_matrix.csv</li>
      <li>./data/jaccard_global_matrix.csv</li>
      <li>./data/jaccard_local_matrix.csv</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>./img/clustering_structural.png</li>
      <li>./data/structural_ad_clustering.csv</li>
      <li>./img/clustering_top_gene.png</li>
      <li>./data/functional_top_ad_clustering.csv</li>
      <li>./img/clustering_bottom_gene.png</li>
      <li>./data/functional_bottom_ad_clustering.csv</li>
      <li>./img/clustering_global.png</li>
      <li>./data/functional_global_ad_clustering.csv</li>
      <li>./img/clustering_local.png</li>
      <li>./data/functional_local_ad_clustering.csv</li>
    </ul>
  </li>
</ul>

#### ad_gene_nw_analysis.ipynb
<ul>
  <li><b>Details:</b> This jupyter notebook realizes the network analysis of antidepressant-gene network.</li>     
</ul>

#### ad_adr_local_nw_analysis.ipynb
<ul>
  <li><b>Details:</b> This jupyter notebook realizes the network analysis of antidepressant-adverse effect network considering local PRR values.</li>     
</ul>

#### ad_adr_global_nw_analysis.ipynb
<ul>
  <li><b>Details:</b> This jupyter notebook realizes the network analysis of antidepressant-adverse effect network considering global PRR values.</li>     
</ul>

### Bash
#### download_LINCS.sh
<ul>
  <li><b>Details:</b> Downloads all the necessary files obtained from LINCS to replicate the research.</li>  
  <li>Output
    <ul>
      <li>./data/GSE92742_Broad_LINCS_Level3_INF_mlr12k_n1319138x12328.gctx.gz</li>
      <li>./data/GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx.gz</li>
      <li>./data/GSE92742_Broad_LINCS_gene_info.txt.gz</li>
      <li>./data/GSE92742_Broad_LINCS_pert_info.txt.gz</li>
      <li>./data/GSE92742_Broad_LINCS_inst_info.txt.gz</li>
    </ul>
  </li>
</ul>

#### python_scripts.sh
<ul>
  <li><b>Details:</b> Runs all the necessary python scripts in the correct order.</li>  
  <li>Input
    <ul>
      <li>./data/GSE92742_Broad_LINCS_Level3_INF_mlr12k_n1319138x12328.gctx.gz</li>
      <li>./data/GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx.gz</li>
      <li>./data/GSE92742_Broad_LINCS_gene_info.txt.gz</li>
      <li>./data/GSE92742_Broad_LINCS_pert_info.txt.gz</li>
      <li>./data/GSE92742_Broad_LINCS_inst_info.txt.gz</li>
    </ul>
  </li>
  <li>Output
    <ul>
      <li>All output files of other python scripts</li>
    </ul>
  </li>
</ul>

#### Additional_Scripts/install_dependencies.sh
<ul>
  <li><b>Details:</b> Bash script to download dependencies of libraries of R in Ubuntu. It isn't required if the user has used BiocManager libraries before.</li>     
</ul>


