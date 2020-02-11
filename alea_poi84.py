import psycopg2 
from faker import Faker 
fake = Faker() 
conn = psycopg2.connect(database="lizmap", user="postgres", password="postgres", host="10.13.34.161", port="5432") 
print "Ouverture de la BDD : OK" 
cur = conn.cursor() 
list = ["Trip", "Advisor", "Google+", "Booking", "Locaux"] 
for i in range (7175):
    gestionnaire = fake.name()
    note_public=fake.random_int(1,10)
    note_critique=fake.random_int(1,10)
    type_critique=fake.random_element(list)
    occupation = fake.random_int(1,50) 
    cur.execute("INSERT INTO point_interet_caracteristic (gestionnaire, note_public, note_critique, type_critique, occupation) VALUES (%s, %s, %s, %s, %s)", (gestionnaire, note_public, note_critique, type_critique, occupation));


conn.commit() 
print "Remplissage OK";
conn.close()
