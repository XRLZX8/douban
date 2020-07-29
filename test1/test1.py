#BS4测试


from bs4 import BeautifulSoup

file = open('./baidu.html','rb')
html = file.read()
bs = BeautifulSoup(html,'html.parser')#不同类型的文件可以换不同解析器，支持xml,json...
# print(bs.title)
# print(bs.a)

#1.Tag   标签及其内容，只能拿到它所拿到的第一个内容
# print(bs.title.string)
# print(type(bs.title.string))
#2.NavigableString   标签里的内容（字符串）


# print(bs.a.attrs)


#print(type(bs))
#3.BeautifulSoup  表示整个文档
# print(bs)

# print(bs.a.string)
# print(type(bs.a.string))
#4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号


#-------------------------------------
#节点获取
#文档的遍历

# print(bs.head.contents)
#

#文档的搜索
#(1) find_all()
#字符串过滤：会查找与字符串完全匹配的内容
# t_list=bs.find_all("a")
# print(t_list)

import re
#（2）正则表达式搜索：使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))

#(3)方法：传入一个函数，根据函数的要求来搜索

# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)

# print(t_list)

#2.kwargs   参数

# t_list = bs.find_all(id='head')
# t_list = bs.find_all(class_=True)
#
# for i in t_list:
#     print(i)
#
#3.test参数
# t_list =bs.find_all(text="hao123")
# t_list = bs.find_all(re.compile("\d")#应用正则表达式来查找包含特定文本的内容




#4.limit参数  在获取的信息中进行个数限定
# t_list = bs.find_all("a",limit=3)
#
# for i in t_list:
#     print(i)
#

#5.css选择器
# t_list = bs.select('title')#通过标签查找
# t_list = bs.select('.mnav')#通过类名查找，. 代表class
# t_list = bs.select('#u1')#通过id查找
# t_list = bs.select("a[class='bri']")#通过属性查找
# t_list = bs.select("head > title")#通过子标签查找，查找head中的title
t_list = bs.select(".mnav~.bri")
print(t_list[0].get_text())
# for i in t_list:
#     print(i)