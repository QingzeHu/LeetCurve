import requests

class GitHubAPI:
    def __init__(self, repo, token):
        self.repo = repo
        self.api_url = f"https://api.github.com/repos/{repo}"
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {token}'
        }
    
    def get_commits(self, path):
        url = f"{self.api_url}/commits"
        params = {'path': path}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_files(self, path=''):
        url = f"{self.api_url}/contents/{path}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        contents = response.json()
        files = []
        
        for item in contents:
            if item['type'] == 'file':
                files.append(item)
            elif item['type'] == 'dir':
                files.extend(self.get_files(item['path']))
        
        return files
