#!/usr/bin/python3
# -- coding: utf-8 --
# @Time: 2023/6/30 10:23
# -------------------------------
# cron "0 0 6,8,20 * * *" script-path=xxx.py,tag=匹配cron用
import json, requests, os, time

yyusername = "linmuxiaoye"
yypassword = "Xf123321"

def login_sign():
    O00OOO00O0OO0OO00 = requests.session()
    OOOO000000000O0O0 = O00OOO00O0OO0OO00.post('https://api.v2.rainyun.com/user/login', headers={"Content-Type": "application/json"},
                                               data=json.dumps({"field": f"{yyusername}", "password": f"{yypassword}"}))
    if OOOO000000000O0O0.text.find("200") > -1:
        print("登录成功")
        O000OOOOO000OOO0O = OOOO000000000O0O0.cookies.get_dict()['X-CSRF-Token']
    else:
        print(f"登录失败，响应信息：{OOOO000000000O0O0.text}")
        return

    O000O0OOOO00OOOOO = {'x-csrf-token': O000OOOOO000OOO0O}
    O0O0O000OOOO0OOO0 = O00OOO00O0OO0OO00.post('https://api.v2.rainyun.com/user/reward/tasks', headers=O000O0OOOO00OOOOO,
                                               data=json.dumps({"task_name": "每日签到", "verifyCode": ""}))
    print('开始签到：签到结果 ' + O0O0O000OOOO0OOO0.text)
    print('尝试10次服务器兑换！')

    for OO00000OO0OO0000O in range(10):
        OOOO00OO000O0O000 = O00OOO00O0OO0OO00.post('https://api.v2.rainyun.com/user/reward/items', headers=O000O0OOOO00OOOOO,
                                                   data='{"item_id":107}')
        OOO0O0OO0O000O0O0 = O00OOO00O0OO0OO00.post('https://api.v2.rainyun.com/user/reward/items', headers=O000O0OOOO00OOOOO,
                                                   data='{"item_id":106}')
        print(f'第{OO00000OO0OO0000O+1}次尝试兑换云服务器 ' + json.loads(OOOO00OO000O0O000.text)['message'])
        print(f'第{OO00000OO0OO0000O+1}次尝试兑换云服务器 ' + json.loads(OOO0O0OO0O000O0O0.text)['message'])
        time.sleep(5)

if __name__ == '__main__':
    login_sign()
