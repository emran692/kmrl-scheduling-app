import subprocess

# List of notebooks in order
notebooks = [
    "notebooks/01_data_analysis.ipynb",
    "notebooks/02_model_training.ipynb",
    "notebooks/03_optimization_engine.ipynb",
    "notebooks/04_save_model.ipynb"
]

for nb in notebooks:
    print(f"\n Running {nb} ...")
    subprocess.run([
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute", nb,
        "--inplace"
    ])
    print(f" Finished {nb}")

print("\n All notebooks executed successfully!")
