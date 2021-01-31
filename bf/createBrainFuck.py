import os
import math

if os.path.exists("./hoge2.bf"):
    os.remove("hoge2.bf")

s = input()
array= [] #文字siのascii
for si in s:
    array.append(ord(si))

f = open("hoge2.bf", "w")

MAX = 0
for ai in array:
    if MAX < ai:
        MAX = ai

list = [] #差分

#iの決め打ち
for i in range(MAX):
    if i == 0:
        continue
    sum = i 
    for ai in array:

        r1 = ai // i
        r2 = (ai + i) // i

        if ai - r1 * i > r2 * i - ai:
            r = r2 * i - ai
            sum += r2
        else :
            r = ai - r1 * i
            sum += r1

        sum = sum + r
        list.append(sum)

m = 10000000000
for i in range(len(list)):
    #print(li)
    li = list[i]
    if m > li:
        #print(li)
        m = li
        std = i

#ループを回す回数
for i in range(m):
    f.write('+')

flag = []
#ループ中身
f.write('[')
for ai in array:
    r1 = ai // m 
    r2 = (ai + m) // m 
    f.write('>')

    if ai - r1 * m > r2 * m - ai:
        flag.append(-(r2 * m - ai))
        for j in range(r2):
            f.write('+')

    else:
        flag.append(ai - r1 * m)
        for j in range(r1):
            f.write('+')


#ポインタをループカウンタに戻す
for i in range(len(array)):
    f.write('<')
f.write('-')
f.write(']')

#端数を処理する
for i in range(len(array)):
    
    f.write('>')
    if flag[i] < 0:
        for j in range(-flag[i]):
            f.write('-')
    else:
        for j in range(flag[i]):
            f.write('+')
    f.write('.')

#改行する
f.write('>++++++++++++.')
f.close()