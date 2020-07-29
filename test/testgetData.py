def getData(baseurl):#获取数据
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        # print(url)
        html = askURL(url)
        #2.逐一解析数据
        soup =BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_="item"):#查找符合要求的字符串，形成列表
            # print(item)
            data=[]#保存一部电影的全部信息
            item=str(item)

            #获取影片详情的连接
            link = re.findall(findlink,item)[0]#re库用来通过正则表达式来查找(在item中查找符合findlink规则的）
            # print(link)
            data.append(link)#开始向data列表中添加信息

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)#片名可能只有一个中文名，也可能同时有中文和外文名
            if len(titles)==2:
                c_title = titles[0]#添加中文名
                data.append(c_title)
                otitle = titles[1].replace('/','')
                data.append(otitle)#添加外国名
            else:
                data.append(titles[0])
                data.append(' ')#没有外文名要留空

            rating = re.findall(findRating,item)[0]#添加评分
            data.append(rating)

            judge = re.findall(findJudge,item)[0]#添加评价人数
            data.append(judge)

            inq = re.findall(findInq,item)#添加概述,但概述可能没有
            if len(inq)!=0:
                inq = inq[0].replace('。','')#去掉句号
                data.append(inq)
            else:
                data.append(' ')#留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?>(\s+?)',' ',bd)#去掉<br>
            bd = re.sub('/',' ',bd)#替换/
            data.append(bd.strip())#去掉前后空格

            datalist.append(data)#把处理好的一部电影信息放入datalist
    # print(datalist)
    return datalist