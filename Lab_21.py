# import requests

# # Define the API endpoint
# url = 'https://jsonplaceholder.typicode.com/posts'

# # Define the data to send
# new_post = {
#     "title": "My New Post",
#     "body": "This is the content of my new post.",
#     "userId": 1
# }

# # Make a POST request
# response = requests.post(url, json=new_post)

# # Check the status code
# if response.status_code == 201:
#     # Parse JSON response
#     created_post = response.json()
#     print("Created Post:")
#     print(f"Title: {created_post['title']}")
#     print(f"Body: {created_post['body']}")
# else:
#     print(f"Failed to create post. Status code: {response.status_code}")

# import requests

# url = 'https://jsonplaceholder.typicode.com/posts/1000'  # Non-existent post

# response = requests.get(url)

# if response.status_code == 200:
#     post = response.json()
#     print("Fetched Post:", post)
# else:
#     print(f"Error: {response.status_code} - {response.reason}")


#---------------POST LABS-----------------

import requests 
 
class Client: 
 
    def __init__(self): 
        self.base_url = "https://jsonplaceholder.typicode.com" 
 
    def get_posts(self): 
        url = f"{self.base_url}/posts" 
        x = requests.get(url) 
        if x.status_code == 200: 
            return x.json() 
        return None 
 
    def create_post(self, title, body, userId): 
        url = f"{self.base_url}/posts" 
        data = { 
            "title": title,
           "body": body, 
            "userId": userId 
        } 
        a = requests.post(url, json=data) 
        if a.status_code == 201: 
            return a.json() 
        return None 
 
 
# Client class: 
client = Client() 
 
posts = client.get_posts() 
if posts: 
    print("\nFetched Posts:") 
    for post in posts[:5]: 
        print(post["title"]) 
 
post = client.create_post("Demo Post", "This is a demo content", 5) 
if post: 
    print("\nNew Post Created Successfully:") 
    print(post)

