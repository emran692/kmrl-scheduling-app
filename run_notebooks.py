import os 
os.system("jupyter nbconvert --to notebook --execute notebooks/01_data_analysis.ipynb") 
os.system("jupyter nbconvert --to notebook --execute notebooks/02_model_training.ipynb") 
os.system("jupyter nbconvert --to notebook --execute notebooks/03_optimization_engine.ipynb") 
os.system("jupyter nbconvert --to notebook --execute notebooks/04_save_model.ipynb") 
