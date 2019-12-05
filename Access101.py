# -*- coding:utf-8 -*-
import os
class tools:
    def __init__(self):
        pass
    def show_menu(self):
        print("*" * 60)
        print("歡迎使用【昆盈共享文件】")
        print("")
        print("1.進入101")
        print("2.進入mis$")
        print("3.進入misiso$ (說明:權限問題,切換時需要等待時間)")
        print("")
        print("0.退出系統")
        print("*" * 60)

tool = tools()
while True:
    tool.show_menu()
    action_str = input("請選擇操作功能(1,2,3,0):")
    if action_str in ["1","2","3"]:
        if action_str == "1":
            os.system("net use * /del /y")
            os.system("net use \\\\172.20.100.55 Aa123456! /user:12012345")
            os.system("start \\\\172.20.100.55\\101")
            os.system("cls")
        elif action_str == "2":
            os.system("net use * /del /y")
            os.system("net use \\\\172.20.100.55 hj57897! /user:12057897")
            os.system("start \\\\172.20.100.55\\mis$")
            os.system("cls")

        elif action_str == "3":
            os.system("net use * /del /y")
            os.system("net use \\\\172.20.100.55 tt848714! /user:12036378")
            os.system("start \\\\172.20.100.55\\misiso$")
            os.system("cls")
    elif action_str == "0":
        break
    else:
        print("輸入錯誤,請重新輸入")
            #os.system("net use \\\\172.30.17.86\\software")
            #os.system("start \\\\172.30.17.86\\software")
