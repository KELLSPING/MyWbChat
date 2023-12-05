import eel



@eel.expose  # 使函数能够被 JavaScript 调用
def say_hello_py(x):
    print(f"Hello from Python: {x}")
    return f"Hello from Python: {x}"

@eel.expose
def start_chat():
    
    # eel.init('web')  # 设置 Web 页面所在的文件夹
    eel.init('web', allowed_extensions=['.js', '.html'])
    
    # 啟動 Eel 應用，並設定視窗位置和大小
    eel.start('index.html', size=(300, 200), suppress_error=True, debug=True)



if __name__ == '__main__':
    start_chat()
