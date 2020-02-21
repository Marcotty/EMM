from flask import Flask, render_template, request
import tools

app = Flask(__name__)

def Inscription():
    print('Inscription')
    tools.Inscription_QR()
   
def ListDevices():
    tools.AffListDevices()

def DeleteDevices():
    #inscription.DeleteAllDevices()
    device = 'enterprises/LC0430y1qm/devices/3d0336d4fe96b3a9'
    tools.DeleteDevices(device)
def ListPolitiques():
    tools.AffListPolicies()

def UpdatePolitique():
    politique = '/policies/policy1'
    tools.UpdatePolitique(politique)

def test():
    tools.UpdatePolitique()
    
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
    pols = tools.ListPolicies()
    #for pol in pols:
        #pols_names += pol['name']
    return render_template("inscription.html")#, politiques =pols_name)
@app.route("/devices")
def devices():
    return render_template("devices.html")
@app.route("/politiques")
def politiques():
    pols = tools.ListPolicies()
    #for pol in pols:
     #   pol1_name = pol['name']
    return render_template("politiques.html")
    
@app.route("/entreprise")
def entreprise():
    return render_template("entreprise.html")
    
@app.route('/resultats', methods = ['POST'])
def resultats():
    result = request.form
    pol = result['politique']
    #comment ajouter un nombre incertains de paramètres ??
    return render_template("resultats.html", politique = pol, qr = tools.getQRLien())
    
if __name__ == "__main__":
    app.run(debug=True)