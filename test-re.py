import re

def clean_txt(doc_ko) :
    clean_doc = re.sub('[^ㄱ-ㅎ가-힣\s]', '', doc_ko)
    print(clean_doc)


clean_txt('가가.aaaaaaaaa 나난나나나')