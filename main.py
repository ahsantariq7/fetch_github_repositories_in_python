import requests

def get_github_repositories(username, token):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repositories = response.json()
        repo_names = [repo['name'] for repo in repositories]
        return repo_names
    else:
        print(f"Error: Unable to fetch repositories. Status code: {response.status_code}")
        return []

# Replace 'YOUR_GITHUB_USERNAME' and 'YOUR_ACCESS_TOKEN' with your actual GitHub username and access token.
github_username = 'your_username'
github_token = 'paste_your_access_token'

repo_names = get_github_repositories(github_username, github_token)
print("Your GitHub repositories:")
print(repo_names)
