import random

def generate_insert_queries_visits(visitors_and_events):
	with open("insert_queries_visitor_relationship.sql", "w+") as f:
		for v in visitors_and_events:
			email = v["email"]
			eventdate = v["date"]
			query = "INSERT INTO Visits (Visitor_email, EventDate) VALUES(\'%s\', \'%s\');\n" % (email, eventdate)
			f.write(query)

def generate_insert_queries_performs(performers_and_events):
	with open("insert_queries_performer_relationship.sql", "w+") as f:
		for (email, eventdate) in performers_and_events:
			query = "INSERT INTO Performs (Performer_email, EventDate) VALUES(\'%s\', \'%s\');\n" % (email, eventdate)
			f.write(query)

def generate_insert_queries_work(staffnames):
	workday = 1
	with open("insert_queries_work_relationship.sql", "w+") as f:
		for name in staffnames:
			idquery = "(SELECT id from STAFF WHERE name=\'%s\')" % name
			day = "January %d, 2018" % workday
			query = "INSERT INTO Work (StaffID, EventDate) VALUES((%s), \'%s\');\n" % (idquery, day)
			workday += 1
			f.write(query)

def generate_insert_queries_borrow(equipnames):
	with open("insert_queries_borrow_relationship.sql", "w+") as f:
		for eqName in equipnames:
			date = "January %d, 2018" % random.choice([1,2,3])
			idquery = "(SELECT id from Equipment WHERE type=\'%s\')" % eqName
			qty = 1
			query = "INSERT INTO Borrow (EquipmentID, EventDate, Quantity) VALUES(%s, \'%s\', %d);\n" % (idquery, date, qty)
			f.write(query)

def generate_insert_queries_sells(booths_and_merch_names):
	with open("insert_queries_sells_relationship.sql", "w+") as f:
		booths_and_merch_list = []
		for k in booths_and_merch_names:
			for v in booths_and_merch_names[k]:
				booths_and_merch_list.append((k, v))
		for (booth, merch) in booths_and_merch_list:
			idquery = "(SELECT id from Merchandise WHERE name=\'%s\')" % merch
			qty = random.choice(range(1, 10))
			query = "INSERT INTO Sells (Booth_name, MerchandiseID, quantity) VALUES(\'%s\', %s, %d);\n" % (booth, idquery, qty)
			f.write(query)

def create_relationship_queries(entity_data):
	generate_insert_queries_visits(entity_data["visitor_tickets"])
	generate_insert_queries_performs(entity_data["performers_and_events"])
	generate_insert_queries_work(entity_data["staff_names"])
	generate_insert_queries_borrow(entity_data["equipment_names"])
	generate_insert_queries_sells(entity_data["booths_and_merch_names"])