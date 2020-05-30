import requests
import csv
# import json

# descriptions = []


# def get_json():
#     with open('raw.json', 'r') as file:
#         return json.load(file)


# def create_stars(response):
#     for item in response.json():
#         decs = item['description']
#         if decs is not None:
#             descriptions.append(decs)


def write_col(data):
    with open('data2.csv', 'w') as file:
        writer = csv.writer(file)
        for d in data:
            writer.writerow(d)


# def write_header(data):
#     with open('data2.csv', 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(data)


# values = [['name2', 'description2', 'url2', 'star_count2'],
#           ['name2', 'description2', 'url2', 'star_count2']]
values = [['name', 'html_url', 'description', 'created_at',
           'updated_at', 'stargazers_count', 'language']]
# print(descriptions)
# write_header(header)
# write_col(values)


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
        # create_stars(response)
        # append_new_data


# j_data = get_json()
# values.extend(append_new_data(j_data))
# print(values)
fetch_data()
write_col(values)
