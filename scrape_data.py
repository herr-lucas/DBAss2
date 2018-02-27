import urllib, json, random
import create_relationships, create_entities

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

events = [{"January 5th"}, {"January 6th"}, {"January 7th"}]
sponsors = ['Videotron', 'Sapporo', 'Solotech', 'RBC', 'STM']

create_entity_queries()
create_relationship_queries()