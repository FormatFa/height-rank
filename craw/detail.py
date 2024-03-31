import requests
import json
import re
with open('heroList.json','r') as f:
    result=[]
    heroList = json.loads(f.read())['yzzyxs_4880']
    for hero in heroList:
        id=hero['yzzyxi_2602']
        name=hero['yzzyxm_4588']
        job = hero['yzzyxz_1918']
        print(id)
        # name
        # print(hero)
        url = 'https://pvp.qq.com/zlkdatasys/ip/hero/{}.html'.format(id)
        res = requests.get(url)
        text = res.text
        heightRe = re.search("heroHeight = '(\d+)'",text)
        # 两个身高的，取最高
        if heightRe==None:
            heightRe = re.search("heroHeight = '\d+/(\d+)'",text)
        height = 0
        if heightRe!=None:
           height = int(heightRe.group(1)     )
        else:
            print("unknow height")
        
        # print(heightRe)
        # print(res.text)
        print(name,height)
        result.append({
            "id":id,
            "name":name,
            "job":job,
            "height": height
        })
print(result)
with open('heroHeight.json','w',encoding='UTF-8') as f:
    f.write(json.dumps(result,indent=3,ensure_ascii=False))
