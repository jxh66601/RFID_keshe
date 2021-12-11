#! /usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import threading
from threading import Lock,Thread
import time,os
from PyQt5 import QtWidgets  # 导入相关组件
import LoginWindow  # 导入登录界面的py文件
import debugWindow  # 导入调试界面py文件
# 密码权限校验函数
def on_click(self):
    name = ui.lineEdit.text()   # 用户名
    password = ui.lineEdit_2.text() # 密码
    if name == '123':
        if password == '123':
            #message = "登陆成功"
            loginwindow.close()  # 关闭登陆窗口
            debugwindow.show()  # 打开调试界面
    #ui.textBrowser_2.setText(message)  # 登陆状态信息显示
def back():
    debugwindow.close()  # 关闭调试窗口
    loginwindow.show()  # 打开登陆界面

# 主程序运行函数*
if __name__=='__main__':
    app = QtWidgets.QApplication([])
    loginwindow = QtWidgets.QTableWidget()
    ui = LoginWindow.Ui_Form()
    ui.setupUi(loginwindow)  # 启动运行
    ui.pushButton.clicked.connect(on_click)  # 设置登陆界面按钮点击事件
    debugwindow = QtWidgets.QTableWidget()
    ui1 = debugWindow.Ui_Form1()
    ui1.setupUi(debugwindow)  # 启动运行
    ui1.pushButton.clicked.connect(back)  # 设置调试界面按钮点击事件
    loginwindow.show()

    app.exec()