#! /usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(1,11):
    print "Tabla del ",i
    print "--------------"
    for j in range(1,11):
    	num=i*j
    	print '%d por %d es %d ' % (i,j,num)