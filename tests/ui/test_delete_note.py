from time import sleep

from pages.ui.delete_note import DeleteNote
from pages.ui.login import LoginPage


def test_delete_note(setup_and_teardown):
    driver = setup_and_teardown

    lp = LoginPage(driver)
    lp.login()

    dn = DeleteNote(driver)

    sleep(2)
    dn.scroll_to_amt(270)
    dn.click_delete_btn()
    dn.click_confirm_delete_btn()