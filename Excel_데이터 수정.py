# 통합

import pandas as pd
from glob import glob

excel_file_name = '담당자별_판매량통합.xlsx'
excel_total_file_writer = pd.ExcelWriter(excel_file_name, engine=xlsxwriter)
total_data2.to_excel(excel_total_file_writer, index=False, sheet_name='담당자별_판매량_통합')

excel_total_file_writer.save()
glob(excel_file_name)
print()
pd.read_excel(excel_file_name)