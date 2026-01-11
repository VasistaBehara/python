import requests
# response = requests.get('https://jsonplaceholder.typicode.com/users/1')
# d = response.json()
# print(f'name is {d['name']}, email is {d['email']}')
# response1 = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# if response1.status_code != 200:
#     print("ERROR")
# else:
#     print(response1.json()['title'])
# response2 = requests.get('https://jsonplaceholder.typicode.com/posts')
# posts = response2.json()
# count = 0
# for post in posts:
#     if post['userId'] == 1:
#         count+=1
# print(count)
# try:
#     response3 = requests.get('https://httpstat.us/200?sleep=3000', timeout=2)
#     print(response3.status_code)
# except requests.exceptions.RequestException:
#     print("FAILED")
# payload = {
#   "title": "CodeSignal",
#   "body": "Interview",
#   "userId": 1
# }
# url = "https://jsonplaceholder.typicode.com/posts"
# response4 = requests.post(url, json=payload)
# print(response4.json()['id'])
# def combine():
#     users = requests.get('https://jsonplaceholder.typicode.com/users')
#     users_list = users.json()
#     for user in users_list:
#         if user['username'] == 'Bret':
#             user_id = user['id']
#             print(f'user id for Bret is: {user_id}')
#             break
#     posts = requests.get('https://jsonplaceholder.typicode.com/posts')
#     posts_list = posts.json()
#     for post in posts_list:
#         if post['userId'] == user_id:
#             print(post)

# combine()

def advanced():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts_list = posts.json()
    print(posts_list)
advanced()