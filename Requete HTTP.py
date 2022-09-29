import http,json
r = http.get('http://youtube.com')
print(r.text) # affiche le contenu de la réponse
print(r.json) #affiche le json de la réponse si il y en as
print(r.headers) #Affiche les headers de la réponse sous forme de dictionnaire
print(r.headers['Content-Type']) # affiche le content_type
r = http.get('http://youtube.com')
r = http.post('http://youtube.com')
r = http.delete('http://youtube.com')
r = http.put('http://youtube.com')
r = http.patch('http://youtube.com')
r = http.get('un_site_avec_json.fr')
donnees = json.dumps(r.json)

url = 'votresite.fr'
donnees = json.loads({prenom : 'michel'}) # formatage du dictionnaire vers le json
r = requests.post(url, data=donnees) #envoi des données

from http import HTTPStatus
HTTPStatus.OK
HTTPStatus.OK: 200
HTTPStatus.OK == 200
True
HTTPStatus.OK.value
200
HTTPStatus.OK.phrase
'OK'
HTTPStatus.OK.description
'Request fulfilled, document follows'
list(HTTPStatus)
[<HTTPStatus.CONTINUE: 100>, <HTTPStatus.SWITCHING_PROTOCOLS:101>, ...]

