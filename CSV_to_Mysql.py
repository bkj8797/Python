# 파이썬 & MariaDB 연동
# !pip install mysqlclient
# !pip install mysql


# csv파일을 읽을 수 있도록 필요한 라이브러리와 모듈 import
import csv
import MySQLdb
import sys
from datetime import datetime, date

# csv 파일의 이름과 경로를 지정해서 input
input_file = 'supplier_data.csv'

# MySQL DB와 연결
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='kitri10', passwd='kitri10')

#커서가 선택할 수 있도록 승인	
c = con.cursor()

# 데이터를 읽어 suppliers 테이블에 입력하는 함수. 읽기속성, utf-8로 인코딩, 필드 구분을 콤마(,)로 하겠다는 뜻
file_reader = csv.reader(open(input_file, 'r', encoding='utf-8'), delimiter=',')	#읽기속성, utf-8로읽어, 필드구분을 컴마로하겠다

# 열어준 파일에 next()함수를 이용해 header 변수에 저장
header = next(file_reader)

# 헤더를 제외한 1번째 행부터 마지막까지 가져옴
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
# $ : 라인의 끝
# 콤마(,) 기호를 제거하고 좌우 공백을 뺌으로써 왼쪽 정렬
			data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())	
		else:

# 날짜 형식, 소문자y는 20만 표시, 대문자Y는 2020으로 표시
			a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))			
			a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)

# execute() 함수로 Suppliers 테이블에 정보를 넣는다.
	c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)

# 정보 삽입 종료 후 데이터를 commit하는 함수
con.commit()