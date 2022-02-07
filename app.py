
from flask import Flask,request,jsonify
from datetime import datetime 
t=datetime.now()
mad_Thing={}
hinokami=[]
kagura=0
app=Flask(__name__)


#Profile
@app.route("/profile",methods=["GET"])
def home():
    return jsonify(mad_Thing)

@app.route("/profile",methods=["POST"])
def profPost():
    t=datetime.now()
    username=request.json["username"]
    role=request.json["role"]
    color=request.json["color"]
    user_object={
        "data":{
            "username":username,
            "color":color,
            "role":role,
            "last_updated":t
        }
    }
    global mad_Thing
    mad_Thing=user_object

    return jsonify(mad_Thing)

@app.route("/profile",methods=["PATCH"])
def profPatch():
    t=datetime.now()
    if 'username' in request.json:
        mad_Thing["data"]["username"]=request.json["username"]
        mad_Thing["data"]["last_updated"]=t
    
    if 'role' in request.json:
        mad_Thing["data"]["role"]=request.json["role"]
        mad_Thing["data"]["last_updated"]=t

    if 'color' in request.json:
        mad_Thing["data"]["color"]=request.json["color"]
        mad_Thing["data"]["last_updated"]=t
    
    return jsonify(mad_Thing)


#DATA-------------------------------------
@app.route("/data",methods=["GET"])
def dataGET():
    return jsonify(hinokami)

@app.route("/data",methods=["POST"])
def dataPost():
    l=request.json["location"]
    la=request.json["lat"]
    lo=request.json["long"]
    pf=request.json["percentage_full"]
    global kagura
    kagura+=1

    moon_object={
        "id":kagura,
        "location":l,
        "lat":la,
        "long":lo,
        "percentage_full":pf
    }

    hinokami.append(moon_object)
    print(kagura)
    return jsonify(moon_object)

@app.route("/data/<int:id>",methods=["DELETE"])
def dataDelete(id):
    
    for u in hinokami:
        if u["id"]==id:
            hinokami.remove(u)
    deel={
        "Sucess":True
    }
    return deel
     
@app.route("/data/<int:id>",methods=["PATCH"])
def dataPatch(id):
    for u in hinokami:
        if u["id"]==id:
            if 'location' in request.json:
                u["location"]=request.json["location"]
            if 'lat' in request.json:
                u["lat"]=request.json["lat"]
            if 'long' in request.json:
                u["long"]=request.json["long"]
            if 'percentage_full' in request.json:
                u["percentage_full"]=request.json["percentage_full"]
    return jsonify(u)
     

if __name__ =='__main__':
    app.run(
        debug=True,
        port=3000,
        host="0.0.0.0"
    )


