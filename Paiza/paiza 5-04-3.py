# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:28:13 2018

@author: tayak
"""

# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for point in points:
    sum=sum+points[point]

print(int(sum))

