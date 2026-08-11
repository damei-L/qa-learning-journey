"""
conftest.py: Pytest全局Fixture
自动被Pytest发现，所有测试文件共享
"""

import yaml
import pytest
import os

@pytest.fixture(scope="session")
def config():
    """读取yaml文件"""
    # 获取当前文件所在目录的父目录（项目根目录）
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(root_dir, "config", "config.yaml")

    with open("config/config.yaml","r",encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture
def base_url(config):
    """从配置读取base_url"""
    return config["base_url"]

@pytest.fixture
def api_headers(config):
    """从配置读取headers"""
    return config["headers"]

@pytest.fixture
def timeout(config):
    """从配置读取timeout"""
    return config["timeout"]