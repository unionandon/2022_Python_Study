## 2022-05-12
'''
“test*.brcastory.tsv”를 읽어와 각각의 파일에 변이가 몇개씩있는지 출력하고 
각각의 파일의 변이를 모두 합쳐서 하나의 파일로 만만들어주세요
'''

import sys, os, glob, csv

input_path = sys.argv[1]
output_li = list()
for i in glob.glob(os.path.join(input_path,'test*')):
    row_counter = 0
    with open(i,'r',newline='') as input_file:
        filereader = csv.reader(input_file)
        for row in filereader:
            row_counter += 1
            print(row)
            output_li.append(row)
            #filewriter.writerow(row)
        print(row_counter)
    with open('2en_output','w',newline='') as output:
        filewriter = csv.writer(output)
        for row in output_li:
            filewriter.writerow(row)
