import os
from rdkit.Chem import PandasTools

# Function to process an SDF file and save it as CSV
def process_sdf_file(file_path):
    try:
        df = PandasTools.LoadSDF(file_path, embedProps=True, molColName=None, smilesName='smiles')
        csv_filename = os.path.splitext(file_path)[0] + ".csv"
        df.to_csv(csv_filename, sep=";")
        print(f"Processed {file_path} and saved as {csv_filename}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

# Main function to convert SDF files in the specified folder to CSV
def convert_sdf_to_csv(folder_path):
    # Recursively traverse the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sdf"):
                sdf_file_path = os.path.join(root, file)
                process_sdf_file(sdf_file_path)

# Example usage
folder_path = "C:\\Users\\borge\\Documents\\DBsimilarity\\Mikania\\"
convert_sdf_to_csv(folder_path)
