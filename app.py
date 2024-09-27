from flask import Flask,request,render_template,redirect
from models import db,Contact


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/home")

def home():
    contacts = Contact.query.all()
    return render_template("home.html",contacts=contacts)

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        new_contact = Contact(
            name = name,
            email = email,
            message = message
        )

        db.session.add(new_contact)
        db.session.commit()

        # return f"Name = {name} Email = {email} Message = {message}"
        return redirect("/home")
    
    return render_template("contact.html")

if __name__ == "__main__":

    app.run(debug=True)