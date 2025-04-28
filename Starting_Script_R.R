# ----------------------------------------------------------------------------
# Script Title: Starting Script
# Author: Allan Ken Miyazono Ushijima
# Creation Date: 2025-02-21
# Last Update: 2025-02-21
# Version: 1.0
# Description: 
# This script is to run all the scripts with the correct version of the libraries
# using renv. 
#
# ----------------------------------------------------------------------------
# Changes:
# - [2025-02-21] Script creation. (Allan Ken Miyazono Ushijima)
# ----------------------------------------------------------------------------


if (!requireNamespace("renv", quietly = TRUE)) install.packages("renv")
renv::restore()
source("Vecindarios_Unicos.R")
source("GSEA_uniques_top_bottom.R")
source("GSEA_vecindarios_all.R")
