import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self._artisti_filtrati = []
        self._map_id = {}

        self.G = nx.Graph()
        self._nodes = []
        self._edges = []

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        self._artisti_filtrati = DAO.get_all_with_min_album(min_albums)
        return self._artisti_filtrati

    def map_id(self):
        self._map_id = {}
        for artist in self._artisti_filtrati:
            self._map_id[artist.id] = artist
        return self._map_id

    def build_graph(self):
        self.G.clear()
        self.G.add_nodes_from(self._artisti_filtrati)
        conessioni = DAO.get_connessioni()
        for a1,a2, num in conessioni:
            if (a1,a2) in self._artisti_filtrati:
                self._graph.add_edge(a1,a2,weight=num)
        return self.G

    def num_nodi_archi(self):
        return self.G.number_of_nodes(), self.G.number_of_edges()

    def artisti_connessi(self,a1):
        artisti_connessi = []
        for n in self.G.neighbors(a1):
                peso = self.G[a1][n]['weight']
                artisti_connessi.append((n,peso))
        sorted(artisti_connessi, key=lambda x: x[0])
        return artisti_connessi


