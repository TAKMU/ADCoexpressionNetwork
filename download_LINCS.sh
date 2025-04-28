#!/bin/bash

#This scripts downloads and decompresses all the necessary files for the project
#the files used in this project are located in this URL: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742

mkdir data
cd data

wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742%5FBroad%5FLINCS%5Fgene%5Finfo%2Etxt%2Egz
wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742%5FBroad%5FLINCS%5Finst%5Finfo%2Etxt%2Egz
wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742%5FBroad%5FLINCS%5FLevel3%5FINF%5Fmlr12k%5Fn1319138x12328%2Egctx%2Egz
wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742%5FBroad%5FLINCS%5FLevel4%5FZSPCINF%5Fmlr12k%5Fn1319138x12328%2Egctx%2Egz
wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742%5FBroad%5FLINCS%5Fpert%5Finfo%2Etxt%2Egz

gzip -d GSE92742_Broad_LINCS_Level3_INF_mlr12k_n1319138x12328.gctx.gz
gzip -d GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx.gz
gzip -d GSE92742_Broad_LINCS_gene_info.txt.gz
gzip -d GSE92742_Broad_LINCS_pert_info.txt.gz
gzip -d GSE92742_Broad_LINCS_inst_info.txt.gz



