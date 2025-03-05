import requests  # 导入库
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"  # 目标网站（一个图书测试网站）
response = requests.get(url)  # 发送 GET 请求

# 检查是否成功（状态码 200 表示成功）
if response.status_code == 200:
    print("成功获取网页！")
else:
    print("请求失败，状态码：", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]  # 书名在 <a> 标签的 title 属性中
    price = book.find("p", class_="price_color").text  # 价格在 class 为 price_color 的 <p> 标签中
    print(f"书名：{title}，价格：{price}")