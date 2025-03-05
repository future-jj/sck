from bs4 import BeautifulSoup
import json
import re

# 将json 的
# 将中国日报的数据存储到本地，搜狐新闻，微博新闻，等等都存储到本地
# 整理出一系列时间背后的时间线

# 英语学习
# 锻炼身体
# 构建知识库
# 年薪达到三十万

def parse_sidebar(html):
    # 创建BeautifulSoup解析器对象，使用html.parser作为解析引擎
    soup = BeautifulSoup(html, 'html.parser')
    
    # 定义递归函数处理每一个菜单层级
    def process_node(ul_node):
        # 当前层级的菜单项列表
        items = []
        # 查找所有包含'td-sidebar-nav__section'类的<li>标签（仅直接子节点）
        for li in ul_node.find_all('li', class_=lambda x: x and 'td-sidebar-nav__section' in x.split()):
            # 提取链接
            link = li.find('a', class_='td-sidebar-link')
            if not link:
                continue
                
            node = {
                "id": link.get('id', '').strip(),
                "url": link.get('href', '').strip(),
                "text": link.get_text(strip=True),
                "children": []
            }
            
            # 处理子菜单（匹配含有foldable类的ul）
            child_ul = li.find('ul', class_=lambda x: x and 'foldable' in x.split())
            if child_ul:
                node['children'] = process_node(child_ul)
            
            items.append(node)
        return items
    
    # 从第一个UL开始解析（根据样例中的ul-1）
    root_ul = soup.find('ul', class_='ul-1')
    return process_node(root_ul)

# 使用示例
if __name__ == "__main__":
    with open('k8s.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    try:
        menu_data = parse_sidebar(html_content)
        print(json.dumps(menu_data, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {str(e)}")