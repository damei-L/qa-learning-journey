#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mock回调服务 - 使用Python标准库http.server
无需安装flask，Python 3.x自带
"""

import json
import uuid
from http.server import HTTPServer, BaseHTTPRequestHandler

class MockHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 读取请求体
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        print(f"\n{'='*60}")
        print(f"[RECV] 收到 {self.path} 请求")
        print(f"[RECV] Headers: {dict(self.headers)}")
        print(f"[RECV] Body: {body}")
        
        # 解析请求体
        try:
            req_data = json.loads(body) if body else {}
        except:
            req_data = {}
        
        # 获取场景（默认auto_archive）
        scene = req_data.get('mock_scene', 'auto_archive')
        
        # 构造响应
        resp = {
            "appId": req_data.get('appId', '100001'),
            "nonce": uuid.uuid4().hex,
            "seq": req_data.get('seq', 'SEQ_' + uuid.uuid4().hex[:16]),
            "actId": req_data.get('actId', '20230830091519498'),
            "callResult": "0",
            "recordPath": "http://mock-server/record/test.mp3"
        }
        
        if scene == 'auto_archive':
            resp["seqResult"] = json.dumps({
                "是否满意": "9", "是否解决": "是",
                "是否有升级投诉意图": "否", "是否有新问题要求": "否"
            }, ensure_ascii=False)
        elif scene == 'manual_intervention':
            resp["seqResult"] = json.dumps({
                "是否满意": "5", "是否解决": "是",
                "是否有升级投诉意图": "否", "是否有新问题要求": "否"
            }, ensure_ascii=False)
        elif scene == 'auto_reject':
            resp["seqResult"] = json.dumps({
                "是否满意": "9", "是否解决": "否",
                "是否有升级投诉意图": "否", "是否有新问题要求": "否"
            }, ensure_ascii=False)
        elif scene == 'trial':
            resp["seqResult"] = json.dumps({
                "是否满意": "9", "是否解决": "试用中",
                "是否有升级投诉意图": "否", "是否有新问题要求": "否"
            }, ensure_ascii=False)
        else:
            resp = {"error": "未知场景"}
        
        resp_body = json.dumps(resp, ensure_ascii=False).encode('utf-8')
        
        # 发送响应
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(resp_body)
        
        print(f"[SEND] 响应: {resp}")
        print(f"{'='*60}")
    
    def log_message(self, format, *args):
        # 禁用默认日志，我们用自定义的
        pass


if __name__ == '__main__':
    PORT = 5001
    server = HTTPServer(('0.0.0.0', PORT), MockHandler)
    print(f"Mock回调服务启动: http://localhost:{PORT}/aisp-data-interface/aisp/callbackResult")
    print("按 Ctrl+C 停止服务")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止")