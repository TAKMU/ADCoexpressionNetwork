# ADCoexpressionNetwork
Scripts (Python and R) for article <b>Network analysis of potential antidepressant gene mechanisms and side effects </b>

## Requirements for this repository:
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

<ul>
  <li> Starting_Script_R.R
    <ul>    
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
        </ul>
      </li>
  </li>
</ul>
