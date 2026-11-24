from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    messages = db.relationship('Message', backref='author')

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Author: Name = {self.name}, Address = {self.address}, Messages = {self.messages}"

    def __repr__(self):
        return str(self)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

    def __init__(self, title, content):
        if len(title) < 1:
            raise ValueError("Title is required!")
        if len(title) > 20:
            raise ValueError("Title is too long!")
        if title[0] == 'X':
            raise ValueError("Title cannot start with X!")
        self.title = title
        if len(content) < 1:
            raise ValueError("Content is required!")
        if len(content) > 100:
            raise ValueError("Content is too long!")
        self.content = content

    def __str__(self):
        a = Author.query.get(self.author_id)
        return f"Message: Title = {self.title}, Content = {self.content}, Author = {a.name}"

    def __repr__(self):
        return str(self)

