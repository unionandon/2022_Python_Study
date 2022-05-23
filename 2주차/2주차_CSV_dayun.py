## 2022-05-19
'''
“test*.brcastory.tsv”를 읽어와 각각의 파일에 변이가 몇개씩있는지 출력하고 
각각의 파일의 변이를 모두 합쳐서 하나의 파일로 만만들어주세요
'''
import os, sys, csv, glob

input_path = os.getcwd()
out_f = '{}/merge_brca.csv'.format(input_path)

f_cnt = 0
first_file = True
for input_f in glob.glob(os.path.join(input_path, 'test*.brcastory.tsv')):
    r_cnt = 0
    with open(input_f, 'r', newline='') as tsv_inf:
        with open(out_f, 'a', newline='') as tsv_outf:
            freader = csv.reader(tsv_inf, delimiter='\t')
            fwriter = csv.writer(tsv_outf, delimiter=',')
            if first_file:
                header_list = ["Gene", "Pos", "exon_NM", "HGVS", "zygosity", "other_names", "Polymorphism"]
                fwriter.writerow(header_list)
                for row in freader:
                    fwriter.writerow(row)
                    print(row)
                    r_cnt += 1                
                first_file = False
            else:
                for row in freader:
                    fwriter.writerow(row)
                    r_cnt += 1
    print('{0!s}: \t{1:d} variants '.format(os.path.basename(input_f), r_cnt))
    f_cnt += 1

print('Number of files : {0:d}'.format(f_cnt))


