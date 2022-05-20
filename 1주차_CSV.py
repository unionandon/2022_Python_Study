## 2022-05-12
'''
“2022_05_study.csv”를 읽어와 POS 이 ‘100,000,000’ 이상이면서 \
ID가 ‘rs’로 시작하는 행만 필터링 진행하여 그 결과를 출력 파일에 기록해주세요. (Sys , re 사용)
'''

import sys, csv, re

inf = sys.argv[1] #"2022_05_study.csv"
outf = sys.argv[2] #"1주차_다윤"

pattern = re.compile("rs*")

with open(inf, 'r', newline = '') as csv_inf:
    with open(outf, 'w', newline = '') as csv_outf:
        freader = csv.reader(csv_inf)
        fwriter = csv.writer(csv_outf)
        header = next(freader)
        fwriter.writerow(header)
        for row_list in freader:
            POS = float(row_list[1])
            ID = str(row_list[2]).strip()
            if POS > 100000000 and pattern.search(ID):
                fwriter.writerow(row_list)

        

