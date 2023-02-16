import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"


    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+ username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+ username + '/repos')
        return response.json()


github = Github()



while True:
    enter = input("1-Find User\n2-Get Repositories\n3-Exit\nSelection: ")

    if enter == "1":
        username_find = input("Username: ")
        result = github.getUser(username_find)
        print("*"* 30)
        print(f"name: {result['name']}\nPublic Repos: {result['public_repos']}\nFollowing: {result['following']}\nFollowers: {result['followers']}")
        print("*"* 30)
    elif enter == "2":
        repos_find = input("Username Repos: ")
        result = github.getRepositories(repos_find)
        for repo in result:
            print(f"Repo Name: {repo['name']}\nRepo URL: {repo['html_url']}\nClone URL: {repo['clone_url']}")
    elif enter == "3":
        exit(0)
    else:
        print("Error!!")

 # Coded By Onurhocaoglu
 # https://www.onurhocaoglu.com
