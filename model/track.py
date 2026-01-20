from dataclasses import dataclass
@dataclass
class Track:
    id : int
    name :str
    album_id : int
    media_type_id :int
    genre_id : int
    composer : int
    milliseconds : int
    bytes : int
    unit_price : int