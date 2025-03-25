import requests

def Notify(message,user_id,access_token):
    url = 'https://api.line.me/v2/bot/message/push' #LINE機器人通用API網址
    headers={
        'Content-type':'Application/json',
        'Authorization':f'Bearer {access_token}'
    } #告訴LINE你是以甚麼身分拜訪

    body={
        'to':user_id,
        'messages':[
            {
                'type':'text',
                'text':message
            }
        ]
    } #要傳送給誰跟傳送的訊息

    res = requests.post(url,headers=headers,json=body) #因為是要推送所以這邊使用post請求
    return res.status_code,res.text #最後回傳狀態碼跟內容
