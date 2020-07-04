import requests,re,json

with open('./config.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

#保持图片到本地
def save_img():
    img_link=get_url_img()
    if img_link == 0:
        return 0
    content=requests.get(img_link).content
    path_img=json_data['pathImg']+'\\1.jpg'
    try:
        with open(path_img,'wb') as f:
            f.write(content)
        return {'status':'success','path':path_img}
    except:
        return {'status':'error','path':''}



#获取网页图片的链接
def get_url_img():


    html=requests.get(json_data['url'])
    if html.status_code != 200:
        print('获取网页失败')
        return 0
    #构建re正则
    r=json_data['r']
    img_url=re.findall(r,html.text)

    if(len(img_url) == 0):
        print('没找找到符合的链接')
        return 0
    img_link=json_data['url_source']+img_url[0]

    return img_link





if __name__ =='__main__':
    save_img()
