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
  <li>Run script LINCS_ad_effects_nw_construction.py.</li>
</ol>
