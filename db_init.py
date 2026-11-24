from app import Author, Message, db, app
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
    a = Author("Alice","Australia")
    b = Author("Bob", "Belgium")
    c = Author("Charlie", "Canada")
    db.session.add(a)
    db.session.add(b)
    db.session.add(c)
    db.session.commit() # Commit now to get author IDs
    m1 = Message("Hello","Hello, world!")
    m1.author_id = a.id
    m2 = Message("Yo", "Well, hello there, IS2208")
    m2.author_id = a.id
    m3 = Message("My favourite food", "Is there anything better than Belgian waffles?")
    m3.author_id = b.id
    db.session.add(m1)
    db.session.add(m2)
    db.session.add(m3)
    db.session.commit()