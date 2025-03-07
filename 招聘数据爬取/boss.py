import requests
from bs4 import BeautifulSoup

# 登录URL
login_url = 'https://login.zhipin.com/?ka=header-login'

# 登录信息
login_data = {
    'account': 'your_username',  # 替换为你的用户名
    'password': 'your_password',  # 替换为你的密码
}

# 创建会话
session = requests.Session()

# 发送POST请求登录
response = session.post(login_url, data=login_data)

# 检查登录是否成功
if response.status_code == 200:
    print('登录成功')
else:
    print('登录失败')

# 定义要爬取的页面URL
url = 'https://www.zhipin.com/c101280600/?query=java&page=1&ka=page-1'

# 使用会话发送GET请求
response = session.get(url)

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 提取职位信息
jobs = soup.find_all('div', class_='job-primary')

# 打印职位信息
for job in jobs:
    title = job.find('h3', class_='name').text.strip()
    company = job.find('div', class_='company-text').find('a').text.strip()
    salary = job.find('span', class_='red').text.strip()
    location = job.find('span', class_='job-area-wrapper').text.strip()
    
    print(f"职位名称: {title}")
    print(f"公司名称: {company}")
    print(f"薪资待遇: {salary}")
    print(f"工作地点: {location}")
    print("-" * 50)