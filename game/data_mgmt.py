from django.conf import settings
import requests
import json
import pickle

class Data_mgmt:

	def getMovies(self):
		l = []
		for name in settings.MOVIES:
			response = requests.get("http://www.omdbapi.com/?t=" + name + "&plot=short&r=json")
			l.append(json.loads(response.text))
		return l

	def picklize(self):
		f = open("data_pickled", "wb")
		pickle.dump(self.getMovies(), f)
		f.close()

	def unpicklize(self):
		f = open("data_pickled", "rb")
		obj = pickle.load(f)
		for item in obj:
			print(item['Title'])
		f.close()

# {Data management} (class)
# 	[ ] ’load’ :					Charge les données de jeu passés en paramètres dans l’instance
# 									de classe.
# 									Retourne l’instance courante.

# 	[ ] ’dump’ :					Retourne les données de jeu.

# 	[ ] ’get_random_movie’ :		Retourne un Moviemon au hasard parmis les Moviemons
# 									non capturés.

# 	[ ] ’load_default_settings’ :	Charge les données de jeu dans l’instance de classe depuis
# 									les settings. Requête et stocke les détails de tous les
# 									Moviemons sur IMDB. Retourne l’instance courante.

# 	[ ] ’get_strength’ :			Retourne la force du joueur.

# 	[ ] ’get_movie’ :				Retourne un dictionnaire Python contenant tous les détails
# 									depuis le nom du Moviemon passé en paramètre et nécessaires à
# 									la page Detail
