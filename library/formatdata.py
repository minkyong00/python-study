# formatdata.py
# 포맷데이터

# CSV
import csv

# csvdata.csv파일에 ,를 구분자로 하고 홑따옴표로 문자를 구별하는 writer를 획득해서
# 두 줄의 데이터를 출력
with open('csvdata.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',', quotechar="'")
    writer.writerow(['홍길동', '30', '서울']) 
    writer.writerow(['강감찬', '40', '부산']) 

# csvdata.csv 파일의 내용을 화면에 출력
with open('csvdata.csv', mode='r', encoding='utf-8') as f:
    print(f.read())

# XML
import xml.etree.ElementTree as ET

persons = ET.Element('persons')

person = ET.SubElement(persons, 'person')
name = ET.SubElement(person, 'name')
name.text = '홍길동'
age = ET.SubElement(person, 'age')
age.text = '20'

person = ET.SubElement(persons, 'person')
name = ET.SubElement(person, 'name')
name.text = '강감찬'
age = ET.SubElement(person, 'age')
age.text = '30'

xmlstr = ET.tostring(persons, encoding='utf-8').decode()
print(xmlstr)

with open('xmldata.xml', mode='w', encoding='utf-8') as f:
    f.write(xmlstr)

with open('xmldata.xml', mode='r', encoding='utf-8') as f:
    print(f.read())

# JSON
import json

# 딕셔너리
jsonDic = {
    "name":'홍길동',
    "age":'20'
}

with open('jsondata.json', mode='w', encoding='utf-8') as f:
    json.dump(jsonDic, f)

with open('jsondata.json', mode='r', encoding='utf-8') as f:
    print(json.load(f))














