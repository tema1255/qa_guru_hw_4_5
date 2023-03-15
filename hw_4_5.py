'''
В новом проекте, соответствующему базовому формату «проекта для автотестов»,
разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form
'''
from selene import browser, have, command


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
    browser.element('#gender-radio-1').perform(command.js.click)

def test_userNumber_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#userNumber').type('9876543210')

def test_birth_type():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#dateOfBirthInput').type('9876543210')

