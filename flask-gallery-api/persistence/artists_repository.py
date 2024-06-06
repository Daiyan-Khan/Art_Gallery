from models.artist import Artist
from utils.database import db
from persistence.IArtistDataAccess import IArtistDataAccess

class ArtistRepository(IArtistDataAccess):
    def create_artist(self, artist: Artist) -> None:
        db.session.add(artist)
        db.session.commit()

    def get_all_artists(self):
        return Artist.query.all()

    def get_artist_by_id(self, artist_id: int) -> Artist:
        return Artist.query.get(artist_id)

    def update_artist(self, artist: Artist) -> None:
        db.session.commit()

    def delete_artist(self, artist_id: int) -> bool:
        artist = Artist.query.get(artist_id)
        if artist:
            db.session.delete(artist)
            db.session.commit()
            return True
        return False
