# 写一个函数，接收任意数量的数字，返回它们的平均值
def average(*numbers):
    # 你的代码
    result = sum(numbers) / len(numbers)
    return result

print(average(10, 20, 30))  # 应该输出 20.0
print(average(5, 15))       # 应该输出 10.0