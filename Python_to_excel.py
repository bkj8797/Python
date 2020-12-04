# 엑셀 관련 모듈 설치

# !pip install xlrd
# !pip install xlwt
# !pip install xlsxwriter
# !pip install matplotlib
# !pip install pandas




# 1. 엑셀 파일 생성 1단계 : 데이터 선언(작성)
# 파이썬으로 엑셀 만들기
import pandas as pd
# 딕셔너리 : 행과 열을 동시에 입력
excel_exam_data1 = {'학생' : ['김민지', '신진선', '신세은', '이중석', '염찬호'],
                   '국어' : [30, 90, 36, 5, 35],
                   '영어' : [30, 90, 36, 5, 35],
                   '수학' : [30, 90, 36, 5, 35]
                   } 

# 2. 엑셀 서식화
# 입력한 데이터를 엑셀서식화 한다.
df1 = pd.DataFrame(excel_exam_data1, columns = ['학생', '국어', '영어', '수학'])


# 3. 엑셀파일에 데이터 작성 후 저장하기
# 엑셀 파일 생성하기
excel_writer = pd.ExcelWriter('학생시험성적.xlsx', engine = 'xlsxwriter') #엑셀파일을 생성하는 모듈

# 엑셀 파일에 데이터 작성하기
df1.to_excel(excel_writer, index=False) # false 이거 안 해주면 0 1 2 3 4가 학생 열로 들어옴

# 데이터 저장 후 닫기
excel_writer.save()

pd.read_excel('학생시험성적2.xlsx')
