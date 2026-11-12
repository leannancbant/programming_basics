import db

db.create_tables()
db.add_testdata()

for m in db.get_modules():
    print(dict(m))