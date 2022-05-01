wordsListPath = '/home/maincpp/WordsFinder/parseDictionaries/words/mielstronk58k.txt'

#Python script to get word definitions from the Oxford Dictionary API and store them in a text file

import requests as r
import json

WORDS = ['forebrain','occipital','temporal_lobe','gyrus','sulcus','hippocampus','inhibitory_neurons', 'run']

app_id = 'b62d6a70'
app_key = '0b65d2166229a7e856cb85f797d8bcb9'
headers = {'app_id':app_id, 'app_key':app_key}

base_url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' #last one (en) is language

output = 'DEFINITIONS\n\n'

for i in range(0,len(WORDS)):
	url = base_url + WORDS[i].lower()
	#print(url)
	response = r.get(url, headers=headers)

	#If request goes through (HTTP code 200), append definition to output, otherwise do nothing
	if response.status_code == r.codes.ok:
		response_json = response.json()
		definition = response_json['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0] #access word definition
		output += WORDS[i].title().replace("_", " ") + ':\n' + definition.capitalize() + '\n\n' #formatting

filename = 'definitions.txt'

f = open(filename,'w')
f.write(output)
f.close()