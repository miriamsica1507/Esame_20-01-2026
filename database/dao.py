from unittest import result

from database.DB_connect import DBConnect
from model.artist import Artist
from model.artisti_filtrati import ArtistiFiltrati


class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_with_min_album(min_albums):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.id as artist_id, a.name, count(*) as num_album
                    FROM artist a, album al 
                    where a.id = al.artist_id
                    group by a.id , a.name
                    having COUNT(*) > %s """
        cursor.execute(query, (min_albums,))
        for row in cursor:
            a = (ArtistiFiltrati(**row))
            result.append(a)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()
        connessioni = []
        cursor = conn.cursor(dictionary=True)
        query = """select least(a1.id , a2.id) as a1, greatest(a1.id , a2.id) as a2, count(*) as num  
                    from artist a1, artist a2, album al1, album al2, track t1, track t2
                    where a1.id  = al1.artist_id  and a2.id = al2.artist_id and al1.id = t1.album_id and al2.id = t2.album_id
                    and t1.genre_id = t2.genre_id 
                    group by a1, a2"""
        cursor.execute(query)
        for row in cursor:
            connessioni.append((row['a1'], row['a2'], row['num']))

        cursor.close()
        conn.close()
        return connessioni
