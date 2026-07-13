"""
Day04: Pytest Fixture + 参数化实战
"""


import pytest
import requests

#=============fixture定义区===============

@pytest.fixture
def base_url():
    """基础URL，所有测试共享"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_headers():
    """请求头，模拟真实项目"""
    return{
        "Content-Type":"application/json",
        "Accept":"application/json"
    }
    

@pytest.fixture
def post_payload():
    """post请求的数据模版"""
    return{
        "title":"fixture测试文章",
        "body":"用fixture管理测试数据",
        "userId":1
    }

#=============测试函数区===============
def test_get_post_with_fixture(base_url):
    """使用fixture的get测试"""
    response = requests.get(f"{base_url}/posts/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    print(f"✅️get测试通过，标题：{data['title'][:30]}……")

def test_create_post_with_fixture(base_url,post_payload,api_headers):
    """使用fixture的post测试"""
    response = requests.post(f"{base_url}/posts",json=post_payload,headers=api_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == post_payload["title"]
    print(f"✅️测试通过，新ID:{data['id']}")

#==================参数化测试区=====================

@pytest.mark.parametrize("post_id,expected_user_id",[(1,1),(2,1),(3,1)])
def test_post_belongs_to_user(base_url,post_id,expected_user_id):
    """参数化测试：验证多篇文章的userID"""
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    data =response.json()
    assert data["userId"] == expected_user_id
    print(f"✅️文章{post_id}的userId={data['userId']}，符合预期")


@pytest.mark.parametrize("user_id,expected_count",[(1,10)])

def test_list_posts_by_user(base_url,user_id,expected_count):
    """参数化测试：验证用户文章数量"""
    response= requests.get(f"{base_url}/posts",params={"userId":user_id})
    assert response.status_code == 200
    data =response.json()
    assert len(data) == expected_count
    print(f"✅️userId={user_id}的文章数量：{len(data)},符合预期")