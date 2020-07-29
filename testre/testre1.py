import re


#正则表达式：字符串模式 （判断字符串是否符合标准）

pat = re.compile('AA')#此处的AA是正则，用来验证其他字符串
# m = pat.search('SERFASEWFAAadwdAAADWDWADAAAA')#只会找到第一个符合标准的字符串
# print(m)
#search方法进行比对查找，1.通过compile生成对象，2.操作对象查找

#没有模式对象时
# m=re.search('asd','awdadasgawdasdadsadad')#第一个是模版
# print(m)


#
# list=re.findall("","1231124adwdghsrh sfdawd  as")#findall输出列表#第一个字符串是规则（正则），第二个字符串是被校验字符串
# print(list)

#sub
print(re.sub('a',"A",'awawdadhsfaw'))#3个参数#参数1：被替换对象 ；参数2：替换对象；参数3：进行替换的对象
                                        #将字符串中的a替换为A
#建议在正则表达式中，被比较的字符串前面加上'r'，从而不用担心转义字符的问题
#如："\adwadasdawd",不在前面加r,会把\a看做转义字符，应该写为r"\adwadasdawd"


