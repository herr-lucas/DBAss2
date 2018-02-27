import random

def generateOptional(generator):
	if random.random() > 0.5:
		return generator
	else:
		return lambda *x: "NULL"

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
		day = int(random.random()*30)
		month = random.choice(["December", "January"])
		purchase_day = int(random.random()*day) if month == "January" else int(random.random()*30)
		return {"event_day": "January %sth" % day, "purchase_day": month + " %sth" % purchase_day}

	def generate_price(ticket_type):
		return str(80 if ticket_type == "VIP" else 40)

	def sample_visitor_email(visitors):
		return generate_email(random.choice(visitors))

	ticket_types = ['VIP', 'Regular']
	num_tickets = 500

	visitors_and_tickets = []
	with open("insert_queries_tickets.sql", "w+") as f:
		for ticket_num in range(1, num_tickets):
			ticket_type = random.choice(ticket_types)
			dates = generateOptional(generate_dates)()
			event_day = dates["event_day"] if dates != "NULL" else "NULL"
			purchase_day = dates["purchase_day"] if dates != "NULL" else "NULL"
			price = generateOptional(generate_price)(ticket_type)
			visitor_email = generateOptional(sample_visitor_email)(visitors)
			query = """INSERT INTO Ticket (TicketNO, Date_of_entry, Ticket_type, Date_of_purchase, Price, 
				Visitor_email) %d %s %s %s %s %s\n""" % (
				ticket_num, event_day, ticket_type, purchase_day, price, visitor_email
			)
			f.write(query)
			visitors_and_tickets.append({"email": visitor_email, "date": event_day})

	return visitors_and_tickets

def generate_insert_queries_staff(student_names):
	num_staff = 50
	staff_roles = ["cleaner", "sales", "security", "ticketing", "food"]
	with open("insert_queries_staff.sql", "w+") as f:
		for name in student_names[-num_staff:]:
			email = generate_email(name)
			role = random.choice(staff_roles)
			query = "INSERT INTO Staff (Name, Email, Role) %s %s %s\n" % (name, email, role)
			f.write(query)

def generate_insert_queries_events():
	events_and_dates = [	
		{"date": "January 5th", "name": "Kaytranada"}, 
		{"date": "January 6th", "name": "Bonobo"}, 
		{"date": "January 7th", "name": "Petit Biscuit"}
	]
	with open("insert_queries_events.sql", "w+") as f:
		for e in events_and_dates:
			date = e["date"]
			name = e["name"]
			query = "INSERT INTO Event (Date, Name) %s %s\n" % (date, name)
			f.write(query)

def generate_insert_queries_sponsors(sponsors):

	def generate_amount():
		return random.choice([0, 1000, 5000, 10000])

	with open("insert_queries_sponsors.sql", "w+") as f:
		for sponsor in sponsors:
			email = generate_email(sponsor)
			query = "INSERT INTO Sponsor (email, sponsor, generate_amount) %s %s %s\n" % (email, sponsor, generate_amount())
			f.write(query)

def generate_insert_queries_equipment():
	eqs = [('speakers', 10000, 2), ('screens', 20000, 3)]
	equipment = []
	with open("insert_queries_equipment.sql", "w+") as f:
		for (name, price, qty) in eqs:
			query = "INSERT INTO Equipment (name, price, quantity) %s %d %d\n" % (name, price, qty)
			f.write(query)
			equipment.append(name)
	return equipment

def generate_insert_queries_booth(sponsors):
	types = [('hats', 'non-food'), ('games', 'non-food'), ('heated area', 'non-food'),('snacks','food'), ('drinks', 'food')]
	locations = [a + str(b) + str(c) for a in ['A', 'B', 'C'] for b in range(1,4) for c in range(1, 4)]
	with open("insert_queries_booths.sql", "w+") as f:
		for (i, (name, typ)) in map(lambda x: (types.index(x), x), types):
			query = "INSERT INTO Booth (Name, Location, Type) %s %s %s\n"  % (name, locations[i], typ)
			f.write(query)

def generate_insert_queries_merchandise():
	merch = {
	  "hats": ["red hat", "orange hat", "blue hat", "baseball cap"],
	  "games": ["pinball", "cards", "snowball toss"],
	  "heated area": ["souveniers"],
	  "snacks": ["ham sandwich", "turkey sandwich", "crackers and cheese"],
	  "drinks": ["voda", "rum", "jack daniels", "orange juice", "water"]
	}
	sponsor = "Videotron"
	sponsor_email = generate_email(sponsor)
	with open("insert_queries_merchandise.sql", "w+") as f:
		for merchitems in merch.values():
			for name in merchitems:
				stock = random.choice([10, 50]) 
				price = random.choice([3, 5, 10, 20, 30])	
				query = "INSERT INTO Merchandise (Name, Stock, Price_per_unit, sponsor_email) %s %d %s% s\n" % (name, stock, price, sponsor_email)
				f.write(query)

def generate_insert_queries_performers():
	performances = [
		{"day": "January 1st", "performers": ["Hack", "Slack", "Kaytranada"]}, 
		{"day": "January 2nd", "performers": ["Slice", "Dice", "Bonobo"]}, 
		{"day": "January 3rd", "performers": ["Mash", "Petit Biscuit"]}
	]
	default_genre = "Electronic"
	emails_and_dates = []
	with open("insert_queries_performers.sql", "w+") as f:
		for p in performances:
			day = p["day"]
			performers = p["performers"]
			for performer in performers:
				email = generate_email(performer)
				name = performer
				genre = default_genre
				pay = random.choice([500, 1000, 10000, 50000])
				intro = "insert intro here"
				query = "INSERT INTO Performer (Email, Name, Genre, Pay, Intro) %s %s %s %d %s\n" % (email, name, genre, pay, intro)
				f.write(query)
			emails_and_dates.append((email, day))
	return emails_and_dates

def create_entity_queries(names, sponsors):
	visitor_names = names[len(names)/5:]
	staff_names = names[:len(names)/5]
	generate_insert_queries_visitors(visitor_names)
	visitors_and_tickets = generate_insert_queries_tickets(visitor_names)
	generate_insert_queries_staff(staff_names)
	generate_insert_queries_events()
	performer_emails_and_dates = generate_insert_queries_performers()
	generate_insert_queries_sponsors(sponsors)
	eqIDs = generate_insert_queries_equipment()
	generate_insert_queries_booth(sponsors)
	generate_insert_queries_merchandise()
	return {
		"visitor_tickets": visitors_and_tickets,
		"performers_and_events": performer_emails_and_dates,
		"equipment_ids": eqIDs#,
		#"booths_and_merch": booths_and_merch
	}