## 2022-05-26 
'''
 "Variants_2022_05.xlsx" "Sheet2" 를 읽어와  
 frameshift variant를 가진 행 중에 Exon Number가 5 이상인 행을 가져온다.

Gene Name	Exon Number  HGVS pDot	Sequence Ontology Chr:Pos

헤더는 위의 순서대로 가져와서 새로운 엑셀 파일을 생성한다.
'''

#!/usr/bin/env python3
import pandas as pd
import sys 

input_f = "Variants_2022_05.xlsx"
output_f = "3주차_output_dayun.xlsx"

df = pd.read_excel(input_f, sheet_name="Sheet2", index_col = None)

df_f = df[df["Sequence Ontology"].str.startswith("frameshift")]
df_ff = df_f[df_f["Exon Number"].astype(float) > 5]
df_ff

df_ff = df_ff.loc[:, ["Gene Name", "Exon Number", "HGVS pDot", "Sequence Ontology", "Chr:Pos"]]
print(df_ff)
writer = pd.ExcelWriter(output_f)
df_ff.to_excel(writer, sheet_name = 'variant', index=False)
writer.save()