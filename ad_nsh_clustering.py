import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import pandas as pd

df_tan = pd.read_csv("./data/tanimoto_matrix.csv", index_col=0)
df_top_jac = pd.read_csv("./data/jaccard_top_matrix.csv", index_col=0)
df_bottom_jac = pd.read_csv("./data/jaccard_bottom_matrix.csv", index_col=0)
df_global_jac = pd.read_csv("./data/jaccard_global_matrix.csv", index_col=0)
df_local_jac = pd.read_csv("./data/jaccard_local_matrix.csv", index_col=0)
antidepressants = df_tan.index
antidepressants_eff = df_global_jac.index
dfs = [df.iloc[:, :].apply(pd.to_numeric, errors='coerce') for df in [df_tan, df_top_jac, df_bottom_jac, df_global_jac, df_local_jac]]
df_tan, df_top_jac, df_bottom_jac, df_global_jac, df_local_jac = dfs
tan, top_jac, bottom_jac, global_jac, local_jac = [df.to_numpy() for df in dfs]

################################################################################
# non-supervised hierarchical clustering for structural similarity
################################################################################
distance_matrix = sch.distance.pdist(tan, metric='euclidean')
linkage_matrix = sch.linkage(distance_matrix, method='complete')

plt.figure(figsize=(18, 12))
dendrogram = sch.dendrogram(linkage_matrix, labels=antidepressants, color_threshold=1.375)
for i, d in enumerate(dendrogram['dcoord']):
    x = dendrogram['icoord'][i]
    plt.plot(x, d, c=dendrogram['color_list'][i], linewidth=8)

plt.axhline(y=1.375, color='r', linestyle='--', label='cut-off threshold', linewidth=4)
plt.title('Non-supervised hierarchical clustering based on structural (Tanimoto) similarity profiles')
plt.xlabel('antidepressants')
plt.ylim(0, 1.75)
plt.yticks(np.arange(0, 2, 0.25))
plt.ylabel('euclidean distance')
plt.xticks(fontsize=10, rotation=90)
plt.legend(['1', '2', '3', '4', '5', '6'], title='k = 6', loc='upper right')

plt.tight_layout()  # Ajusta automáticamente los márgenes
plt.savefig("./img/clustering_structural.png")

cluster_labels = sch.fcluster(linkage_matrix, t=1.375, criterion='distance')
structural_ad_clustering = pd.DataFrame({'AD': df_tan.index, 'Cluster': cluster_labels})
structural_ad_clustering = structural_ad_clustering.sort_values(by=['Cluster', 'AD'])
structural_ad_clustering.reset_index(drop=True, inplace=True)
structural_ad_clustering.to_csv("./data/structural_ad_clustering.csv", index=False)
################################################################################
# non-supervised hierarchical clustering for top network functional perturbations similarity
################################################################################

distance_matrix = sch.distance.pdist(top_jac, metric='euclidean')
linkage_matrix = sch.linkage(distance_matrix, method='complete')

plt.figure(figsize=(18, 12))
dendrogram = sch.dendrogram(linkage_matrix, labels=antidepressants, color_threshold=1.350)
for i, d in enumerate(dendrogram['dcoord']):
    x = dendrogram['icoord'][i]
    plt.plot(x, d, c=dendrogram['color_list'][i], linewidth=8)

plt.axhline(y=1.350, color='r', linestyle='--', label='cut-off threshold', linewidth=4)
plt.title('Non-supervised hierarchical clustering based on top network functional (Jaccard) genetic perturbations similarity profiles')
plt.xlabel('antidepressants')
plt.ylim(0, 1.75)
plt.yticks(np.arange(0, 2, 0.25))
plt.ylabel('euclidean distance')
plt.xticks(fontsize=10, rotation=90)
plt.legend(['1', '2', '3', '4', '5', '6', '7'],  title='k = 7', loc='upper right')
plt.savefig("./img/clustering_top_gene.png")

cluster_labels = sch.fcluster(linkage_matrix, t=1.350, criterion='distance')
functional_top_ad_clustering = pd.DataFrame({'AD': df_top_jac.index, 'Cluster': cluster_labels})
functional_top_ad_clustering = functional_top_ad_clustering.sort_values(by=['Cluster', 'AD'])
functional_top_ad_clustering.reset_index(drop=True, inplace=True)
functional_top_ad_clustering.to_csv("./data/functional_top_ad_clustering.csv", index=False)

################################################################################
# non-supervised hierarchical clustering for bottom network functional perturbations similarity
################################################################################
distance_matrix = sch.distance.pdist(bottom_jac, metric='euclidean')
linkage_matrix = sch.linkage(distance_matrix, method='complete')

