# Initialize renv (or activate if already initialized)
if (!requireNamespace("renv", quietly = TRUE)) {
  install.packages("renv")
}
renv::activate()
install.packages("codetools")
# Install BiocManager if not already present
if (!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager")
}
options(repos = BiocManager::repositories())

# Set Bioconductor version (optional but helps reproducibility)
BiocManager::install(version = "3.21")

# Set Bioconductor repositories so renv can track them
options(repos = BiocManager::repositories())
BiocManager::install(c(
  "AnnotationDbi",
  "DOSE",
  "enrichplot",
  "GO.db",
  "GOSemSim",
  "plyr",
  "qvalue"
))

# List Bioconductor packages
bioc_packages <- c(
  "GenomeInfoDbData",
  "clusterProfiler",
  "org.Hs.eg.db"
)

# List CRAN packages
cran_packages <- c(
  "tidyverse",
  "dplyr",
  "ggplot2"
)

# Install Bioconductor packages
BiocManager::install(bioc_packages, ask = FALSE, update = TRUE)

# Install CRAN packages
install.packages(cran_packages)

# Optional: load libraries to test installation (not required in script)
invisible(lapply(c(bioc_packages, cran_packages), library, character.only = TRUE))

# Snapshot the environment (capture CRAN + Bioconductor)
renv::snapshot(type = "all")