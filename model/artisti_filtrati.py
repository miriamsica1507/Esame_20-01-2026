from dataclasses import dataclass
@dataclass
class ArtistiFiltrati:
    artist_id: int
    name: str
    num_album: int

    def __hash__(self):
        return hash(self.artist_id)

