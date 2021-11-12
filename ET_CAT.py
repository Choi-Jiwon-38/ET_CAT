from selenium import webdriver
driver = webdriver.Chrome('C:/Download/chromedriver.exe')

url = "https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800"
driver.get(url)

xpath = "//table[@class='prettytable']//dd/a"

# find_elements_by_xpath 함수 ->  조건에 맞는 태그(요소)를 모두 찾아 리스트에 저장
wordList_1 = driver.find_elements_by_xpath(xpath) 
wordList_2 = [] # wordList_1의 요소들을 텍스트로 변환한 뒤 저장할 빈 리스트 생성
for w in wordList_1:
    word = w.text # wordList_1 의 요소를 변환
    # print(word) # debug_1 :: 텍스트 형태 변환 확인 용도
    wordList_2.append(word)

print(wordList_2) # debug_2 :: 리스트 저장 확인 용도
