from django.conf import settings
import requests
import json
import pickle
import random

class Data_mgmt:

	def get_strength(self):
		return len(self.dump()['Moviedex'])

	def load_default_settings(self):
		moviedex = []
		position = settings.PLAYER_START
		nbr_balls = 3
		for name in settings.MOVIES:
			response = requests.get("http://www.omdbapi.com/?t=" + name + "&plot=short&r=json")
			movielist.append(json.loads(response.text))
		self.dic = {"position": position, "nbr_balls": nbr_balls, "Moviedex": moviedex, "Movies": movielist}
		picklize()
		return self

	def load(self, pos, balls, dex)
		movielist = self.dump['Movies']
		moviedex.append(dex)
		position = pos
		nbr_balls = balls
		self.dic = {"position": position, "nbr_balls": nbr_balls, "Moviedex": moviedex, "Movies": movielist}
		picklize()
		return self

	def dump(self):
		obj = unpicklize()
		return (obj)

	def get_random_movie(self):
		obj = self.dump()
		mv = obj['Movies']
		dex = obj['Moviedex']
		while len(dex) < len(mv):
			var = random.choice(mv)
			if dex.find(var['Title']) == -1:
				return var

	def get_movie(self, name):
		obj = self.dump()['Movies']
		for item in obj:
			if item['Title'] == name:
				return item

	def picklize(self):
		f = open("data_pickled", "wb")
		pickle.dump(self.dic, f)
		f.close()

	def unpicklize(self):
		f = open("data_pickled", "rb")
		obj = pickle.load(f)
		f.close()
		return obj
