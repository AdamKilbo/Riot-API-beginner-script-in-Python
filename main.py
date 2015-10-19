#Note to self that this must be run with Python 2.7 because pip and requests is not installed on the latest version

from RiotAPI import RiotAPI

def main():
	api = RiotAPI('') # Your API key goes inbetween the blank quotes.
	r = api.get_summoner_by_name('golden foxes') # make a request to the API for information on the summoner name 'Golden Foxes' (my personal LoL summoner name). The variable R holds the JSON dictionary returned by the API.
	print r # printing the whole JSON dictionary
	print r['goldenfoxes'] # printing information on the summoner name Golden Foxes found within the JSON dictionary
	print r['goldenfoxes']['id'] # printing the ID of Golden Foxes within the JSON dictionary

if __name__ == "__main__":
	main()
