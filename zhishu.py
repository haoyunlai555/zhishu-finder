import signal
import sys

a = 1491556
num = 23735557
stop_flag = False

def signal_handler(sig, frame):
    global stop_flag
    stop_flag = True

signal.signal(signal.SIGINT, signal_handler)

f = open("质数.txt", "a", encoding="utf-8")
buffer = []

try:
    while not stop_flag:
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            line = f"第 {a} 个质数： {num}\n"
            print(line.strip())
            buffer.append(line)
            if len(buffer) >= 100:
                f.writelines(buffer)
                f.flush()  # 强制刷盘，确保写进去
                buffer.clear()
            a += 1
        num += 1
except Exception as e:
    print(f"异常：{e}")
finally:
    # 不管怎么退出，这里一定执行
    if buffer:
        try:
            f.writelines(buffer)
        except:
            pass
    try:
        f.flush()
        f.close()
    except:
        pass
    print(f"\n已停止，共 {a - 1} 个质数，已保存至 质数.txt")