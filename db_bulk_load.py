"""
Bulk loads data into the database
"""

from faker import Factory
import psycopg2
gender = ['Male','Female']
ethnicity = ['White','Black','American Indian',
			 'Asian Indian','Chinese','Filipino',
			 'Other Asian','Japanese','Korean',
			 'Vietnamese','Native Hawaiian','Guamanian',
			 'Samoan','Other Pacific Islander','Other']
fake = Factory.create()

# Connect to an existing database
conn = psycopg2.connect("dbname=postgres user=postgres password=hi host=localhost")

# Open a cursor to perform database operations
cur = conn.cursor()

num_records = 1000
id_photo = open("test_img.jpg","rb").read()

def load_patients(num_records):
	insertions = 0
	while insertions < num_records:
		name = fake.name()
		village = fake.city()
		dob = fake.date(pattern="%Y-%m-%d")
		gend = fake.random_element(gender)
		ethn = fake.random_element(ethnicity)
		fp_hash = fake.md5(raw_output=False)
		cur.execute("INSERT INTO clinic.patients(name, village, dob, gender, ethnicity, fingerprint_hash, id_photo) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
												    (name,
												     village, 
												     dob,
												     gend,
												     ethn,
												     fp_hash,
												     psycopg2.Binary(id_photo)))
		conn.commit()
		insertions += 1
		print "Inserted %s into the database\n"%name

def load_nurses(num_records):
	insertions = 0
	while insertions < num_records:
		name = fake.name()
		village = fake.city()
		dob = fake.date(pattern="%Y-%m-%d")
		gend = fake.random_element(gender)
		fp_hash = fake.md5(raw_output=False)
		cur.execute("INSERT INTO clinic.nurses(name, village, dob, gender, fingerprint_hash, id_photo) VALUES (%s, %s, %s, %s, %s, %s)", 
												    (name,
												     village, 
												     dob,
												     gend,
												     fp_hash,
												     psycopg2.Binary(id_photo)))
		conn.commit()
		insertions += 1
		print "Inserted %s into the database\n"%name
# Close communication with the database

def load_doctors(num_records):
	insertions = 0
	while insertions < num_records:
		name = fake.name()
		doc_id = fake.md5(raw_output=False)
		cur.execute("INSERT INTO clinic.doctors(name, doc_id) VALUES (%s, %s)", 
												    (name,
												     doc_id,))
		conn.commit()
		insertions += 1
		print "Inserted %s into the database\n"%name		

load_doctors(num_records)
cur.close()
conn.close()
