if (!requireNamespace("renv", quietly = TRUE)) {
  install.packages("renv")
}
library(renv)

# 1. Find installed packages
installed_pkgs <- installed.packages()

# 2. Find base or recommended packages (skip these)
base_pkgs <- rownames(installed_pkgs[installed_pkgs[, "Priority"] %in% c("base", "recommended"), ])

# 3. Find user packages (non-base)
user_pkgs <- setdiff(rownames(installed_pkgs), base_pkgs)

# 4. Update only user packages
renv::update(packages = user_pkgs)

# 5. Snapshot to update renv.lock
renv::snapshot()

cat("\n✅ Packages updated and renv.lock refreshed successfully!\n")