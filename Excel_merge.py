import pandas as pd
from glob import glob
import sys
excel_path = sys.argv[1]

excel_data_files3 = glob(excel_path)
total_data3 = pd.DataFrame()

for f in excel_data_files3 : 
    df = pd.read_excel(f)
    total_data2 = total_data3.append(df, ignore_index=True)
    
print(total_data3)

# 모든 엑셀파일 통함
# !python excel_merge.py d:/python/'담당자*'

#쓸 때는 excel_data_files3 이런식으로 숫자 바꿔서 충돌 안 나게