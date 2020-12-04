# !pip install PyPDF2
# !pip install textract
# !pip install nltk
# !pip install pdfminer3k

import PyPDF2
pdfFileObj = open('meetingminutes1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages # 전체 페이지
pageObj = pdfReader.getPage(0) # 페이지 지정

pageObj.extractText() #글자 추출하는 함수
# 원본대로 출력하는 방법
print(pageObj.extractText())