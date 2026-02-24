from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # Ссылка для проверки (замените на вторую для теста падения)
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Используем уникальные селекторы для обязательных полей (first, second, third)
    # Эти селекторы ищут инпуты внутри контейнеров обязательных полей
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("test@example.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ожидание для визуального контроля и закрытие браузера
    time.sleep(5)
    browser.quit()