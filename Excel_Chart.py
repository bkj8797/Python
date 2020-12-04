import matplotlib.pyplot as plt # 그림그리는거임
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

sales = {
    '시간' : [9, 10, 11, 12, 13, 14, 15],
    '제품1' : [10, 15, 12, 11, 19, 14, 13],
    '제품2' : [9, 11, 4, 12, 13, 10, 12]
}


df = pd.DataFrame(sales, index=sales['시간'], columns= ['제품1', '제품2'])

df.index.name = '시간'





matplotlib.rcParams['font.family'] = 'Malgun gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

product_plot = df.plot(grid = True, style = ['-*', 'o'], title = '시간대별 생산량')
image_file = 'excel.png'
plt.savefig(image_file, dpi = 400)
plt.show()



# 엑셀 객체 생성

excel_chart = pd.ExcelWriter('data_chart.xlsx',
                            engine='xlsxwriter')
# 엑셀에 삽입

df.to_excel(excel_chart, index=True, sheet_name='Chart')
# 엑셀 파일과 엑셀 시트 생성

workbook = excel_chart.book
worksheet = excel_chart.sheets['Chart'] # 위의 sheet_name과 맞아야함

# 원하는 차트 종류 지정하기

chart = workbook.add_chart({'type' : 'line'})
# 차트 생성을 위한 데이터 범위 지정

chart.add_series({'values' : '=Chart!$B$2:$B$8'})
chart.add_series({'values' : '=Chart!$C$2:$C$8'})
# 차트 제목과 라밸 지정

chart.set_title({'name' : '시간대별 생산량'})
chart.set_x_axis({'name' : '시간'})
chart.set_y_axis({'name' : '생산량'})
# 워크 시트에 차트가 들어갈 위치 지정

worksheet.insert_chart('D2', chart)
# 워크 시트에 차트가 들어갈 위치 지정

worksheet.insert_chart('D2', chart)
# 엑셀 객체 저장 후 닫기
excel_chart.save()
