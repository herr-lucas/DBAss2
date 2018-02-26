import urllib, json, random

students_url = "https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/students.json"
students_json = urllib.urlopen(students_url).read()
students = students_json.split("\n")[:-1]
students.pop()

student_objects = [json.loads(line) for line in students] 
student_names = map(lambda x: x["name"], student_objects)
with open("student_names.txt", "w+") as f:
	json.dump(student_names, f)

def generateOptional(generator):
	if random() > 0.5:
		return generator()
	else 
		return lambda x: None

def generate_email(name):
	return name.replace(" ", "_") + "@gmail.com"

def generate_credit_card_number():
	return 10**18 + random.random() * (10**19 - 10**18) - 1

def generate_billing_address():
	streets = ["Walkley", "Wolseley", "Gray Inn", "Peel", "Aylmer"]
	address = "%d %s" % (int(random.random()*5000), random.choice(streets))
	return address

def generate_insert_queries_visitors(names):
	with open("insert_queries_visitors.sql", "w+") as f:
		for name in names:
			email = generate_email(name)
			billing_adddress = generate_billing_address()
			credit_card_number = generate_credit_card_number()
			query = "INSERT INTO Visitor (name, email, billing_adddress, credit_card_number) %s %s %s %d\n" % (name, email, billing_adddress, credit_card_number)
			f.write(query)

def generate_insert_queries_tickets(visitors):
	def generate_dates():
		day = int(random()*30)
		month = random.choice["December", "January"]
		purchase_day = if month == "January" int(random()*day) else int(random()*30)
		return {"event_day": "January " + day + "th", "purchase_day": month + " " + purchase_day}

	def generate_price(ticket_type):
		return if ticket_type == "VIP" return 80 else 40

	def sample_visitor_email(visitors):
		return generate_email(visitors.choice())

	ticket_types = ['VIP', 'Regular']
	num_tickets = 500

	with open("insert_queries_tickets.sql", "w+") as f:
		for ticket_num in range(1, num_tickets):
			ticket_type = int(random.choice(ticket_type))
			dates = generateOptional(generate_dates)()
			price = generateOptional(generate_price)(ticket_type)
			visitor_email = generateOptional(sample_visitor_email)(visitors)
			query = """INSERT INTO Ticket (TicketNO, Date_of_entry, Ticket_type, Date_of_purchase, Price, 
					Visitor_email) %d %s %s %s %d %s""" % (ticket_num, dates[event_day], 
					ticket_type, dates[purchase_day] price, visitor_email)


generate_insert_queries_visitors(student_names)
generate_insert_queries_tickets(student_names)