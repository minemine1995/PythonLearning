# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:45:03 2020

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:06:05 2020

@author: Yenny

如果你没有安装xlwt

请先 'pip install xlw' 安装库
"""

# 导入xlwt库
import xlwt

# 定义workbook
workbook = xlwt.Workbook() 

# 添加sheet，这个sheet的名字叫'Border'
sheet = workbook.add_sheet('Border')  

# 设置样式格式
def SetStyle(name,color,height,bold,italic,underline,struck_out,horz):
    
    # 初始化样式
    style = xlwt.XFStyle()  
    
    # 字体设置
    font = xlwt.Font()  
    font.name = name  # 设置字体    
    font.colour_index = color # 设置字体颜色
    font.height = height # 字体大小    
    font.bold = bold # 是否为粗体    
    font.italic = italic # 字体是否斜体    
    font.underline = underline # 是否有下划线    
    font.struck_out = struck_out # 字体中是否有横线
    
    # 位置设置
    al = xlwt.Alignment()
    al.horz = horz      # 设置水平位置，0是左对齐，1是居中，2是右对齐
    # al.vert = 0x01      # 设置垂直位置
    
    # 设置边框
    borders = xlwt.Borders() # Create Borders
    # DASHED虚线
    # NO_LINE没有
    # THIN实线
    borders.left = xlwt.Borders.DASHED 
    borders.right = xlwt.Borders.DASHED 
    borders.top = xlwt.Borders.DASHED 
    borders.bottom = xlwt.Borders.DASHED 
    borders.left_colour = color
    borders.right_colour = color
    borders.top_colour = color
    borders.bottom_colour = color

    style.font = font
    style.alignment = al
    style.borders = borders 
    
    return style

# 写入数据
row = 0 # 行
column = 0 # 列
for i in range(72): 
    if i < 27:        
        sheet.write(row, column, i, SetStyle('Times New Roman',i,400,False,False,False,False,1)) 
    elif i<54:
        sheet.write(row, column, i, SetStyle('Times New Roman',i,400,False,False,False,False,1)) 
    else:
        sheet.write(row, column, i, SetStyle('Times New Roman',i,400,False,False,False,False,1))     
    column += 1
    if column > 8:
        column = 0
        row += 1
        
# 定义保存Excel的位置
workbook.save('Border.xls')