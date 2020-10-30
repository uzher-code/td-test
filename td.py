import urllib3, json

url = "https://jsonplaceholder.typicode.com/users"

http = urllib3.PoolManager()

r = http.request('GET', url)

print(r.status)

my_json = json.loads(r.data.decode('utf-8'))
print(my_json[0])

print(my_json[0]['id'])


f = open("test.txt", "w")

f.write(json.dumps(my_json[9]))

f.close()

