# Benchmark list definition
import os
from sklearn.model_selection import train_test_split

if os.getenv("USING_HPC") == "1":
  # To change the path, just change this line. The rest of the code will automatically adapt to it.
  base_path = "/home/bmitra/processed/androzoo_pickles_chirantan"
else:
  base_path = "pruned_graphs_chirantan"

dataset_name = base_path.split("/")[-1]
benign_dir = os.path.join(base_path, "benign")
malware_dir = os.path.join(base_path, "malicious")

X = os.listdir(benign_dir) + os.listdir(malware_dir)
Y = ["benign"] * len(os.listdir(benign_dir)) + ["malware"] * len(os.listdir(malware_dir))

X_temp, X_test, Y_temp, Y_test = train_test_split(
    X, 
    Y, 
    test_size=0.2,       # 20% for testing, 80% for training
    random_state=42,     # Ensures reproducibility
    stratify=Y           # Stratify based on the target variable y
)

X_train, X_val, Y_train, Y_val = train_test_split(
    X_temp, 
    Y_temp, 
    test_size=0.1,       # 10% for val, 90% for training
    random_state=42,     # Ensures reproducibility
    stratify=Y_temp           # Stratify based on the target variable y
)



if os.getenv("USING_HPC") == "1":
  os.makedirs(f"/home/bmitra/Benchmarks/{dataset_name}", exist_ok=True)
  benchmark_train = f"/home/bmitra/Benchmarks/{dataset_name}/benchmark_train.txt"
  benchmark_test = f"/home/bmitra/Benchmarks/{dataset_name}/benchmark_test.txt"
  benchmark_val = f"/home/bmitra/Benchmarks/{dataset_name}/benchmark_validation.txt"
  benchmark_stats = f"/home/bmitra/Benchmarks/{dataset_name}/benchmark_stats.txt"

else:
  os.makedirs(f"{dataset_name}", exist_ok=True)
  benchmark_train = f"{dataset_name}/benchmark_train.txt"
  benchmark_test = f"{dataset_name}/benchmark_test.txt"
  benchmark_val = f"{dataset_name}/benchmark_validation.txt"
  benchmark_stats = f"{dataset_name}/benchmark_stats.txt"

with open(benchmark_stats, "w") as f_stats:
  f_stats.write(f"Total samples: {len(X)}\n")
  f_stats.write(f"Training samples: {len(X_train)}\n")
  f_stats.write(f"Testing samples: {len(X_test)}\n")
  f_stats.write(f"Validation samples: {len(X_val)}\n")

  benign_train, malware_train  = 0, 0
  benign_test, malware_test = 0, 0
  benign_val, malware_val = 0, 0
  with open(benchmark_train, "w") as f:
    for file, label in zip(X_train, Y_train):
      f.write(f"{file} {label}\n")
      if label == "benign":
        benign_train += 1
      else:
        malware_train += 1
      
  with open(benchmark_test, "w") as f:
    for file, label in zip(X_test, Y_test):
      f.write(f"{file} {label}\n")
      if label == "benign":
        benign_test += 1
      else:
        malware_test += 1

  with open(benchmark_val, "w") as f:
    for file, label in zip(X_val, Y_val):
      f.write(f"{file} {label}\n")
      if label == "benign":
        benign_val += 1
      else:
        malware_val += 1
  f_stats.write(f"Benign samples in training: {benign_train}\n")
  f_stats.write(f"Malware samples in training: {malware_train}\n")
  f_stats.write(f"Benign samples in testing: {benign_test}\n")
  f_stats.write(f"Malware samples in testing: {malware_test}\n")
  f_stats.write(f"Benign samples in validation: {benign_val}\n")
  f_stats.write(f"Malware samples in validation: {malware_val}\n")
  f_stats.write(f"Storing format: <filename> <label>\n")

