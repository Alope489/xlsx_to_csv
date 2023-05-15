import pandas as pd
import sys
import os

def xlsx_to_csv(file_path):

    df = pd.read_excel(file_path)
    
    df.replace('_', '|', regex=True, inplace=True)

    df_transposed = df.transpose()

    base_file_name = os.path.basename(file_path).split('.')[0]

    output_file_name = f"{base_file_name}_transposed.csv"

    df_transposed.to_csv(output_file_name, sep='\t', index=False)

    print(f"Transposed file has been saved as {output_file_name}")
    
    #needs the reformatting code for the header lines and the name.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xlsx_to_csv.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    xlsx_to_csv(file_path)
