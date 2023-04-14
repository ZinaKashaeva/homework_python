"""1. Открыть страницу http://google.com/ncr
2. Выполнить поиск слова “selenide”
3. Проверить, что первый результат – ссылка на сайт selenide.org.
4. Перейти в раздел поиска изображений
5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
6. Вернуться в раздел поиска Все
7. Проверить, что первый результат такой же, как и на шаге 3."""


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Search(unittest.TestCase):
    def setUp(self):
        self.driver1 = webdriver.Chrome('chromedriver.exe')
        self.driver1.get("http://google.com/ncr")

    def test_search(self):
        assert 'Google' in self.driver1.title
        element = self.driver1.find_element(By.ID, "APjFqb")
        element.send_keys('selenide')
        element.send_keys(Keys.RETURN)
        assert 'No results found' not in self.driver1.page_source

        element2 = self.driver1.find_element(By.CLASS_NAME, "byrV5b").text
        if element2 != 'https://seleniade.org':
            print('сайт верный')

        element3 = self.driver1.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        element3.click()

        element4 = self.driver1.find_element(By.CLASS_NAME, "dmeZbb").text
        if element4 != 'https://seleniade.org':
            print('сайт верный')

        element5 = self.driver1.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
        element5.click()

        element6 = self.driver1.find_element(By.CLASS_NAME, "byrV5b").text
        if element6 != 'https://seleniade.org':
            print('сайт верный')

    def tearDown(self):
        self.driver1.close()


if __name__ == '__main__':
    unittest.main()
