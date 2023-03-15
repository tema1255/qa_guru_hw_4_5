'''
В новом проекте, соответствующему базовому формату «проекта для автотестов»,
разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form
'''
import os

from selene import browser, have, command
from selenium.webdriver import ActionChains, Keys

def test_form(browser_setup):
    browser.element('#firstName').type('Artem')
    browser.element('#lastName').type('Chekanov')
    browser.element('#userEmail').type('tema-42@mail.ru')
    browser.element('[for="gender-radio-1"]').click()       #почему ту через '#gender-radio-1' не работает, а в отдельном работает
    browser.element('#userNumber').type('9876543210')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1987"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="3"]').click()
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('math').press_enter().type('eng').press_enter()
    browser.driver.execute_script('window.scrollTo(0,150)')
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/0.jpeg')
    browser.element('#currentAddress').type('До востребования!')
    browser.element('#react-select-3-input').type('raj').press_enter()
    browser.element('#react-select-4-input').type('jai').press_enter()
    browser.element('#submit').perform(command.js.click)


def test_firstName_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Artem')


def test_lastName_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#lastName').type('Chekanov')


def test_email_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#userEmail').type('tema-42@mail.ru')


def test_gender_click():
    browser.config.hold_browser_open = True
    browser.config.click_by_js = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#gender-radio-1').click()
    #    browser.element('#gender-radio-1').perform(command.js.click)


def test_userNumber_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#userNumber').type('9876543210')


def test_birth_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1987"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="3"]').click()
    browser.element('.react-datepicker__day--002').click()

def test_subj_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#subjectsInput').type('math').press_enter().type('eng').press_enter()

def test_hobbi_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element("[for='hobbies-checkbox-1']").click()
   # browser.element("#hobbies-checkbox-1").click()
    browser.element("[for='hobbies-checkbox-3']").click()

def test_picture_upload():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script('window.scrollTo(0,150)')
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/0.jpeg')


def test_currentAdress_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script('window.scrollTo(0,150)')
    browser.element('#currentAddress').type('До востребования!')


def test_state_and_city_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script('window.scrollTo(0,150)')
    browser.element('#react-select-3-input').type('raj').press_enter()
    browser.element('#react-select-4-input').type('jai').press_enter()
    browser.element('#submit').perform(command.js.click)