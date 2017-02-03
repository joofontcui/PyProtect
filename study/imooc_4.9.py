#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------- 
# @Time    : 2017/2/3 15:34
# @Author  : Cui jun
# @Site    : 
# @File    : imooc_4.9.py
# @Software: PyCharm
#--------------------------------------- 

class Fib(object):

    def __call__(self, num):
        a,b,l = 0,1,[]
        for i in range(num):
            l.append(a)
            a,b=b,a+b
        return l

f = Fib()
print f(10)