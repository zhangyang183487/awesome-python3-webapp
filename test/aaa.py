#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('''aaa
bbb
ccc''');

str = 'holle' \
      'new' \
      'world'
print(str)

print('==================');

print(r'aa\nbb');

print();

print('\u5f20\u626c');

print();
chartStr = '李必填'.encode('utf-8');
print(chartStr);

print();
msg = 'hello, %s %s' % ('my', 'girl');
print(msg);

print();
classmates = ['王朝', '马汉', '张龙', '赵虎'];
print(classmates);
print(len(classmates));
print(classmates[0]);  # 正数第一个
print(classmates[-1]);  # 倒数第一个

classmates.append('包拯');
print(classmates);

classmates.insert(0, '展昭');
print(classmates);

classmates.pop();
print(classmates);

print();

sum = 'hello: ';
for x in classmates:
    sum = sum + x
print(sum)

print();
names = {'老大': 98, '老二': 88, '老三': 78};
print(names)


def my_max(x, y):
    if isinstance(x, str):
        raise TypeError('bad operand type')
    return max(x, y)


print(my_max(12, 11))


def reg_student(name, address, age=8, city='西安'):
    print('name: ', name)
    print('address: ', address)
    print('age: ', age)
    print('city: ', city)

    return None


print(reg_student('张三', '莲湖区的娃娃'))
print(reg_student('张三', '莲湖区的娃娃', 12, '陕西'))

print()
L = list(range(20))
print(L)
print(L[0:10])
print(L[-10:-1])
print(L[0:10:2])
print(L[::2])

print('=========迭代============')

my_list = list(range(10))
for v in my_list:
    print(v)

print()
my_dict = {'A': 1, 'B': 2, 'C': 3}
for key in my_dict:
    print(key)

print()
for value in my_dict.values():
    print(value)

print()
for k, v in my_dict.items():
    print('key=', k, 'value=', v)

print('=========迭代============')


def findMinAndMax(inputList):
    if len(inputList) == 0:
        raise TypeError('空集合')

    max_v = 0
    min_v = 0
    for value in inputList:
        print(isinstance(value, int))
        max_v = max(max_v, value)
        min_v = min(min_v, value)

    # max_v = max(inputList);
    # min_v = min(inputList);

    return (max_v, min_v);


print(findMinAndMax(list(range(10))))

# print(findMinAndMax(list()))


print('================列表生成式=====================')

list2 = [x for x in my_list if (x % 10) == 0 and (x > 0)]
print(list2)

print('================列表生成式=====================')

print('================可变参数=====================')


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


list3 = {1, 2, 4, 5, 12}
print(calc(*list3))

my_dict02 = {'A': 4, 'B': 5, 'C': 6}


def calc2(**numbers):
    sum = 0
    for value in numbers.values():
        sum = sum + value * value
    return sum


print('======calc2======', calc2(**my_dict02))


def calc3(*numbers, **dicts):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    for x in dicts.values():
        sum = sum + x
    return sum


 #print('======calc3======', calc3(*list3, **my_dict02))


print('================可变参数=====================')
