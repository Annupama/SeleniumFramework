import pytest
from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass


def read_excel(file_path):
    workbook = load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    return data


def get_web_data(driver):
    wait = WebDriverWait(driver, 10)
    data = []

    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table//tr")))

    for row in rows[1:]:  # Skipping the header row
        cols = row.find_elements(By.TAG_NAME, "td")
        data.append([col.text.strip() for col in cols])

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
