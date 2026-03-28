#!/bin/bash
#SBATCH -p compute
#SBATCH -N 1
#SBATCH -n 4
#SBATCH --mem 200000M
#SBATCH -t 4-0:0
#SBATCH --job-name="Organising pyg_out_dir"
#SBATCH --chdir=/home/bmitra/Rakshita/bphc-malware-analysis
#SBATCH -o /home/bmitra/Rakshita/jobs/%j-%x/out.out
#SBATCH -e /home/bmitra/Rakshita/jobs/%j-%x/err.err
#SBATCH --mail-user=f20232010@hyderabad.bits-pilani.ac.in
#SBATCH --mail-type=ALL
module load anaconda3-2021.05-gcc-8.5.0-i5w2nbn

eval "$(conda shell.bash hook)"

conda activate malware_analysis

export USING_HPC=1

cd /home/bmitra/Rakshita/bphc-malware-analysis

python smol_script.py 1 1 0