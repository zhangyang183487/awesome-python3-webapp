# import logging
# logging.basicConfig(level=logging.INFO)
import pdb
from collections import Counter
from collections import deque
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('%s --> %s' % (p.x, p.y))
for n in p:
    print(n)

ddd = deque([x for x in range(1, 10)])
ddd.append(10)
print(ddd.pop())
print(ddd)

c = Counter({'a': 4, 'b': 2})
print(c)

s = '0'
pdb.set_trace()
n = int(s)
print('n = %d' % n)
# logging.info('n = %d' % n);
