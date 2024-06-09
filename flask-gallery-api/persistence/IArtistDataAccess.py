from typing import List
from models.artist import Artist

class IArtistDataAccess:
    def create_artist(self, artist: Artist) -> None:
        raise NotImplementedError

    def get_all_artists(self) -> List[Artist]:
        raise NotImplementedError

    def get_artist_by_id(self, artist_id: int) -> Artist:
        raise NotImplementedError

    def update_artist(self, artist: Artist) -> None:
        raise NotImplementedError

    def delete_artist(self, artist_id: int) -> bool:
        raise NotImplementedError
