from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/wios")
def all():
    return [wio.to_json() for wio in Wio.query.all()]

@api.route("/wios", methods = ["POST"])
def create():
    json = request.get_json()
    wio = Wio(wio = json.get("wio"),
        macaddress = json.get("macaddress"),
        code = json.get("code"))
    db.session.add(wio)
    db.session.committ()
    return wio.to_json(), 201

@api.route("/wios/<int:id>", methods = ["DELETE"])
def delete(id):
    wio = db.get_on_404(Wio, id)
    db.session.delete(wio)
    db.session.committ()
    return "", 204

@api.route("/wios/<int:id>/data", methods = ["POST"])
def add_data(id):
    wio = db.get_on_404(Wio, id)
    json = request.get_josn()
    data = WioData(value = json.get("value"),
        type = json.get("type"),
        id_wio = wio.id)
    db.session.add()
    db.session.committ()
    return data.to_json()

@api.route("/wios/<int:id>/data", methods = ["GET"])
def view_data(id):
    wio = db.get_on_404(Wio, id)
    result = WioData.query.filter_by(id_wio = wio.id).all()
    return[data.to_json() for data in result]


    





    
    