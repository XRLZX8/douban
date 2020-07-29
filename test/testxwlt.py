#-*-coding:utf-8 -*-
import xlwt

# workbook = xlwt.Workbook(encoding='utf-8') #创建workbook对象
# worksheet = workbook.add_sheet('sheet1')#创建工作表
# worksheet.write(0,0,'hello') #写入数据，第一个参数：‘行’，第二个参数‘列’，第三个参数：内容
# workbook.save('student.xls')
#

#九九乘法表
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('99')

for k in range(1,10):#列
    for i in range(1,10):#行
        if k<=i:
            x=i*k
            worksheet.write(i,k,str(k)+'x'+str(i)+'='+str(x))

workbook.save('九九乘法表.xls')
