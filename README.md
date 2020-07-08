# [网络]基于python的自定义时间、网站、一键更换桌面壁纸



## 相关依赖

+ ### python>3.6

+ ### requests(pip install requests)





## 配置信息（config.json）

+ ### time

  +  ### 自定义时间 ： "time": "12"；在每天12内随机更换

+ ### url_source

  + ### 图片的源地址 ，类似网址不带后缀

+ ### url

  + ### 网站地址

+ ### r

  + ### 正则表达式（可自定义正则，匹配图片）

+ ### pathImg

  + ### 图片存放路径，建议放绝对地址，相对路径可能会报错!  (示例：C:\\\Desktop\\\img  ;  命令后缀已写死1.jpg）





```config
{
  "time": "12",
  "url_source": "https://cn.bing.com/",

  "url": "https://cn.bing.com/?FORM=BEHPTB&ensearch=1",

  "r": "<link id=\"bgLink\" rel=\"preload\" href=\"(.*?)\" as=\"image\"",

  "pathImg":"E:\\desktopWallpaper"

}
```



## 代码扩展

+ ### 支持不同网站图片，只需构建正则即可

+ ### 支持拓展多图片幻灯片替换（需要重写requestImg模块下的get_img方法）

+ ### 自由度高，可重写





## 爬取说明

+ ### 默认网站爬取为公开内容，若网站不允许相关爬取图片，使用产生的任何问题与本开源提供方无关

+ ### 允许自由拓展、增设、改查



## 时间

+ ### 2020-7-4-----小健