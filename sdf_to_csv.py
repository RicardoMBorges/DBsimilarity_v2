# This script will search for .sdf files in the specified folder and its subfolders, 
#process each one, and save the corresponding CSV files with the same name in the same 
#directory as the original SDF file. Make sure to replace the folder_path variable with 
#the path to your folder containing the .sdf files.

# Run: activate the env_rmb_rdkit, navegate to the path where this file is saved and run it
# python sdf_to_csv.py

import os
from rdkit.Chem import PandasTools

# Specify the folder containing your .sdf files
folder_path = "/home/nmrbox/rborges/Desktop/GitHub/PriorizaNaturais_DBsimilarity/Salix/"

# Function to process an SDF file and save it as CSV
def process_sdf_file(file_path):
    try:
        df = PandasTools.LoadSDF(file_path, embedProps=True, molColName=None, smilesName='smiles')
        csv_filename = os.path.splitext(file_path)[0] + ".csv"
        df.to_csv(csv_filename, sep=";")
        print(f"Processed {file_path} and saved as {csv_filename}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

# Recursively traverse the folder and its subfolders
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".sdf"):
            sdf_file_path = os.path.join(root, file)
            process_sdf_file(sdf_file_path)
