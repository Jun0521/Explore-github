import requests

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('Status code:',r.status_code)
response_dict=r.json()
print('Total repositories:',response_dict['total_count'])
repo_dicts=response_dict['items']
print('Repositories returned:',len(repo_dicts))
print("\nPython's popular Repository on GitHub:")
for repo_dict in repo_dicts:
    print('\n\nNAME:',repo_dict['name'])
    print('OWNER:',repo_dict['owner']['login'])
    print('STARS:',repo_dict['stargazers_count'])
    print('REPOSITORY:',repo_dict['html_url'])
    print('CREATED:',repo_dict['created_at'])
    print('UPDATED:',repo_dict['updated_at'])
    print('DESCRIPTION:',repo_dict['description'])

