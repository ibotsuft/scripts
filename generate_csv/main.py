import os
from datetime import datetime
import subprocess

def extract_date_from_filename(file_name):
    data_str = file_name[:14]
    data = datetime.strptime(data_str, "%Y%m%d%H%M%S")
    return data

def list_rcg_files(dir):
    files = os.listdir(dir)
    # rcg_files = [os.path.splitext(file)[0] for file in files if file.endswith('.rcg')]
    rcg_files = [file for file in files if file.endswith('.rcg')]
    rcg_files.sort(key=extract_date_from_filename)

    return rcg_files

target_dir = "/home/kali/ibots/statsfile/iBots_x_HeliosBase_original_formation/rcg_rcl"

rcg_files = list_rcg_files(target_dir)

iteration = 1

for file in rcg_files:

    ourTeamName = f"iBots_Dev_{iteration}"
    iteration = iteration + 1
    bash = ['bash', 'generate_csv.sh', file, ourTeamName]
    subprocess.run(bash, cwd=target_dir)
