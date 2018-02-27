import random

def generate_insert_queries_visits(visitors, eventdates):
	with open("insert_queries_visitors.sql") as f:
		for (v, events) in visitors:
			for e in events:
				email = generate_email(v)
				query = "INSERT INTO Visits (Visitor_email, EventDate) %s %s\n" % (email, e)
				f.write(query)

def generate_insert_queries_performs(performers, eventdates):
	with open("insert_queries_performers.sql") as f:
		for (p, events) in performers:
			for e in events:
				email = generate_email(p)
				query = "INSERT INTO Performs (Performer_email, EventDate) %s %s\n" % (email, e)
				f.write(query)

def generate_insert_queries_work(staffids, eventdates):
	workday = 1
	with open("insert_queries_workers.sql") as f:
		for memberId in staffids:
			day = "January %dth" % workday
			query = "INSERT INTO Work (StaffID, EventDate) %s %s\n" % (memberId, day)
			workday += 1
			f.write(query)

def generate_insert_queries_borrow(equipids, eventdate):
	with open("insert_queries_borrow.sql") as f:
		for (eqId, date) in equipids:
			qty = 1
			query = "INSERT INTO Borrow (EquipmentID, EventDate, Quantity) %s %s\n" % (eqId, date, qty)
			f.write(query)

def generate_insert_queries_sells(booths, merchandise):
	with open("insert_queries_sells.sql") as f:
		for (booth, merch) in booths:
			qty = 12
			query = "INSERT INTO Sells (Booth_name, MerchandiseID, quantity) %s %s\n" % (booth, merch, qty)
			f.write(query)