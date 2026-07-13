"""
Day03: Pytest基础实战
把昨天的Requests脚本改造成Pytest格式
"""

import requests


def test_get_post():
    """测试：GET请求获取单篇文章"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Pytest的assert更简洁，失败时自动显示对比信息
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert "title" in data


def test_create_post():
    """测试：POST请求创建文章"""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "damei的Pytest测试",
        "body": "用Pytest发送POST请求",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == "damei的Pytest测试"
    assert "id" in data


def test_list_posts_with_params():
    """测试：GET带参数查询文章列表"""
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    response = requests.get(url, params=params)
    
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) > 0
    assert data[0]["userId"] == 1



    