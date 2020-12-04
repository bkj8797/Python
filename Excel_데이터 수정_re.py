import re
import pandas as pd
from glob import glob

excel_data_files = glob('담당자별*사원.xlsx')

for i in  excel_data_files :
    df = pd.read_excel(i)
    
    if (df.loc[1, '담당자'] == 'A'):
        df['담당자'] = '김민지'
    elif (df.loc[1, '담당자'] == 'B'):
        df['담당자'] = '신세은'
    elif (df.loc[1, '담당자'] == 'C'):
        df['담당자'] = '염찬호'
        
    i_new = re.sub('.xlsx', '5.xlsx', i)
    print(i_new)
    
    new_excel_file = pd.ExcelWriter(i_new, engine = 'xlsxwriter')
    df.to_excel(new_excel_file, index=False)
    new_excel_file.save()