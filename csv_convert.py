import csv
import json
from pathlib import Path

# values = [["key", "value", "ar", "zh", "ja",
#            "pt", "ru", "es", "th", "tr", "vi", "in"]]


def generate_columns_for_csv(json_data):
    values = []
    for item in json_data:
        fl = []
        fl.append(item['name'].replace(' ', '_').lower())
        fl.append(item['name'])
        fl.append(item['names']['ar'])
        fl.append(item['names']['zh'])
        fl.append(item['names']['ja'])
        fl.append(item['names']['pt'])
        fl.append(item['names']['ru'])
        fl.append(item['names']['es'])
        fl.append(item['names']['th'])
        fl.append(item['names']['tr'])
        fl.append(item['names']['vi'])
        fl.append(item['names']['in'])
        values.append(fl)
    return values


def get_json_data():
    data = Path(
        '/Users/kerimdeveci/Desktop/Ringtones/r_contents.json').read_text()
    categories = json.loads(data)
    print(categories)
    return categories


def get_csv():
    final_rows = []
    with open('translate2.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            final_rows.append(row)

    return final_rows


def write_col(data):

    outputFileName = 'translate3.csv'
    with open(outputFileName, 'w') as file:
        writer = csv.writer(file)
        for d in data:
            writer.writerow(d)


getted_rows = get_csv()
getted_data_from_json = get_json_data()
genereated_colums = generate_columns_for_csv(getted_data_from_json)
final_rows = getted_rows + genereated_colums
print(final_rows)
write_col(final_rows)
