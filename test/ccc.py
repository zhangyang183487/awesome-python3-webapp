# -*- coding: UTF-8 -*-
from enum import Enum


class Student(object):
    count = 0

    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'score', '_age', 'level', 'gender');

    def __init__(self, *name, age=8, **score):
        self.name = name
        self._age = age
        self.score = score
        Student.count = Student.count + 1

    def get_age(self):
        return self._age

    def printStudent(self):
        print('%s, %d , %s' % (bart.name, bart._age, bart.score))
        return None

    def set_age(self, age):
        self.__age = age


dist_score = {'语文': 98, '数学': 88, '政治': 100}
list_name = ['包拯']
bart = Student(*list_name, 100, **dist_score)

print(bart)



# print('%s, %d , %s' % (bart.name, bart.__age, bart.score))

# print('%s, %d , %s' % (bart.name, bart.get_age(), bart.score));

# print(dir(bart));

# print(hasattr(bart, '__age'));

# print(bart.count);

bart2 = Student('小龙女');
# print(bart2.count);

print('=============');
bart.level = '高级';
# print(bart.level);

# bart.set_age = MethodType(set_age, bart);
# bart.set_age(18);
# print(bart.get_age());


print('=====================property装饰器===========================');


class Screen(object):

    def __init__(self, resolution='初始化值'):
        self._resolution = resolution;

    @property
    def width(self):
        return self._width;

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError('width must be an integer!')
        if width < 0 or width > 100:
            raise ValueError('width must between 0 ~ 100!')

        self._width = width;

    @property
    def height(self):
        return self._height;

    @height.setter
    def height(self, height):
        self._height = height;

    @property
    def resolution(self):
        return self._resolution;


obj = Screen('实例自己赋值');
obj.width = 90;
obj.height = 80;
print(obj.width);
print(obj.height);
print(obj.resolution);

print('=====================property装饰器===========================');


class Gender(Enum):
    Male = 0
    Female = 1


class Worker(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


worker = Worker('zhangsan', Gender.Male)
print(worker.name)
print(worker.gender)
