import os

if os.getenv("USING_HPC") == "1":
  # To change the path, just change this line. The rest of the code will automatically adapt to it.
  base_path = ""
else:
  base_path = "g_test"

dir = ["train", "test", "validation"]

dataset = ["cic2017"]
data_name = dataset[0]

for d in dir:
  os.makedirs(f"{base_path}/{d}", exist_ok=True)
  os.makedirs(f"{base_path}/{d}/benign", exist_ok=True)
  os.makedirs(f"{base_path}/{d}/malicious", exist_ok=True)
  for file in os.listdir(f"{base_path}/{d}/benign"):
    os.rename(f"{base_path}/{d}/benign/{file}", f"{base_path}/{d}/benign/{data_name}_{d[:5]}_ben_{file}")
  for file in os.listdir(f"{base_path}/{d}/malicious"):
    os.rename(f"{base_path}/{d}/malicious/{file}", f"{base_path}/{d}/malicious/{data_name}_{d[:5]}_mal_{file}")