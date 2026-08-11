"""
使用YAML配置的测试用例
"""

import requests
import pytest

def test_get_post_with_config(base_url):
    """使用配置的GET测试"""
    response = requests.get(f"{base_url}/posts/1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    print(f"✅ GET测试通过，标题: {data['title'][:30]}...")

def test_create_post_with_config(base_url, api_headers):
    """使用配置的POST测试"""
    payload = {
        "title": "YAML配置测试",
        "body": "从配置文件读取base_url和headers",
        "userId": 1
    }
    response = requests.post(
        f"{base_url}/posts",
        json=payload,
        headers=api_headers
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "YAML配置测试"
    print(f"✅ POST测试通过，新ID: {data['id']}")

@pytest.mark.parametrize("user_id, expected_posts", [
    (1, 10),
    (2, 10),
])
def test_list_posts_with_config(base_url, user_id, expected_posts):
    """使用配置的参数化测试"""
    response = requests.get(f"{base_url}/posts", params={"userId": user_id})
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == expected_posts
    print(f"✅ userId={user_id}的文章数量: {len(data)}")