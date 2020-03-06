import requests
resp=requests.get('https://rover.codingcontest.org/rover/create?map=L4_MFJS3487&username=xivitazo&contestId=practice')
print (resp.status_code)