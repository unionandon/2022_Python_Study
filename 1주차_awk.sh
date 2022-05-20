File=$1
awk -F ',' '$2 > 100000000 && $3~/^rs/ {print$0}' $File
