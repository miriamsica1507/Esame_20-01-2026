import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def pp_dropdown(self):
        self._view.ddArtist.options = [ft.dropdown.Option(str(a)) for a in list(self._model.G.nodes())]
        self._view.update_page()

    def handle_create_graph(self, e):
        min_album = int(self._view.txtNumAlbumMin.value)
        if min_album < 0:
            self._view.show_alert('Inserire valore corretto')
            return
        else:
            self._model.load_artists_with_min_albums(min_album)
            self._model.build_graph()
            nodi, archi = self._model.num_nodi_archi()
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text(f'Num nodi {nodi}, num archi {archi}'))
        self._view.update_page()

    def handle_connected_artists(self, e):
        lista = self._model.artisti_connessi(e.control.value)
        self._view.txt_result.clean()
        for a,peso in lista:
            self._view.txt_result.control.append(ft.Text(f'{a},peso {peso}'))
        self._view.update_page()

