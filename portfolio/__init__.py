from flask import Flask, render_template, abort

app = Flask(__name__)
projects = [
    {
        "name": "Coefficient Voting for Residential Properties",
        "thumb": "img/voting.png",
        "hero": "img/voting-hero.png",
        "categories": ["PHP", "JavaScript", "MySQL"],
        "slug": "coeff-voting",
        "prod": "https://votacionesasamblea.space/usuario/1",
    },
    {
        "name": "Movies Watch List",
        "thumb": "img/movies.png",
        "hero": "img/movies-hero.png",
        "categories": ["Python", "Mongo DB", "Jinja2"],
        "slug": "movies-watchlist",
        "prod": "https://movieswatchlist.onrender.com/",
    },
    {
        "name": "Habits Tracking",
        "thumb": "img/habit.png",
        "hero": "img/habit-hero.png",
        "categories": ["python","Flask", "Mongo DB"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-cando.onrender.com/",
    },
    
    {
        "name": "Microblog",
        "thumb": "img/blog.png",
        "hero": "img/blog-hero.png",
        "categories": ["Python", "Mongo DB"],
        "slug": "microblog",
         "prod": "https://microblog-70cy.onrender.com/",
    },
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html.j2", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html.j2")


@app.route("/contact")
def contact():
    return render_template("contact.html.j2")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html.j2", project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html.j2"), 404