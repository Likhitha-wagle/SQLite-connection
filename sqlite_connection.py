import sqlite3

conn=sqlite3.connect('test.db')
print("Done")

conn.execute('''create table if not exists Movie(
movie_name text not null,
actor text not null,
actress text not null,
director text not null,
year_of_release int not null );''')
print("table created")

conn.execute("insert into Movie(movie_name,actor,actress,director,year_of_release) values('yeh jawani hai deewani','RanbirKapoor','Deepika','Ayan',2013)")
conn.commit()

conn.execute("insert into Movie(movie_name,actor,actress,director,year_of_release) values('kirik party','Rakshith','Rashmika','Rishab',2016)")
conn.commit()
print("Inserted")

query=conn.execute("select movie_name,actor,actress,director,year_of_release from Movie")
print("Select query data")
for i in query:
    print(i)

query1=conn.execute("select movie_name,actor,actress,director,year_of_release from Movie where actor='Rakshith'")
for i in query1:
    print("Select query for given actor")
    print(i)
conn.close()