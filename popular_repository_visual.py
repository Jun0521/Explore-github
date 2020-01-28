import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
response_dict=r.json()
print('Total repositories:',response_dict['total_count'])
repo_dicts=response_dict['items']
names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict={
    'value':repo_dict['stargazers_count'],
    'label':str(repo_dict['description']),
    'xlink':repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
#    stars.append(repo_dict['stargazers_count'])
    
my_style = LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title='Most-starred Python Projects on Github'
chart.x_labels=names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
