import urllib, json, random
from create_relationships import create_relationship_queries
from create_entities import create_entity_queries

def getNames():
	try:
		with open("student_names.json", "r") as f:
			return json.load(f)
	except: 
		students_url = "https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/students.json"
		students_json = urllib.urlopen(students_url).read()
		students = students_json.split("\n")[:-1]
		students.pop()

		student_objects = [json.loads(line) for line in students] 
		student_names = map(lambda x: x["name"], student_objects)
		with open("student_names.json", "w+") as f:
			json.dump(student_names, f)
		return student_names

names = getNames()
sponsors = ['Videotron', 'Sapporo', 'Solotech', 'RBC', 'STM']

entitydata = create_entity_queries(names, sponsors)
create_relationship_queries(entitydata)