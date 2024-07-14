import requests

# GitHub credentials
username = 'vijayendra-k'
repository = 'Portfolio'
token = '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'

# GitHub API URL for repository traffic views
url = f'https://api.github.com/repos/{username}/{repository}/traffic/views'

# Making a GET request to the GitHub API
response = requests.get(url, headers={'Authorization': f'token {token}'})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    count = data['count']
    uniques = data['uniques']
    print(f'Total Views: {count}')
    print(f'Unique Visitors: {uniques}')
else:
    print(f'Failed to fetch data: {response.status_code}')
    print(response.json())  # Print the error message from GitHub API
