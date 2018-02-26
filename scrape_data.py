import urllib, json, random

students_url = "https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/students.json"
students_json = urllib.urlopen(students_url).read()
students = students_json.split("\n")[:-1]
students.pop()

student_objects = [json.loads(line) for line in students] 
student_names = map(lambda x: x["name"], student_objects)
with open("student_names.txt", "w+") as f:
	json.dump(student_names, f)

def generate_email(name):
	return name + "@gmail.com"

def generate_credit_card_number():
	return random(10**18, 10**19-1)

def generate_billing_address
	streets = ["Walkey", "Wolseley", "Gray Inn", "Peel", "Aylmer"]
	address = random(5000) + " " + random.choice(streets)
	return address

def generate_insert_queries(names):
	with fopen("insert_queries", "w+") as f:
		for name in names:
			email = generate_email(name)
			billing_adddress = generate_billing_address()
			credit_card_number = generate_credit_card_number()
			query = "INSERT INTO Visitor (name, email, billing_adddress, credit_card_number) %s %s %s %d" % (name, email, billing_adddress, credit_card_number)
			f.write(query)