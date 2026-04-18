import os
import argparse


def get_base_path() -> str:
  parser = argparse.ArgumentParser(description="Rename dataset files with split and label prefixes.")
  parser.add_argument(
    "--path",
    type=str,
    help="Base dataset path to use when running on HPC (USING_HPC=1).",
  )
  args = parser.parse_args()

  if os.getenv("USING_HPC") == "1":
    if not args.path:
      parser.error("When USING_HPC=1, --path is required.")
    return args.path

  return "g_test"

base_path = get_base_path()

dir = ["train", "test", "validation"]

dataset = ["cic2017"]
data_name = dataset[0]

for d in dir:
  os.makedirs(f"{base_path}/{d}", exist_ok=True)
  os.makedirs(f"{base_path}/{d}/benign", exist_ok=True)
  os.makedirs(f"{base_path}/{d}/malicious", exist_ok=True)
  for file in os.listdir(f"{base_path}/{d}/benign"):
    if not file.startswith(f"{data_name}_{d[:5]}_ben_"):
        os.rename(f"{base_path}/{d}/benign/{file}", f"{base_path}/{d}/benign/{data_name}_{d[:5]}_ben_{file}")
  for file in os.listdir(f"{base_path}/{d}/malicious"):
    if not file.startswith(f"{data_name}_{d[:5]}_mal_"):
        os.rename(f"{base_path}/{d}/malicious/{file}", f"{base_path}/{d}/malicious/{data_name}_{d[:5]}_mal_{file}")