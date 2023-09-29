from models import db, Puppy, Toy, Owner, app

app.app_context().push()

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all(['rufus', 'fido'])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

hasnain = Owner('Hasnain', rufus.id)

toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all(['hasanin', toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())