# fp_benchmarking

This repository generates benchmark split files (train/test/validation) for a
binary malware-classification dataset organized into two folders: `benign` and
`malicious`.

## What This Code Does

The main script `benchmark_gen_all.py`:

1. Selects a dataset root path based on the `USING_HPC` environment variable.
2. Reads file names from:
	 - `<base_path>/benign`
	 - `<base_path>/malicious`
3. Creates labels:
	 - `benign` for files from the benign folder
	 - `malware` for files from the malicious folder
4. Performs stratified splits using scikit-learn:
	 - First split: 80% temp / 20% test
	 - Second split: 90% train / 10% validation from the temp set

Final effective split ratio is:
- Train: 72%
- Validation: 8%
- Test: 20%

The split uses `random_state=42` and stratification to keep class balance and
reproducibility.

## Input Expectations

Expected directory structure under `base_path`:

```
<base_path>/
	benign/
		file_a.pkl
		file_b.pkl
		...
	malicious/
		file_x.pkl
		file_y.pkl
		...
```

The script stores only file names, not full paths, in output lists.

## Output Files And Storage Format

The script writes four files:

- `benchmark_train.txt`
- `benchmark_test.txt`
- `benchmark_validation.txt`
- `benchmark_stats.txt`

### Per-sample file format

Each line in `benchmark_train.txt`, `benchmark_test.txt`, and
`benchmark_validation.txt` is:

```
<filename> <label>
```

Example:

```
12345.pkl benign
98765.pkl malware
```

### Stats file content

`benchmark_stats.txt` includes:

- Total sample count
- Split sizes (train/test/validation)
- Per-class counts in each split
- A line documenting storage format: `<filename> <label>`

## Where Files Are Written

If `USING_HPC=1`:

- Input base path:
	`/home/bmitra/processed/androzoo_pickles_chirantan`
- Output directory:
	`/home/bmitra/Benchmarks/<dataset_name>/`

If `USING_HPC` is not `1`:

- Input base path:
	`pruned_graphs_chirantan`
- Output directory:
	`./<dataset_name>/`

`dataset_name` is inferred as the last segment of `base_path`.

## Running On HPC (SLURM)

`compute.sh` is a SLURM batch script that:

1. Requests compute resources.
2. Loads Anaconda.
3. Activates the `malware_analysis` conda environment.
4. Exports `USING_HPC=1`.
5. Runs `python benchmark_gen_all.py`.

Submit with:

```bash
sbatch compute.sh
```

## Running Locally

Install dependency:

```bash
pip install scikit-learn
```

Then run:

```bash
python benchmark_gen_all.py
```

## Notes

- The random seed is fixed (`42`), so reruns on the same input produce the same
	split assignment.