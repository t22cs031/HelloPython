'''
Created on 2024/10/11

@author: uta
'''

print('Hello, Python world!')

#型の定義は必要ない
a = 10
b = 0.000001
c = 'string'
print(a,b,c)

for x in {1,2,3}:
    print(x)

if 0 < x < 10:
    print('0<x<10')
else:
    print('x<=0, x>=0')

p=0
while p<10:
    print('p = ',p)
    p += 1
