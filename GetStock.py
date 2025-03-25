import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_stock(stock_code):
    try:
        url = f'https://tw.stock.yahoo.com/quote/{stock_code}.TW'
        headers = {
            'User-Agent':'Mozilla/5.0'
        }

        result = requests.get(url,headers=headers)
        soup = BeautifulSoup(result.text,'html.parser')

        stock_name = soup.find('h1',class_='C($c-link-text) Fw(b) Fz(24px) Mend(8px)')
        stock_price = (soup.find('span',class_='Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)') or soup.find('span',class_='Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)') or soup.find('span',class_='Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)'))

        #<h1 class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)">台積電</h1>
        #<span class="C($c-icon) Fz(24px) Mend(20px)">2330</span>
        #<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)">972</span>

        now = datetime.now().strftime('%Y / %m / %d - %H : %M : %S')

        if stock_name:
            return {
                'stock_name':stock_name.text,
                'stock_price':stock_price.text,
                'stock_num':stock_code,
                'time':now,
                'status':'Success',
                'currency':'新台幣'
            }
        else:
            return {
                'stock_num':stock_code,
                'status':'Stock Not Found'
            }
    except Exception as e:
        return {
            'stock_num':stock_code,
            'status':'Error',
            'message':str(e)
        }
    
#print(get_stock('2330'))