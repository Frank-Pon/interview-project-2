from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        body = request.get_json(force=True)  # 加上 force=True 以防空 payload 出錯
        print("✅ 收到 webhook 資料：")
        print(body)

        if "events" in body:
            for event in body["events"]:
                user_id = event["source"]["userId"]
                print(f"🎯 抓到 userId：{user_id}")

        return jsonify({"status": "ok"}), 200  # 一定要回傳 200 OK
    except Exception as e:
        print("❌ 發生錯誤：", e)
        return jsonify({"status": "error", "message": str(e)}), 200  # 即使錯誤也回 200

if __name__ == '__main__':
    app.run(port=5000)
