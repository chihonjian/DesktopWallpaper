import ctypes,requestsImg,time,json,encodefix

with open('./config.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

print("启动成功")

#初次启动执行一次
res=requestsImg.save_img()
#判断状态
if res['status'] == 'error':
    print('图片获取失败')
else:
    img_path=res['path']
    #系统API
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0) # 设置桌面壁纸
        print('更换壁纸成功')
    except:
        print('无法调用系统API，请重试')


#模块
while(True):
    time_hms=time.strftime("%H", time.localtime())
    if time_hms == json_data['time']:
        res=requestsImg.save_img()
        #判断状态
        if res['status'] == 'error':
            print('图片获取失败')
        else:
            img_path=res['path']
            #系统API
            try:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0) # 设置桌面壁纸
                print('更换壁纸成功')
            except:
                print('无法调用系统API，请重试')
                
    min=time.strftime("%H:%M:%S", time.localtime())
    print('当前时间:'+min)
    time.sleep(1800)
