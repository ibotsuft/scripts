import csv
import os

def merge_csv(path_folder, filename_output):
    csv_files = [file for file in os.listdir(path_folder) if file.endswith('.csv')]

    if len(csv_files) < 2:
        print("At least two csv files are necessary to merge.")
        return

    data = []
    header = None
    for csv_file in csv_files:
        with open(os.path.join(path_folder, csv_file), 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_lines = list(csv_reader)

            if header is None:
                header = csv_lines[0]
            else:
                if header != csv_lines[0]:
                    print(f"The header file {csv_file} does not match with the others files.")
                    return
            
            data.extend(csv_lines[1:])

    with open(filename_output, 'w', newline='') as csv_output:
        csv_writer = csv.writer(csv_output)
        csv_writer.writerow(header)

        for line in data:
            csv_writer.writerow(line)

    print(f"The files were merged with sucess in {filename_output}")


if __name__ == "__main__":
    folder = '/home/kali/ibots/statsfile/iBots_x_HeliosBase_541/rcg_rcl/'
    file_output = 'iBots_x_HeliosBase_541.csv'

    merge_csv(folder, file_output)