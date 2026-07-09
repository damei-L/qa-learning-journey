"""
Day02: Python Requests库实战
使用 jsonplaceholder.typicode.com 作为测试API
"""

import requests


def test_get_post():
    """API 1: GET请求 - 获取单篇文章"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    assert response.status_code == 200, f"预期200，实际{response.status_code}"
    
    data = response.json()
    print(f"状态码: {response.status_code}")
    print(f"用户ID: {data['userId']}")
    print(f"文章ID: {data['id']}")
    print(f"标题: {data['title'][:40]}...")
    print("-" * 40)


def test_create_post():
    """API 2: POST请求 - 创建文章"""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "damei的测试文章",
        "body": "这是用Python Requests库发送的POST请求",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 201, f"预期201，实际{response.status_code}"
    
    data = response.json()
    print(f"状态码: {response.status_code}")
    print(f"创建成功，新ID: {data['id']}")
    print(f"标题: {data['title']}")
    print("-" * 40)


def test_list_posts_with_params():
    """API 3: GET带参数 - 查询用户文章列表"""
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    response = requests.get(url, params=params)
    
    assert response.status_code == 200
    
    data = response.json()
    print(f"状态码: {response.status_code}")
    print(f"返回条数: {len(data)}")
    print(f"第一篇文章标题: {data[0]['title'][:40]}...")
    print("-" * 40)


if __name__ == "__main__":
    print("=" * 50)
    print("Day02: 开始执行API测试...")
    print("=" * 50)
    
    test_get_post()
    test_create_post()
    test_list_posts_with_params()
    
    print("=" * 50)
    print("全部执行完成！")
    print("=" * 50)