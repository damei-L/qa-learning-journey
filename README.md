# QA 学习之路

目标：高级测试工程师（Web/API/App）  
周期：2026.7 - 2026.10

## 现有基础
- Selenium Web自动化（Python）
- Postman 接口手工测试
- Navicat 数据库操作

## 学习进度

### Week 1: Python API自动化基础 ✅
| 日期 | 内容 | 文件 |
|------|------|------|
| Day01 | HTTP协议核心 | `day01_http_notes.md` |
| Day02 | Python Requests库 | `day02_requests_demo.py` |
| Day03 | Pytest基础 | `test_api_pytest.py` |
| Day04 | Pytest Fixture + 参数化 | `test_api_fixture.py` |

### Week 2: 框架搭建与CI/CD 🔄
- [ ] 框架目录结构设计
- [ ] 配置文件管理（YAML/JSON）
- [ ] Allure报告集成
- [ ] Jenkins流水线配置

## 运行方式

```bash
# 安装依赖
pip install requests pytest pytest-html

# 运行测试
pytest -v

# 生成HTML报告
pytest --html=report.html