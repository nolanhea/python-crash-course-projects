import requests
from plotly.graph_objs import Bar
from plotly import offline
# Make api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in variable
response_dict = r.json()

repo_dicts = response_dict['items']

repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    repo_url = repo_dict['html_url']
    label = f"<a href = '{repo_url}'> {repo_dict['name']}</a>"
    labels.append(label)

# Make visualisation
data = [{
    'type': 'bar',
    'x': labels,
    'y': stars,
    'hovertext': labels,
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most starred Python projecs on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')


