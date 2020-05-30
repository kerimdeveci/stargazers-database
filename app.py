import requests
import csv

values = [['name', 'html_url', 'description', 'created_at',
           'updated_at', 'stargazers_count', 'language']]


def write_col(data):
    with open('data2.csv', 'w') as file:
        writer = csv.writer(file)
        for d in data:
            writer.writerow(d)


def append_new_data(json_data):
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


def fetch_data():
    for page in range(0, 8):
        url = f'https://api.github.com/users/kerimdeveci/starred?per_page=100&page={page}'
        response = requests.get(url)
        js = response.json()
        values.extend(append_new_data(js))


fetch_data()
write_col(values)
