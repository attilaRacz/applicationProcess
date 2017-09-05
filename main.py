from flask import Flask, render_template, request, redirect
import queries
app = Flask(__name__)

@app.route("/")
def index_page():
    front_page = True
    return render_template("list.html", front_page=front_page)


@app.route("/mentors")
def mentors():
    return queries.mentors_and_schools()


@app.route("/all-school")
def all_school():
    return queries.all_school()


@app.route("/mentors-by-country")
def mentors_by_country():
    return queries.mentors_by_country()


@app.route("/contacts")
def contacts():
    return queries.contacts()


@app.route("/applicants")
def applicants():
    return queries.applicants()


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    return queries.applicants_and_mentors()


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
