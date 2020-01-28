import requests #导入requests库

url='https://api.github.com/search/repositories?q=language:python&sort=stars'#请求页面地址

r=requests.get(url)#使用requests库get方法
response_dict=r.json()#将返回的json数据存储在字典中
repo_dicts=response_dict['items']#把键为items的值存在变量repo_dicts中(是个列表)
repo_dict=repo_dicts[0]#把列表的第一个字典存在变量repo_dict中（是个字典）

print("\nPython's highest star repository on GitHub:\n")#输出标题
#输出想要的字典键值
print('NAME:',repo_dict['name'])
print('OWNER:',repo_dict['owner']['login'])
print('STARS:',repo_dict['stargazers_count'])
print('REPOSITORY:',repo_dict['html_url'])
print('CREATED:',repo_dict['created_at'])
print('UPDATED:',repo_dict['updated_at'])
print('DESCRIPTION:',repo_dict['description'])

