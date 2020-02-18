from flask import Flask, render_template, request
import inscription

app = Flask(__name__)

def Inscription():
    print('Inscription')
    inscription.Inscription_QR()
    
@app.route("/", methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Inscription') == 'Inscription':
            Inscription()
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)