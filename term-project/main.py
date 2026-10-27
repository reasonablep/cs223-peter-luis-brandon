from pathlib import Path

import pandas as pd
import scanpy as sc

# Function for creation of h5ad file from raw data
def main():
    data_dir = Path("data/raw")
    output_dir = Path("output")

# Load expression counts, cell IDs, and gene information
    adata = sc.read_10x_mtx(
        data_dir,
        var_names="gene_symbols",
        make_unique=True,
    )

# Load information about each cell
    metadata = pd.read_csv(
        data_dir / "meta.tsv",
        sep="\t",
        index_col=0,
    )

    if not metadata.index.is_unique:
        raise ValueError("Metadata contains duplicate cell IDs")

    if not adata.obs_names.is_unique:
        raise ValueError("Count matrix contains duplicate cell IDs")

    missing = adata.obs_names.difference(metadata.index)

    if len(missing) > 0:
        raise ValueError(
            f"{len(missing)} cells have no matching metadata. "
            f"Examples: {missing[:5].tolist()}"
        )

# Match metadata rows to the exact cell order in the matrix
    adata.obs = metadata.loc[adata.obs_names].copy()

# Save the combined dataset
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "pdac_raw.h5ad"
    adata.write_h5ad(output_file, compression="gzip")

    print(f"Saved {output_file}")
    print(f"{adata.n_obs:,} cells × {adata.n_vars:,} genes")
    print(adata.obs.head())


if __name__ == "__main__":
    main()
