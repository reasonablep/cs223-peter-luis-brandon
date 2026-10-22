import scanpy as sc
import pandas as pd

def main():
    adata = sc.read_10x_mtx(
        "data/raw/",
        var_names = "gene_symbols",
        make_unique=True,
    )

    metadata=pd.read_csv(
        "data/raw/meta.tsv",
        sep="\t"
        index_col=0
    )

    if not metadata.index_is_unique:
        raise ValueError("metadata contains duplicate cell IDs")

    missing = adata.obs_names.difference(metadata.index)
    if len(missing) > 0:
        raise ValueError(
            f"{len(missing)} cells have no matching metadata"
            )
