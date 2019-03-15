#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
import pickle
import json

print('=============================file open =====================================');

try:
    #f = open('aaa.py','r');

    #要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
    f = open('aaa.py', 'r', encoding='UTF-8');

    #遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理
    #f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

    print(f.read());
except FileNotFoundError as e:
    raise e;
finally:
    f.close();


with open('eee.py', 'r') as f:
    print(f.read());


with open('123.txt', 'w') as output:
    with open('eee.py', 'r') as input:
        output.write(input.read());

print('=============================file open =====================================');


print('=============================StringIO=====================================');

f = StringIO();
f.write('hello Wen');
print(f.getvalue());

print('=============================StringIO=====================================');



print('=============================pickle=====================================');

my_dict = {'A':'111', 'B':2, 'C':3}
with open('E:\\111\\123.txt','wb') as f:
    pickle.dump(my_dict, f);

with open('E:\\111\\123.txt','rb') as f1:
    d1 = pickle.load(f1);
print(d1);

print('=============================pickle=====================================');



print('=============================json=====================================');

jsonStr = json.dumps(my_dict);
print('========jsonStr=======', jsonStr);

jsonStr2 = json.dumps(my_dict, ensure_ascii=True);
print('============jsonStr2=========',jsonStr2);

dict2 = json.loads(jsonStr);
print('============dict2=========',dict2);

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88);

print('=============__dict__===================', s.__dict__);

studentJSON = json.dumps(s, default=student2dict);

print('========studentJSON======',studentJSON)

student = json.loads(studentJSON, object_hook=dict2student);

print('===========student========',student)

print('=============================json=====================================');






