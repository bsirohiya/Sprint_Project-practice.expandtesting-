import pytest

from time import sleep
from pages.ui.delete_note import DeleteNote
from pages.ui.login import LoginPage
from utils.loggers import get_logger
from utils.performance import get_page_load_time


@pytest.mark.ui
@pytest.mark.order(7)
def test_delete_note(setup_and_teardown):

    logger = get_logger(__name__)
    logger.info("Starting test_delete_note")

    driver = setup_and_teardown
    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    lp = LoginPage(driver)
    lp.login()

    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")

    dn = DeleteNote(driver)

    # Count notes before delete
    notes_before = len(dn.get_all_notes())

    dn.scroll_to_amt(280)
    dn.click_delete_btn()
    dn.click_confirm_delete_btn()

    sleep(2)

    # Count notes after delete
    notes_after = len(dn.get_all_notes())

    assert notes_after == notes_before - 1, \
        "Note was not deleted successfully"

    logger.info("Note deleted successfully")