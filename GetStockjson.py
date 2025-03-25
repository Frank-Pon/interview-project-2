import json
from GetStock import get_stock

search = input('請輸入股票代號')
result = get_stock(search)

if result['status'] == 'Success':
    print('查詢成功,將幫您輸出json檔')
else:
    print('查詢錯誤,請確認代號是否正確')

with open(f'{search}.json','w',encoding='utf-8') as f:
    json.dumps(result,f,ensure_ascii=False,indent=2)
