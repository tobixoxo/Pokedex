from flask import jsonify, request, render_template
from backend import app,db , models


@app.route("/")
def index():
    return "<a href = 'https://www.wikipedia.org/'>click</a>"

#@app.route("/api/pokemon/<int:num>")   #when we have to a number in the url as an input
@app.route("/api/allpokemon")
def page1():
    pokemon = [{ 
        "id" : x.id,
        "name" : x.name,
        "type1" : x.type1,
        "type2" : x.type2,
        "legendary" : x.legendary,
        "attack" : x.attack,
        "speed" : x.speed,
        "healthPoints" : x.healthPoints,
        "spattack" : x.spattack,
        "spdefense" : x.spdefense
    } for x in models.Pokemon.query.all()]
    return jsonify(pokemon)

@app.route("/addpokemon",methods = ["GET","POST"])
def addpkmn():
    if request.method == "POST":
        newpkmn = request.get_json(force= True)
        print(newpkmn)
        db.session.add(models.Pokemon(**newpkmn))
        db.session.commit()
        return "posted!"

    elif request.method == "GET":
        return "add form here!"

@app.route("/api/pokemon/<int:num>")
def individualpkmn_api(num):
    x = models.Pokemon.query.filter_by(id = num).first()
    pokemon = { 
        "id" : x.id,
        "name" : x.name,
        "type1" : x.type1,
        "type2" : x.type2,
        "legendary" : x.legendary,
        "attack" : x.attack,
        "speed" : x.speed,
        "healthPoints" : x.healthPoints,
        "spattack" : x.spattack,
        "spdefense" : x.spdefense
    } 
    return jsonify(pokemon)

@app.route("/pokemon/<int:num>")
def individualpkmn(num):
    x = models.Pokemon.query.filter_by(id = num).first()
    pokemon = { 
        "id" : x.id,
        "name" : x.name,
        "type1" : x.type1,
        "type2" : x.type2,
        "legendary" : x.legendary,
        "attack" : x.attack,
        "speed" : x.speed,
        "healthPoints" : x.healthPoints,
        "spattack" : x.spattack,
        "spdefense" : x.spdefense
    } 
    return render_template("pokemon.html",**pokemon)