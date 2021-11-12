from selenium import webdriver
driver = webdriver.Chrome('C:/Download/chromedriver.exe')

url = "https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800"
driver.get(url)

xpath = "//table[@class='prettytable']//dd/a"


wordList = driver.find_elements_by_xpath(xpath)
print(wordList)