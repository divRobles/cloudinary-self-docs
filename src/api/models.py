from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(50), unique=True, nullable=False)
    nacimiento = db.Column(db.String(8), nullable=False)
    foto = db.Column(db.String(50), nullable=False)
    descipcion = db.Column(db.String(3000), nullable=False)


    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "dni": self.dni,
            "nacimiento": self.nacimiento,
            "foto": self.foto,
            "descripcion": self.descripcion,

            # do not serialize the password, its a security breach
        }







class Pic (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, nullable=False)
    # name = db.Column(db.Text, nullable=False)
    # minetype = db.Column(db.Text, nullable=False)
    


    def __repr__(self):
        return '<Pic %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "img": self.img,
            # "name": self.name,
            # "minetype" : self.minetype
            # "minetype": self.minetype
        }



