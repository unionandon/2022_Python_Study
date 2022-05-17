## 2022-05-12
'''
“2022_05_study.csv”를 읽어와 POS 이 ‘100,000,000’ 이상이면서 \
ID가 ‘rs’로 시작하는 행만 필터링 진행하여 그 결과를 출력 파일에 기록해주세요. (Sys , re 사용)
'''
#!/usr/bin/env python3
import csv
import re
import sys

input_file =sys.argv[1]
output_file =sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^rs.*)')

with open(input_file,'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            pos = str(row_list[1].strip())
            id = row_list[2]
            if (float(pos)>= 100000000) and (pattern.search(id)):
                filewriter.writerow(row_list)
