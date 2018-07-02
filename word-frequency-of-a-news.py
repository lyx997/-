
# coding: utf-8

# In[10]:


import jieba
import pyecharts
import jieba.analyse
text = """
麦克斯韦电磁理论经验定律包括：
静电学的库仑定律，涉及磁场的定律，关于电流的磁场的安培定律，法拉第电磁感应定律。
麦克斯韦把这四个定律予以综合，导出麦克斯韦方程，该方程组系统而完整地概括了电磁场的基本规律，
并预言了电磁波的存在。麦克斯韦提出的涡旋电场和位移电流假说的核心思想是：变化的磁场可以激发涡旋电场，
变化的电场可以激发涡旋磁场；电场和磁场不是彼此孤立的，它们相互联系、相互激发组成一个统一的电磁场。
下面我们通过制作感应天线体，来验证电磁场的存在。如图所示：电偶极子是一种基本的辐射单元，
它是一段长度远小于波长的直线电流元，线上的电流均匀同相，一个作时谐振荡的电流元可以辐射电磁波，
故又称为元天线，元天线是最基本的天线。电磁感应装置的接收天线可采用多种天线形式，相对而言性能优良，
但又容易制作，成本低廉的有半波天线、环形天线、螺旋天线等。 
"""

word_list = jieba.lcut(text)
# print(word_list)

extract_tags = jieba.analyse.extract_tags(text) 
print(extract_tags)

word_dict = {}
for word in word_list:
    if word in extract_tags:
        word_dict[word] = word_dict.get(word, 0) + 1
print(word_dict)

chart = pyecharts.WordCloud("...")
chart.add("", word_dict.keys(), word_dict.values(), word_size_range = [15, 100], rotate_step = 30)
chart

