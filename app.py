from flask import Flask,jsonify,render_template,request
import json
from line_bot import Notify
from GetStock import get_stock

app = Flask(__name__)

access_token='6aPFf4xSSSEs+MEF4+qkT6yGtVolZ9riYKAd8i/NtHsbS1qba/VdqCXcwuIcwbVY2rGfcgk4zuiDVvOx7tLOR+6kquhXHt99N6IpEUMRiNiRFRu6s07F7ymzQvjeEIFX3zlSf3lZ3VCy1rYoDvNY5QdB04t89/1O/w1cDnyilFU='
user_id = 'U037ef2ca1e20d501a61686a1b8b075ab'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multi_check',methods = ['POST'])
def multi_check():
    '''
    stock_list是前端傳回來的list of dict
    回傳結果為：
    
    [
    
    {'stock_code':'2330','target':'1200'},
    
    {'stock_code':'00637L','target':'20'}

    ] 

    使用for 迴圈取出每支股票的代號與目標價，呼叫get_stock取得每支股票的詳細資訊
    '''
    stock_list = request.get_json()
    result = []

    for stock in stock_list:
        code = stock['stock_code']
        target = stock.get('target')
        data = get_stock(code)
    
        if data['status'] == 'Success':
            try:
                price = float(data['stock_price'].replace(',',''))

                if target and price <= target:
                    message = f"{data['stock_name']} ( {code} ) 的當前股價為： {price} ,已低於您設定的目標價格 {target} ,請把握機會入手!"
                    Notify(message,user_id,access_token)
            except Exception as e:
                pass
        result.append(data)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

