import csv
import json
import yaml
import xml.etree.ElementTree as ET
# from lxml import etree

# CSV
csv.register_dialect('my_dialect', delimiter=',', quoting=csv.QUOTE_ALL)

with open('csv_file_open.csv', 'r', encoding='utf-8', newline='') as csv_file: 
  reader = csv.reader(csv_file)
  data = [row for row in reader]

with open('csv_file_write.csv', 'w', encoding='utf-8', newline='') as csvfile:
  writer = csv.writer(csvfile, dialect='my_dialect')
  writer.writerows(data)

# JSON
with open('json_file_open.json', 'r') as json_file:
  json_file_ = json.load(json_file)
  count = 0
  title_list = []
  for title in json_file_['articles']:
    title_list.append(title['title'])
    count += 1
  print(f"В файле {count} статей. Вот их список {title_list}")

with open('json_file_write.json', 'w', newline='') as json_file:
  json.dump(title_list, json_file, indent=2, ensure_ascii=False)
  json_file_ = json.dumps(title_list, indent=2, ensure_ascii=False)
  print(json_file_)

# YAML
with open('yaml_file_read.yml', 'r', encoding='utf-8') as yaml_file:
  yaml_file_ = yaml.load_all(yaml_file, Loader=yaml.FullLoader)
  data_yaml = [file for file in yaml_file_ if file is not None]
  print(data_yaml)

with open('yaml_file_write.yml', 'w', encoding='utf-8') as yaml_file:
  yaml.dump_all(data_yaml, yaml_file, allow_unicode=True, default_flow_style=False)
  yaml.dump_all(title_list, yaml_file, allow_unicode=True)

d = {"hello": "python", "goodbye": 'java'}
with open('for_LeadER_TV.json', 'w', encoding='utf-8') as json_file:
    json.dump(d, json_file)
    result = json.dumps(d)
    print(type(result), result)

# XML
tree = ET.parse('xml_file_read.xml')
root = tree.getroot()

for book in root:
  print(book.find('title').text)
  print(book.find('author').text)
  print(book.find('year').text)
  print()


# Парсим XML-файл
# tree = etree.parse('rss_habr.xml')
tree = ET.parse('rss_habr.xml')
root = tree.getroot()


# Находим все элементы `item` в корневом элементе
items = root.findall('channel/item')

# Итерируемся по элементам `item` и извлекаем заголовки
for item in items:
    title = item.find('title').text
    link = item.find('link').text
    print(title,'\n', link)

print(root.attrib)