plt.figure(figsize=(18, 12))
dendrogram = sch.dendrogram(linkage_matrix, labels=antidepressants, color_threshold=1.365)
for i, d in enumerate(dendrogram['dcoord']):
    x = dendrogram['icoord'][i]
    plt.plot(x, d, c=dendrogram['color_list'][i], linewidth=8)

plt.axhline(y=1.365, color='r', linestyle='--', label='cut-off threshold', linewidth=4)
plt.title('Non-supervised hierarchical clustering based on bottom network functional (Jaccard) genetic perturbations similarity profiles')
plt.xlabel('antidepressants')
plt.ylim(0, 1.75)
plt.yticks(np.arange(0, 2, 0.25))
plt.ylabel('euclidean distance')
plt.xticks(fontsize=10, rotation=90)
plt.legend(['1', '2', '3', '4', '5'],  title='k = 5', loc='upper right')
plt.savefig("./img/clustering_bottom_gene.png")

cluster_labels = sch.fcluster(linkage_matrix, t=1.365, criterion='distance')
functional_bottom_ad_clustering = pd.DataFrame({'AD': df_bottom_jac.index, 'Cluster': cluster_labels})
functional_bottom_ad_clustering = functional_bottom_ad_clustering.sort_values(by=['Cluster', 'AD'])
functional_bottom_ad_clustering.reset_index(drop=True, inplace=True)
functional_bottom_ad_clustering.to_csv("./data/functional_bottom_ad_clustering.csv", index=False)

################################################################################
# non-supervised hierarchical clustering for functional global adverse effects similarity
################################################################################
distance_matrix = sch.distance.pdist(global_jac, metric='euclidean')
linkage_matrix = sch.linkage(distance_matrix, method='complete')
plt.figure(figsize=(18, 12))
dendrogram = sch.dendrogram(linkage_matrix, labels=antidepressants_eff, color_threshold=1.417)
for i, d in enumerate(dendrogram['dcoord']):
    x = dendrogram['icoord'][i]
    plt.plot(x, d, c=dendrogram['color_list'][i], linewidth=8)

plt.axhline(y=1.417, color='r', linestyle='--', label='cut-off threshold', linewidth=4)
plt.title('Non-supervised hierarchical clustering based on functional (Jaccard) global adverse effects similarity profiles')
plt.xlabel('antidepressants')
plt.ylim(0, 1.75)
plt.yticks(np.arange(0, 2, 0.25))
plt.ylabel('euclidean distance')
plt.xticks(fontsize=10, rotation=90)
plt.legend(['1', '2', '3'], title='k = 3', loc='upper right')
plt.savefig("./img/clustering_global.png")
cluster_labels = sch.fcluster(linkage_matrix, t=1.417, criterion='distance')
functional_eff_ad_clustering = pd.DataFrame({'AD': df_global_jac.index, 'Cluster': cluster_labels})
functional_eff_ad_clustering = functional_eff_ad_clustering.sort_values(by=['Cluster', 'AD'])
functional_eff_ad_clustering.reset_index(drop=True, inplace=True)
functional_eff_ad_clustering.to_csv("./data/functional_global_ad_clustering.csv", index=False)

################################################################################
# non-supervised hierarchical clustering for functional local adverse effects similarity
################################################################################
distance_matrix = sch.distance.pdist(local_jac, metric='euclidean')
linkage_matrix = sch.linkage(distance_matrix, method='complete')

plt.figure(figsize=(18, 12))
dendrogram = sch.dendrogram(linkage_matrix, labels=antidepressants_eff, color_threshold=1.415)
for i, d in enumerate(dendrogram['dcoord']):
    x = dendrogram['icoord'][i]
    plt.plot(x, d, c=dendrogram['color_list'][i], linewidth=8)

plt.axhline(y=1.415, color='r', linestyle='--', label='cut-off threshold', linewidth=4)
plt.title('Non-supervised hierarchical clustering based on functional (Jaccard) local adverse effects similarity profiles')
plt.xlabel('antidepressants')
plt.ylim(0, 1.75)
plt.yticks(np.arange(0, 2, 0.25))
plt.ylabel('euclidean distance')
plt.xticks(fontsize=10, rotation=90)
plt.legend(['1', '2', '3', '4'], title='k = 4', loc='upper right')
plt.savefig("./img/clustering_local.png")

cluster_labels = sch.fcluster(linkage_matrix, t=1.415, criterion='distance')

functional_eff_ad_clustering = pd.DataFrame({'AD': df_local_jac.index, 'Cluster': cluster_labels})


functional_eff_ad_clustering = functional_eff_ad_clustering.sort_values(by=['Cluster', 'AD'])

functional_eff_ad_clustering.reset_index(drop=True, inplace=True)

functional_eff_ad_clustering.to_csv("./data/functional_local_ad_clustering.csv", index=False)


