import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    def get_emoji(self, emoji):
        r = requests.get(f'https://api.github.githubassets.com/images/icons/{emoji}')
        body = r.json()

        return body
    
    def patch_user(self, name):
        r = requests.patch(f'https://api.github.com/users/{name}')
        body = r.json()

        return body