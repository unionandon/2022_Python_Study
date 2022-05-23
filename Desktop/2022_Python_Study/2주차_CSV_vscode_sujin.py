## 2022-05-12
'''
“test*.brcastory.tsv”를 읽어와 각각의 파일에 변이가 몇개씩있는지 출력하고 
각각의 파일의 변이를 모두 합쳐서 하나의 파일로 만만들어주세요
'''
#!/usr/bin/env python3

import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'test*')):
    row_counter = 1 
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
    print('{0!s}: \t{1:d} variants'.format(\
        os.path.basename(input_file), row_counter))
    file_counter += 1
print('Number of files: {0:d}'.format(file_counter))

first_file = True
for input_file in glob.glob(os.path.join(input_path,'test*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
        
            else:
                header = next(filereader)
                for row in filereader:
                    filewriter.writerow(row)