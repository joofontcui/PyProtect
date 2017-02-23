#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------- 
# @Time    : 2017/2/4 11:01
# @Author  : Cui jun
# @Site    : 
# @File    : mysqlLearn.py
# @Software: PyCharm
#--------------------------------------- 

#coding=utf-8
#
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root',passwd='root')

if conn.cursor() is not '':
    print 'OK'
else:
    print 'SORRY'

conn.close()
