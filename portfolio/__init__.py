from flask import Flask, render_template, abort
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)    

    projects = [
    {
        "name": "Coefficient Voting for Residential Properties",
        "thumb": "img/voting.png",
        "hero": "img/voting-hero.jpg",
        "categories": ["PHP", "JavaScript", "MySQL"],
        "slug": "coeff-voting",
        "prod": "https://votacionesasamblea.space/usuario/1",
        #"prod": "https://nifty-water-88162.pktriot.net/Encuesta/usuario/38ab678e915f4f15fdc015329648f23c",
    },
    {
        "name": "Movies Watch List",
        "thumb": "img/movies.png",
        "hero": "img/movies-hero.jpg",
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
        "hero": "img/blog-hero.jpg",
        "categories": ["Python", "Mongo DB"],
        "slug": "microblog",
         "prod": "https://microblog-70cy.onrender.com/",
    },]

    slug_to_project = {project["slug"]: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)


    @app.route("/about")
    def about():
        return render_template("about.html")


    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404
        
    return app

