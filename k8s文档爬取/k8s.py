import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_kubernetes_versions(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        # 发送请求并获取页面内容
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取元数据
        meta_description = soup.find("meta", {"name": "description"})["content"].strip()
        last_modified = soup.find("div", class_="text-muted").text.split("Last modified")[1].strip()
        
        # 提取版本信息
        versions = []
        
        # 最新版本
        latest_section = soup.find("h2", id="version-latest")
        latest_item = latest_section.find_next("li")
        versions.append({
            "version": latest_item.a.text.strip(),
            "url": latest_item.a["href"],
            "status": "latest",
            "description": "Current documentation"
        })
        
        # 旧版本
        older_section = soup.find("h2", id="versions-older")
        for item in older_section.find_next("ul").find_all("li"):
            versions.append({
                "version": item.a.text.strip(),
                "url": item.a["href"],
                "status": "older",
                "description": "Archived documentation"
            })
        
        # 提取反馈信息
        feedback = {
            "helpful_question": soup.find("p", class_="feedback--prompt").text.strip(),
            "yes_button": soup.find("button", class_="feedback--yes").text.strip(),
            "no_button": soup.find("button", class_="feedback--no").text.strip(),
            "issue_link": soup.find("a", class_="feedback--link")["href"]
        }
        
        # 构建完整数据集
        data = {
            "metadata": {
                "page_title": soup.title.text.strip(),
                "description": meta_description,
                "last_modified": last_modified,
                "source_url": url
            },
            "versions": versions,
            "feedback": feedback
        }
        
        return data
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def save_to_csv(data, filename):
    # 转换版本数据为 DataFrame
    df = pd.DataFrame(data["versions"])
    
    # 添加元数据列
    df["page_title"] = data["metadata"]["page_title"]
    df["last_modified"] = data["metadata"]["last_modified"]
    df["source_url"] = data["metadata"]["source_url"]
    
    # 保存到 CSV
    df.to_csv(filename, index=False)
    print(f"数据已保存到 {filename}")

# 使用示例
if __name__ == "__main__":
    target_url = "https://kubernetes.io/docs/home/"
    parsed_data = parse_kubernetes_versions(target_url)
    
    if parsed_data:
        save_to_csv(parsed_data, "kubernetes_doc_versions.csv")
        
        # 打印元数据
        print("\n元数据信息:")
        for key, value in parsed_data["metadata"].items():
            print(f"{key}: {value}")
            
        # 打印反馈信息
        print("\n反馈信息:")
        for key, value in parsed_data["feedback"].items():
            print(f"{key}: {value}")