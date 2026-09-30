import anndata as ad
import pandas as pd
from sort_and_search_funs import *
from util_funs import *

def filter_mt_cells(anndata_obj, mt_exp_lvl_threshold, gene_exp_threshold):
                    
#Validate thresholds
                    
    if not 0 <= mt_exp_lvl_threshold <=1:
        raise ValueError("Mitochondrial threshold must be between 0 and 1")
    if not 0 <= gene_exp_threshold <= 2000:
        raise ValueError("Gene threshold must be between 0 and 2000")
	
		

# Copy the cell metadata so the original stays unchanged.
    original_cells = anndata_obj.T.var.copy()
    original_index_name = original_cells.index.name

    rows = (
    original_cells
    .rename_axis("cell_barcode")
    .reset_index()
    .to_dict("records")
    )

    algorithms = {
    "Merge recursive": timer_decorator(merge_sort_recursive),
    "Merge iterative":timer_decorator(merge_sort_iterative),
    }

    filtered_results = {}
    timings = []

    for algorithm_name, sort_function in algorithms.items():

# Each algorithm receives a fresh copy of the original,
# unsorted rows. Copying is outside the timed section.
        input_rows = [row.copy() for row in rows]

# Stage 1: Sort mitochondrial expression, highest first.


        mt_sorted = sort_function(
            input_rows,
            key=lambda row: row["percent_mito"],
            reverse=True
        )

        timings.append({
            "algorithm": algorithm_name,
            "stage": "percent_mito descending",
            "number_of_cells": len(input_rows),
            "seconds": sort_function.last_elapsed
        })

# Keep cells at or BELOW the mitochondrial threshold.
        mt_filtered = pd.DataFrame(
            mt_sorted,
            columns=["cell_barcode", *original_cells.columns]
        )

        mt_filtered = mt_filtered.loc[
            mt_filtered["percent_mito"] <= mt_exp_lvl_threshold
        ].copy()

# Stage 2: Sort surviving cells by gene count, lowest first.
        gene_rows = mt_filtered.to_dict("records")

        gene_sorted = sort_function(
            gene_rows,
            key=lambda row: row["n_genes"],
            reverse=False
        )

        timings.append({
            "algorithm": algorithm_name,
            "stage": "n_genes ascending",
            "number_of_cells": len(gene_rows),
            "seconds": sort_function.last_elapsed
        })

        gene_filtered = pd.DataFrame(
            gene_sorted,
            columns=["cell_barcode", *original_cells.columns]
        )

# Keep cells at or ABOVE the gene threshold.
        gene_filtered = gene_filtered.loc[
            gene_filtered["n_genes"] >= gene_exp_threshold
        ].copy()

# Restore cell barcodes as the DataFrame index.
        gene_filtered = gene_filtered.set_index("cell_barcode")
        gene_filtered.index.name = original_index_name

        filtered_results[algorithm_name] = gene_filtered

    return filtered_results, pd.DataFrame(timings)



if __name__ == "__main__":
    adata = ad.read_h5ad("./data/pbmc_sample.h5ad")

# Inspect cell metadata
    cells = adata.T.var
    print(cells.shape)
    print(cells.columns.tolist())
    print(cells.head())
    print(cells[["percent_mito", "n_genes"]].head())
    print(cells["percent_mito"].describe())
    
    
    results, timing_table = filter_mt_cells(
        adata,
        mt_exp_lvl_threshold=0.05,
        gene_exp_threshold=200
    )

    print("\nSorting times:")
    print(timing_table.to_string(index=False))

    for algorithm_name, filtered_cells in results.items():
        print(f"\n{algorithm_name}: {len(filtered_cells)} cells retained")
        print(filtered_cells[["percent_mito", "n_genes"]].head())

# Compare retained cells and their metadata.
# Sorting by barcode here permits different ordering of tied values.
    pd.testing.assert_frame_equal(
        results["Merge recursive"].sort_index(),
        results["Merge iterative"].sort_index()
    )

    timing_table.to_csv("sorting_times.csv", index=False)

    
