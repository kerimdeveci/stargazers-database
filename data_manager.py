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
            f_l = []
            f_l.append(item['name'])
            f_l.append(item['html_url'])
            f_l.append(item['description'])
            f_l.append(item['created_at'])
            f_l.append(item['updated_at'])
            f_l.append(item['stargazers_count'])
            f_l.append(item['language'])
            val.append(f_l)
        return val

    def fetch_data(self):
        for page in range(1, 8):
            url = f'https://api.github.com/users/{self.userName}/starred?per_page=100&page={page}'
            response = requests.get(url)
            js = response.json()
            self.values.extend(self.append_new_data(js))
            return self.values
