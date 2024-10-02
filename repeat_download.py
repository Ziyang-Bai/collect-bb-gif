import subprocess
import time

def repeat_download(num_times):
    for i in range(num_times):
        print(f"第 {i + 1} 次调用下载程序...")
        subprocess.run(["python", "download_gif.py"])  # 调用下载GIF程序
        time.sleep(5)  # 每次调用之间的延时（可以根据需要调整）

if __name__ == "__main__":
    repeat_count = int(input("Counter?>"))  # 设置调用次数
    repeat_download(repeat_count)
