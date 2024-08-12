import time

import pytest
from openpyxl import load_workbook
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

@pytest.mark.usefixtures("setup")
class BaseClass:
    pass


def convert_excel_data(excel_value, index):
    """Converts Excel data to match the format of the Web data."""
    if index == 0 or index == 8:  # Convert float-like numbers to integers
        return str(int(float(excel_value)))  # Convert to integer-like string, e.g., '55.0' -> '55'

    elif index == 2:  # Convert 'true'/'false' to 'active'/'yes'
        if isinstance(excel_value, bool):
            return "active" if excel_value else "inactive"
        return "active" if excel_value.lower() in ["true"] else "inactive"

    elif index == 9: # Convert 'true'/'false' to 'Yes'/'No'
        if isinstance(excel_value, bool):
            return "yes" if excel_value else "no"
        return "yes" if excel_value.lower() == 'True' else "no"

    elif index == 3 or index == 6:  # Convert date formats
        try:
            return datetime.strptime(excel_value, "%d-%m-%Y").strftime("%d-%b-%Y").lower()
        except ValueError:
            return excel_value  # Return as is if the date is in an unexpected format

    elif index == 4 or index == 7:  # Convert 'none' values to '-'
        if excel_value is None:
            return "-"
        return "-" if excel_value.lower() == "none" else excel_value

    return excel_value  # Return the value unchanged if no conversion is needed


def read_excel(file_path):
    workbook = load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=5, values_only=True):
        # Apply conversion to each cell in the row
        modified_row = [convert_excel_data(cell, index) for index, cell in enumerate(row)]
        data.append(modified_row)

    return data


# def convert_web_data(web_value, index):
#     """Converts web data to match the format of the Excel data."""
#     if index == 0 or index == 8:  # Convert float-like numbers
#         return f"{float(web_value)}"  # Ensure it matches Excel's float format
#
#     elif index == 2 or index == 9:  # Convert status and boolean values
#         return "true" if web_value.lower() in ["active", "yes"] else "false"
#
#     elif index == 3 or index == 6:  # Convert date formats
#         try:
#             return datetime.strptime(web_value, "%d-%b-%Y").strftime("%d-%m-%Y")
#         except ValueError:
#             return web_value  # Return as is if the date is in an unexpected format
#
#     elif index == 4 or index == 7:  # Convert 'none' values
#         return "none" if web_value == "-" else web_value
#
#     return web_value  # Return the value unchanged if no conversion is needed


def get_web_data(driver):
    wait = WebDriverWait(driver, 10)
    data = []

    while True:
        rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table//tr")))

        for row in rows[1:]:  # Skipping the header row
            cols = row.find_elements(By.TAG_NAME, "td")
            data.append([col.text.strip() for col in cols[1:]])
            print("Reached the try block")
            # web_row = [convert_web_data(col.text.strip(), index) for index, col in enumerate(cols[1:])]
            # data.append(web_row)
        # Check if there's a "Next" button or similar pagination control
        print("Reached the try block")  # Debugging print before try block
        try:
            next_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[aria-label='Next page']"))
            )
            # Scroll to the "Next" button using ActionChains
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            print("Scrolled to the Next button")  # Debugging print

            # Click the "Next" button
            next_button.click()
            print("Clicked Next button")  # Debugging print

            # Wait until the rows are stale, meaning the new page has loaded
            wait.until(EC.staleness_of(rows[0]))
            print("Page loaded, moving to next")  # Debugging print
        except Exception as e:
            # No more pages or error occurred
            print(f"Pagination ended or an error occurred: {e}")
            break

    return data


def normalize_data(data):
    return [[str(cell).strip().lower() for cell in row] for row in data]


def compare_data(file_data, web_data):
    file_data_normalized = normalize_data(file_data)
    web_data_normalized = normalize_data(web_data)

    if file_data_normalized == web_data_normalized:
        print("The data in the file matches the data on the web application.")
    else:
        print("The data in the file does not match the data on the web application.")
        print("File Data:")
        for row in file_data_normalized:
            print(row)
        print("Web Data:")
        for row in web_data_normalized:
            print(row)
