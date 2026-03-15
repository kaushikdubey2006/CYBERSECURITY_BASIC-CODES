import requests

url = "https://api.github.com/users/kaushikdubey2006"

response = requests.get(url)
data = response.json()

print("Username:", data["login"])
print("Name:", data["name"])
print("Bio:", data["bio"])
print("Public Repos:", data["public_repos"])
print("Followers:", data["followers"])
print("Following:", data["following"])