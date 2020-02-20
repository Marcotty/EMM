from flask import Flask, render_template, request
import inscription

app = Flask(__name__)

def Inscription():
    print('Inscription')
    inscription.Inscription_QR()
   
def ListDevices():
    inscription.AffListDevices()

def DeleteDevices():
    #inscription.DeleteAllDevices()
    inscription.DeleteDevices('enterprises/LC0430y1qm/devices/3b26e58aec3daf7f')
def ListPolitiques():
    inscription.AffListPolicies()

@app.route("/", methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Inscription') == 'Inscription':
            Inscription()
        elif request.form.get('Liste Devices') == 'Liste Devices':
            ListDevices()
        elif request.form.get('Liste Politiques') == 'Liste Politiques':
            ListPolitiques()
        elif request.form.get('Supprimer Devices') == 'Supprimer Devices':
            DeleteDevices()
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)