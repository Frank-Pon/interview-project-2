from flask import Flask,jsonify,render_template,request
import json
from line_bot import Notify
from GetStock import get_stock

access_token='6aPFf4xSSSEs+MEF4+qkT6yGtVolZ9riYKAd8i/NtHsbS1qba/VdqCXcwuIcwbVY2rGfcgk4zuiDVvOx7tLOR+6kquhXHt99N6IpEUMRiNiRFRu6s07F7ymzQvjeEIFX3zlSf3lZ3VCy1rYoDvNY5QdB04t89/1O/w1cDnyilFU='
user_id = 'U037ef2ca1e20d501a61686a1b8b075ab'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock/<stock_code>')
def stock_api(stock_code):
    target = request.args.get('target',type=float)
    result = get_stock(stock_code)
    
    
    if result['status'] == 'Success':
        try:
            current_price = float(result['stock_price'].replace(',',''))

            if target and current_price < target:
                message = f"{result['stock_name']} ( {result['stock_num']} ) 的當前股價為： {current_price} ,已低於您設定的目標價格 {target} ,請把握機會入手!"
                Notify(message,user_id,access_token)
        except Exception as e:
            return f'股價轉換錯誤,錯誤訊息： {str(e)}'
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

