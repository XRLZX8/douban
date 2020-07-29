#-*-coding:utf-8 -*-


import re
import urllib.request,urllib.response
import sys
from bs4 import BeautifulSoup
import sqlite3
import xlwt

def main():
    baseurl='https://movie.douban.com/top250?start='
    # print(baseurl)
    #爬取网页
    datalist=getData(baseurl)
    # print(datalist)
    # savepath=(".\\豆瓣电影top250.xls")
    dbpath = 'doubanmovie.db'
    saveData2db(datalist,dbpath)
    # saveData(datalist,savepath)
    # askURL('https://movie.douban.com/top250?start=')

#影片详情链接的匹配规则
findlink=re.compile(r'<a href="(.*?)">')    #全局变量,创建正则表达式对象，标识规则（字符串的模式）
#影评图片的连接
findImgSrc=re.compile(r'<img .* src="(.*?)>',re.S)#re.S表示让换行符包含在字符中
#影片片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

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
            imgSrc = imgSrc.replace('" width="100"','')
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

#得到指定一个url的网页内容
def askURL(url):
    head={#模拟头部信息
        "User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 78.0.3904.108 Safari / 537.36"
    }#用户代理，表示告诉豆瓣我们是什么类型的浏览器，本质上告诉浏览器，我们能接受什么样的数据
    request=urllib.request.Request(url,headers=head)
    html = ""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
        # print(html)
        return html
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

# def saveData(datalist,savepath):#保存数据为excel
#     book = xlwt.Workbook(encoding='utf-8')
#     sheet = book.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)
#     colom = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
#     for i in range(0,8):
#         sheet.write(0,i,colom[i])#显示每一列的名称
#     for i in range(1,251):
#         print('第%d条'%i)
#         data = datalist[i]
#         for j in range(0,8):
#             sheet.write(i+1,j,data[j])
#
#     book.save(savepath)

def saveData2db(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 3:
                data[index].replace('" width="100"','')
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movietop250(movieinfo_link,img_link,cn_name,o_name,score,rate_num,introduction,info)
            values (%s)
            '''%",".join(data)
        # print(sql)
        c.execute(sql)
        conn.commit()
    c.close()
    conn.close()

def init_db(dbpath):
    sql = '''
    create table movietop250
    (
    id integer not null primary key AUTOINCREMENT ,
    movieinfo_link text not null, 
    img_link text not null,
    cn_name varchar not null,
    o_name varchar not null,
    score numeric not null,
    rate_num numeric not null,
    introduction text not null,
    info text not null
    );
    '''#创建数据表
    conn=sqlite3.connect(dbpath)
    print('数据库创建成功')
    c = conn.cursor()
    c.execute(sql)
    print('表创建成功')
    conn.commit()
    conn.close()

if __name__=="__main__":
    main()
    # init_db('doubanmovie.db')
    print('爬取完毕')