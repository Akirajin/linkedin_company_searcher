import csv
import json
import os

import searcher

PATH_TO_INPUT = 'input'
PATH_TO_OUTPUT = 'output'


def save_every_company_to_output_file(company_url):
    with open(f'{PATH_TO_OUTPUT}/output', "w") as f:
        json.dump(company_url, f, indent=4)


def find_all_urls_and_save_in():
    company_url = {}
    companies = get_every_company_name_from_csv_files(PATH_TO_INPUT)

    for company in companies:
        result = searcher.google_api(company)
        company_url[company] = result

    save_every_company_to_output_file(company_url)


def get_every_company_name_from_csv_files(path):
    companies = []
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):

            try:
                with open(file_path, "r") as f:
                    print(f"File: {filename}")
                    reader = csv.reader(f)
                    for row in reader:
                        for company in row:
                            companies.append(company.strip())
            except csv.Error as e:
                print(f"Error reading CSV file: {e}")
    return companies


if __name__ == '__main__':
    find_all_urls_and_save_in()
