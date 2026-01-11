import requests
# import json
# payload = {
#     'user': 'vasista',
#     'passwd': 'avinash'
# }
r = requests.get('http://localhost/basic-auth/vasista/avinash', auth=('vasista','avinash'))
# with open('comic.png','wb') as f:
#     f.write(r.content)
# print(r.json())
# print(f'is status ok? {r.ok}')
print(r.text)
# d = r.json()
# for item in d.items():
#     print(item)
# print(d['form'])