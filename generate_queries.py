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
merch = {
	  "hats": ["red hat", "orange hat", "blue hat", "baseball cap"],
	  "games": ["pinball", "cards", "snowball toss"],
	  "heated area": ["souveniers"],
	  "snacks": ["ham sandwich", "turkey sandwich", "crackers and cheese"],
	  "drinks": ["voda", "rum", "jack daniels", "orange juice", "water"]
	}

entitydata = create_entity_queries(names, sponsors, merch)
create_relationship_queries(entitydata)