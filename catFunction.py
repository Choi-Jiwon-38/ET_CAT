from selenium import webdriver


wl = "wordList.txt"
wdList = []

def updateWordList():
    driver = webdriver.Chrome('C:/Download/chromedriver.exe')
    url = "https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800"
    driver.get(url)

    xpath = "//table[@class='prettytable']//dd/a"

    # find_elements_by_xpath 함수 ->  조건에 맞는 태그(요소)를 모두 찾아 리스트에 저장
    wordList_1 = driver.find_elements_by_xpath(xpath)
    wordList_2 = []  # wordList_1의 요소들을 텍스트로 변환한 뒤 저장할 빈 리스트 생성
    for w in wordList_1:
        word = w.text  # wordList_1 의 요소를 변환
        if len(word) != 1:  # 글자 1개로 이루어진 단어는 저장 X <- 끝말잇기에서 사용하지 않음
            wordList_2.append(word)

    wordList_2 = list(set(wordList_2))  # 중복되는 단어를 제거
    wordList_2.sort()  # 리스트 내부 단어들 '가나다' 순으로 정리

    f = open(wl, 'w')  # w 명령어 이용 (.txt 파일에 저장 용도)
    for word in wordList_2:
        f.write(word + ' ')  # write 명령어로 내용 작성
    f.close()  # close 명령어로 파일 닫기

def loadWordList():
    f = open(wl, 'r')
    wordData = f.read()
    wdList = wordData.split(' ')
    wdList.pop(-1) # txt 파일 저장에 공백을 넣어두었기 때문에, 마지막 공백은 지워줌
