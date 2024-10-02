import requests
import os
import time
import random
import json

output_dir = "downloaded_gifs"
os.makedirs(output_dir, exist_ok=True)
downloaded_file = "downloaded_urls.json"

def load_downloaded_urls():
    if os.path.exists(downloaded_file):
        with open(downloaded_file, "r") as f:
            return set(json.load(f))
    return set()

def save_downloaded_urls(urls):
    with open(downloaded_file, "w") as f:
        json.dump(list(urls), f)

def download_gif():
    global downloaded_urls
    downloaded_urls = load_downloaded_urls()

    # 创建一个会话
    session = requests.Session()
    
    # 添加请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    while True:
        time.sleep(random.uniform(1, 3))

        # 发送请求获取数据
        response = session.get(api_url, headers=headers)

        print(f"请求状态码：{response.status_code}")
        print(f"响应内容：{response.text}")

        try:
            data = response.json()
        except json.JSONDecodeError:
            print("解析JSON失败，响应不是有效的JSON。")
            break

        if data["code"] == 0:
            icon_url = "https:" + data["data"]["icon"]
            
            if icon_url in downloaded_urls:
                print(f"已下载过的图像，跳过：{icon_url}")
                continue

            icon_response = session.get(icon_url, headers=headers)
            if icon_response.status_code == 200:
                file_number = len(downloaded_urls) + 1
                file_name = os.path.join(output_dir, f"icon_{file_number}.gif")

                with open(file_name, "wb") as f:
                    f.write(icon_response.content)

                downloaded_urls.add(icon_url)
                save_downloaded_urls(downloaded_urls)
                print(f"GIF文件已下载成功：{file_name}")
            else:
                print(f"下载失败，状态码：{icon_response.status_code}")
        else:
            print("获取数据失败，错误代码：", data["code"])
            break

if __name__ == "__main__":
    api_url = "https://api.bilibili.com/x/web-interface/index/icon"
    download_gif()
