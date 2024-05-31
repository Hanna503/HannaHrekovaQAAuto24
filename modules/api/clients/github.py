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
    
    def get_emoji(self, emoji_code):
        self.base_url = 'https://api.github.com'
        r = requests.get(f'https://github.githubassets.com/images/icons/emoji/unicode/{emoji_code}')

        return r.status_code
    
    def get_commit(self, owner, repo, commit_sha):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/git/commits/{commit_sha}')
        body = r.json()

        return body