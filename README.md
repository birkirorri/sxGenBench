# sxGenBench - Benchmark of generative models for single cell RNA
Later
![image](https://github.com/user-attachments/assets/4606a96d-6310-40af-b5ea-0a7cac2df0cf)
Figure shows the general workflow for the benchmark

Each model has it's own folder: 
- Biolord
- CPA
- trVAE
- scGen
- DRVI
- scVI
- Linear model

in each model folder there is a folder for each dataset run


Seperate folder is available which has the disentanglement metric implemented in this benchmark

## Standard benchmarking workflow (Blue)

Files that end with _standard are the standard workflow. This includes model training after the defult pipelines,
reconstruction and disentanglement calculations

## Counterfactul predictions (Red) 

Files that end with _LOO are the counterfactual predictions


## Integration benchmark (Green) ---- And notes on how to run it

The "integration_Benchmark" folder has all of the integration benchmarks that were done. 
The data used there is the extracted test_data for each dataset and also the reconstructed data which is in the .obsm as "X_reconstructed", 
The X_reconstructed is then compared to the original test_data

Notes about running the scib benchmark: 

1. Install the scib package
2. Install anndata2ri
3. Launch an R enviorment in the terminal and do the following
    - library (devtools)
    - install_github("theislab/kBET")
  


## Notes on how to run each model if there are issues: 

CPA: 

CPA requires pytorch version 24.01 when using a GPU (Ucloud version). Using a newer version will cause package conflicts which could at least be fixed in a ucloud environment. If the user was running this locally this could be fixed more easily. 
The stable version of CPA did not work so the developmental version was required. 
After installing CPA importing caused an “ModuleNotFoundError” with tkinter,  the only solution was found was to remove the “from tkinter import N” line located in the cpa/_model.py. 
Tkinter is not used anywhere else in the code so it does not have an effect on the functionality of the model. 


scGen: 

scGen requires pytorch version 24.01 when using a GPU (Ucloud version). 


trVAE:

trVAE requires pytorch version 24.01 when using a GPU (Ucloud version). 




## Datasets

Raw processed datasets: 
https://figshare.com/articles/dataset/Raw_datasets/29179964

Log transformed and normalized datasets: 
https://figshare.com/articles/dataset/Normalized_and_log_transformed_data/29179742
