#Note to self that this must be run with Python 2.7 because pip and requests is not installed on the latest version

from RiotAPI import RiotAPI

def main():
	api = RiotAPI('') # Your API key goes inbetween the blank quotes.
	r = api.get_summoner_by_name('golden foxes')
	print r
	print r['goldenfoxes']
	print r['goldenfoxes']['id']

if __name__ == "__main__":
	main()