from backend import db
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    type1 = db.Column(db.String, nullable = False)
    type2 = db.Column(db.String)
    legendary = db.Column(db.Boolean, nullable = False)
    attack = db.Column(db.Integer , nullable = False)
    defense = db.Column(db.Integer , nullable = False)
    speed = db.Column(db.Integer, nullable = False)
    healthPoints = db.Column(db.Integer, nullable = False)
    spattack = db.Column(db.Integer , nullable = False)
    spdefense = db.Column(db.Integer , nullable = False)
    