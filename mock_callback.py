# mock_callback_server.py
from flask import Flask, request, jsonify
import uuid
import json

app = Flask(__name__)

@app.route('/aisp-data-interface/aisp/callbackResult', methods=['POST'])
def callback_result():
    data = request.get_json() or {}
    print(f"\n[RECV] 收到回调请求:")
    print(f"  Headers: {dict(request.headers)}")
    print(f"  Body: {json.dumps(data, indent=2, ensure_ascii=False)}")
    
    scene = data.get('mock_scene', 'auto_archive')
    
    resp = {
        "appId": data.get('appId', '100001'),
        "nonce": uuid.uuid4().hex,
        "seq": data.get('seq', 'SEQ_' + uuid.uuid4().hex[:16]),
        "actId": data.get('actId', '20230830091519498'),
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
        return jsonify({"error": "未知场景"}), 400
    
    print(f"[SEND] 返回响应:")
    print(f"  {json.dumps(resp, indent=2, ensure_ascii=False)}")
    return jsonify(resp)

if __name__ == '__main__':
    print("Mock回调服务启动: http://0.0.0.0:5001/aisp-data-interface/aisp/callbackResult")
    app.run(host='0.0.0.0', port=5001, debug=True)