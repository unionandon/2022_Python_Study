import sys, re

input_f = sys.argv[1]
output_f = sys.argv[2]

pattern_ID = re.compile('rs*')

with open(input_f, 'r') as inputreader:
    with open(output_f, 'w') as outputwriter:
        input_file_header = inputreader.readline()
        input_file_header = input_file_header.strip()
        input_file_header_list = input_file_header.split(',')
        outputwriter.write(','.join(input_file_header_list)+'\n')
        for i in inputreader:
            row = i.strip().split(',')
            pos = row[1]
            id = row[2]
            if int(pos) > 100000000 and pattern_ID.search(id):
                outputwriter.write(','.join(row)+'\n')