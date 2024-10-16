#population
from app import db, app
from models import Content

#mock data to add

sample_content = [
    {"title": "Interstellar", "genre": "Sci-Fi", "description": "A team of explorers travel through a wormhole in space."},
    {"title": "The Dark Knight", "genre": "Action", "description": "Batman faces off against the Joker."},
    {"title": "Inception", "genre": "Sci-Fi", "description": "A thief who steals corporate secrets through dream-sharing."},
    {"title": "The Godfather", "genre": "Crime", "description": "The aging patriarch of a crime dynasty transfers control to his son."},
    {"title": "Pulp Fiction", "genre": "Crime", "description": "The lives of two mob hitmen, a boxer, and more intertwine."},
]

#add content
with app.app_context():
    for item in sample_content:
        new_content = Content(
            title=item["title"],
            genre=item["genre"],
            description=item["description"]
        )
        db.session.add(new_content)

    db.session.commit()
    print("Sample content added to the database!")