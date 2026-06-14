"""Performance testing utilities for measuring page load times"""

def get_page_load_time(driver):
    """
    Get the page load time in milliseconds using Navigation Timing API
    Returns the total page load time from start to completion

    Args:
        driver: Selenium WebDriver instance

    Returns:
        float: Page load time in milliseconds
    """
    try:
        # Get navigation timing data from the browser
        navigation_start = driver.execute_script("return window.performance.timing.navigationStart")
        load_complete = driver.execute_script("return window.performance.timing.loadEventEnd")

        # Calculate load time in milliseconds
        load_time = load_complete - navigation_start

        return load_time if load_time > 0 else 0
    except Exception as e:
        return 0

