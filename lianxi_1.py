

"""
def add(a,b):
    result = a+b
    return result


print(add(20,10))
"""
import time


def measure_time():
    start = time.time() #记录开始时间
    time.sleep(2)  #模拟消耗两秒
    end = time.time() #记录结束时间
    duration = end - start #差值-耗时
    return duration

print(f"耗时{measure_time()}秒")