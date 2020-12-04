import webbrowser

urls = ['https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=',
        'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=',
        'https://search.daum.net/nate?thr=sbma&w=tot&q=',
        'https://www.google.com/#q=']

#search_words = {'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' : '이천쌀',
#                'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=' : '이천도자기',
#                'https://search.daum.net/nate?thr=sbma&w=tot&q=' : '이천복숭아',
#                'https://www.google.com/#q=' : '이천반도체'}
search_words = ["이천쌀","이천도자기","이천복숭아","이천반도체"]

for i in range(0, len(search_words)) :
    url = urls[i] + search_words[i]
#    print(url)
    webbrowser.open_new(url)