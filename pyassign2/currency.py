# -*- coding: utf-8 -*-
"""
#currency exchange
#author 邓泽宇 Deng Zeyu 1700013234
#2017.12.11
@author: dzy1700013234
'Module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.'"""

from urllib.request import urlopen
#exchange function#
def exchange(currency_from,currency_to,amount_from):            #the exchange function
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+str(currency_from)+'&to='+str(currency_to)+'&amt='+str(amount_from)
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    newdoc=docstr.decode(encoding='UTF-8')                      #set the decoding rule
    a=newdoc.split(':')[2]
    b=a.split()[0]
    amt_to=float(b[1:])
    return amt_to

#test function 1#
def test_input():
    "Verify that the input value is reasonable"
    assert(len(cur_from)==3)
    assert(len(cur_to)==3)
    assert(cur_from.isalpha())                                  #test if the cur_from and cur_to are letters#
    assert(cur_to.isalpha())
    assert(float(amt_from)>0)
    print("test_input pass")

#test function 2#
def test_output():
    "Verify that the input value is reasonable"
    amt_to=exchange(cur_from,cur_to,amt_from)
    assert(type(amt_to)==float)
    print("test_output pass")

#test function 3#
#select three different value to test if the output value is right#
def test_value():
    "Verify that the value is right"
    assert(exchange("USD","EUR",2.5)==2.0952375)
    assert(exchange("CNY","JPY",100)==1668.0366747623)
    assert(exchange("CNY","TWD",100)==460.87279636539)
    print("test_value pass")

#input the test value#
cur_from=input("enter the test cur_from ")
cur_to=input("enter the test cur_to ")
amt_from=input("enter the test amt_from ")

def test_all():
    "test all functions"
    test_input()
    test_output()
    test_value()
    print("all tests pass")
    
test_all()

#input the value need to exchange#
currency_from=input("enter the currency you have ")
currency_to=input("enter the currency you want to exchange for ")
amount_from=input("enter the amount you have ")

#the exchange result#
print(exchange(currency_from,currency_to,amount_from))