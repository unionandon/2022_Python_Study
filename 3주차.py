## 2022-05-26 
'''
 "Variants_2022_05.xlsx" "Sheet2" 를 읽어와  
 frameshift variant를 가진 행 중에 Exon Number가 5 이상인 행을 가져온다.
Gene Name	Exon Number  HGVS pDot	Sequence Ontology Chr:Pos
헤더는 위의 순서대로 가져와서 새로운 엑셀 파일을 생성한다.
'''

import pandas as pd

input_xlsx = "Variants_2022_05.xlsx"
output_xlsx = "taewoo.xlsx"
df = pd.read_excel(input_xlsx, sheet_name="Sheet2", index_col = None)

df_fs = df[df['Sequence Ontology']=='frameshift_variant']
df_fs_en = df_fs[df_fs['Exon Number']>5]
print(df_fs_en)

fin_df = df_fs_en.loc[:, ["Gene Name", "Exon Number", "HGVS pDot", "Sequence Ontology", "Chr:Pos"]]

writer = pd.ExcelWriter(output_xlsx)
fin_df.to_excel(writer, sheet_name = 'variant', index=False)
writer.save()