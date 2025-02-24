# ADCoexpressionNetwork
Scripts (Python and R) for article <b>Network analysis of potential antidepressant gene mechanisms and side effects </b>

## Requirements for this repository:
<ul>
  <li> <b>105 GB of storage</b> approximately ( 100Gb for GEO Series GSE92742 & 5Gb for FAERS DB 2014-2023)
  </li>
  <li> <b>Python 3.7</b> <i>using conda as python and package versioning</i>,  used Python 3.7 because of issues with the package cmapPy with newer versions. 
  </li>
  <li> <b>R 4.4.2</b>
  </li>
  <li> <b>PRR data</b> obtained from the repository FAERS_database (<i>pending</i>)
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
  <li> <b>Obtain PRR values from FAERS 2014-2023.</b> The resulting file is <i>prr_filtered.csv</i>
  </li>
  <li> <b>Activate conda environment cmapPy3</b> The environment file is <i>environment_linux.yml.</i></br>
    <code> conda env create -f environment.yml </code>
    </br>In case that you are having difficulties with the conda environment, we are listing all the necessary packages. Please use Python 3.7 to run these scripts. 
    <ul>
      <li>cmapPy</li>
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
</ol>
