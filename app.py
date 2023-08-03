"""adopt application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from models import db, connect_db, Pet
from forms import CreateAddForm, EditPetForm


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption_db"
app.app_context().push()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "jongainza"

# toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()


@app.route("/")
def show_pets():
    pets = Pet.query.all()
    return render_template("list.html", pets=pets)


@app.route("/add_pet")
def show_add_pet_form():
    "Shows form to create new user"
    return render_template("add_form.html")


@app.route("/add", methods=["GET", "POST"])
def create_add_form():
    form = CreateAddForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo=photo, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"Created a new pet: is a {species} and the name is {name}")
        return redirect("/")
    else:
        return render_template("add_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} updated")
        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
