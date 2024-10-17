#population
from app import db, app
from models import Content

#mock data to add

sample_content = [
    {"title": "Interstellar", "genre": "Sci-Fi", "description": "A team of explorers travel through a wormhole in space.", "poster_url": "Interstellar.jpg"},
    {"title": "The Dark Knight", "genre": "Action", "description": "Batman faces off against the Joker.", "poster_url": "The_Dark_Knight.jpg"},
    {"title": "Inception", "genre": "Sci-Fi", "description": "A thief who steals corporate secrets through dream-sharing.", "poster_url": "Inception.jpg"},
    {"title": "The Godfather", "genre": "Crime", "description": "The aging patriarch of a crime dynasty transfers control to his son.", "poster_url": "The_Godfather.jpg"},
    {"title": "Pulp Fiction", "genre": "Crime", "description": "The lives of two mob hitmen, a boxer, and more intertwine.", "poster_url": "Pulp_Fiction.jpg"},
    {"title": "Eternal Sunshine of the Spotless Mind", "genre":"Dark Romance", "description": "Two lovers try to forget each other...agin", "poster_url": "Eternal_Sunshine_of_the_Spotless_Mind.jpg"}
]

#add content
with app.app_context():
    for item in sample_content:
        new_content = Content(
            title=item["title"],
            genre=item["genre"],
            description=item["description"],
            poster_url=item["poster_url"]
        )
        db.session.add(new_content)

    db.session.commit()
    print("Sample content added to the database!")