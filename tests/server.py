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
    device = 'enterprises/LC0430y1qm/devices/36c701ca905b1f9b'
    inscription.DeleteDevices(device)
def ListPolitiques():
    inscription.AffListPolicies()

def UpdatePolitique():
    politique = '/policies/policy1'
    inscription.UpdatePolitique(politique)

def test():
    inscription.UpdatePolitique()
    
@app.route("/", methods=['GET', 'POST'])
def home():
    print('Requete : ' + request.method)
    if request.method == 'POST':
        if request.form.get('Inscription') == 'Inscription':
            Inscription()
        elif request.form.get('Liste Devices') == 'Liste Devices':
            ListDevices()
        elif request.form.get('Liste Politiques') == 'Liste Politiques':
            ListPolitiques()
        elif request.form.get('Supprimer Devices') == 'Supprimer Devices':
            DeleteDevices()
        elif request.form.get('Update Politique') == 'Update Politique':
            UpdatePolitique()
        elif request.form.get('test') == 'test':
            test()
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/inscription")
def inscription():
    return render_template("inscription.html")
@app.route("/devices")
def devices():
    return render_template("devices.html")
@app.route("/politiques")
def politiques():
    return render_template("politiques.html")
@app.route("/entreprise")
def entreprise():
    return render_template("entreprise.html")
    
if __name__ == "__main__":
    app.run(debug=True)