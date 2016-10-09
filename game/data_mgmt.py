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
