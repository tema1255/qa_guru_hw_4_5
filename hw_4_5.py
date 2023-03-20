'''
В новом проекте, соответствующему базовому формату «проекта для автотестов»,
разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form
'''
import os

from selene import browser, command, have


def test_my_version_student_registration(browser_setup):
    browser.element('#firstName').type('Artem')
    browser.element('#lastName').type('Chekanov')
    browser.element('#userEmail').type('tema-42@mail.ru')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').type('9876543210')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1987"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="3"]').click()
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('math').press_enter().type(
        'eng'
    ).press_enter()
    browser.driver.execute_script('window.scrollTo(0,150)')
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/0.jpeg')
    browser.element('#currentAddress').type('До востребования!')
    browser.element('#react-select-3-input').type('raj').press_enter()
    browser.element('#react-select-4-input').type('jai').press_enter()
    browser.element('#submit').perform(command.js.click)

    browser.element('//tbody/tr[1]/td[2]').should(have.text('Artem Chekanov'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('tema-42@mail.ru'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('9876543210'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('02 April,1987'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Maths, English'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports, Music'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('0.jpeg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('До востребования!'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Rajasthan Jaipur'))
