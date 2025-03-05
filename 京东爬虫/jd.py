import json
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

class JDCommentCrawler:
    def __init__(self, product_id, max_page=100):
        self.session = requests.Session()
        self.product_id = product_id
        self.max_page = max_page
        self.base_url = "https://club.jd.com/comment/productPageComments.action"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

        }

    def _get_params(self, page):
        """构造加密请求参数"""
        return {
            'productId': self.product_id,
            'score': 0,  # 0表示全部评价
            'sortType': 5,  # 按时间排序
            'page': page,
            'pageSize': 10,
            'isShadowSku': 0,
            'fold': 1
        }

    def _get_encrypted_url(self, page):
        """生成带加密参数的请求URL"""
        params = self._get_params(page)
        return f"{self.base_url}?{urlencode(params)}&callback=fetchJSON_comment98&_={int(time.time()*1000)}"

    def _parse_comments(self, data):
        try:
            # 添加原始数据保存用于调试
            with open("raw_response.txt", "w", encoding="utf-8") as f:
                f.write(data)
                
            # 动态检测回调函数名
            if data.startswith("fetchJSON_comment"):
                stripped_data = data.split("(", 1)[1].rsplit(")", 1)[0]
            else:
                stripped_data = data
                
            json_data = json.loads(stripped_data)
            
            # 增强字段校验
            if 'comments' not in json_data:
                print("返回数据异常，关键字段缺失。完整响应：")
                print(json.dumps(json_data, indent=2, ensure_ascii=False))
                return []
                
            return json_data['comments']
        except json.JSONDecodeError:
            print("响应内容不是有效JSON，可能触发反爬！原始响应：")
            print(data[:200])  # 打印前200字符用于分析
            return []
        except Exception as e:
            print(f"解析异常: {str(e)}")
            return []

    def crawl_all_comments(self):
        """执行完整爬取流程"""
        all_comments = []
        
        for page in range(0, self.max_page):
            try:
                # 设置随机延迟（避免触发反爬）
                time.sleep(random.uniform(1.5, 3.5))
                
                # 构造加密URL
                url = self._get_encrypted_url(page)
                
                # 发送请求
                response = self.session.get(url, headers=self.headers)
                
                if response.status_code == 200:
                    page_comments = self._parse_comments(response.text)
                    if not page_comments:
                        print(f"第{page}页无数据，终止爬取")
                        break
                    
                    all_comments.extend(page_comments)
                    print(f"成功获取第{page}页评论，累计{len(all_comments)}条")
                else:
                    print(f"请求失败: HTTP {response.status_code}")
                    break
            except Exception as e:
                print(f"第{page}页爬取出错: {str(e)}")
                break
        
        return all_comments

    def save_to_file(self, data, filename='jd_comments.json'):
        """保存数据到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到 {filename}")

# 使用示例
if __name__ == "__main__":
    crawler = JDCommentCrawler(product_id='100047982391')  # 替换目标商品ID
    comments = crawler.crawl_all_comments()
    crawler.save_to_file(comments)