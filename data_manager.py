import requests
import csv
import sqlite3


class data_manager:

    def __init__(self, userName, outputFileName):
        super().__init__()
        self.userName = userName
        self.outputFileName = outputFileName
        self.values = [['name', 'html_url', 'description',
                        'created_at', 'updated_at', 'stargazers_count', 'language']]

    def write_col(self, data):
        outputFileName = f'{self.outputFileName}.csv'
        with open(outputFileName, 'w') as file:
            writer = csv.writer(file)
            for d in data:
                writer.writerow(d)

    def append_new_data(self, json_data):
        val = []
        for item in json_data:
            fl = []
            fl.append(item['name'])
            fl.append(item['html_url'])
            fl.append(item['description'])
            fl.append(item['created_at'])
            fl.append(item['updated_at'])
            fl.append(item['stargazers_count'])
            fl.append(item['language'])

        return val

    def fetch_data(self):
        for page in range(1, 8):
            url = f'https://api.github.com/users/{self.userName}/starred?per_page=100&page={page}'
            response = requests.get(url)
            js = response.json()
            self.values.extend(self.append_new_data(js))
            return self.values
