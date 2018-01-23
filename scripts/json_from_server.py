import requests

# r = requests.post("http://localhost:5000/exchange", json={'data': 137})
#r = requests.post("https://ravevirtualpet.herokuapp.com/exchange", json={'data': 137})

#r = requests.post("https://ravevirtualpet.herokuapp.com/add_data",
#                  json={'instruction': "FORWARD",
#                        'mood': "HAPPY"})

r = requests.post("http://localhost:5000/add_data",
                  json={'instruction': "FORWARD",
                        'mood': "HAPPY"})

if r.status_code == requests.codes.ok:
    data = r.json()
    print("Data OK: ", data)
else:
    print("error fetching, status is ", r.status_code)
