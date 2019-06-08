num=int(input())
words=list(input())

pinyinget_n=[]
pinyinget_v=[]
ze_n=[]
ping_n=[]
ze_v=[]
ping_v=[]

import re

poemfile = open('poem.txt',encoding='UTF-8').read()

#[汉字]{重复5-7次}[中文句号|中文逗号]
p1 = r"[\u4e00-\u9fa5]{5,7}"
pattern1 = re.compile(p1)

#编译正则表达式
result = pattern1.findall(poemfile) #搜索匹配的字符串，得到匹配列表

#打开输出文件
f=open('zzcf.txt','w+',encoding='utf-8')
for x in result:
    f.write(x) #遍历输出
    
import random
import pinyin

noun=open('freqword_n.txt',encoding='utf-8').read().split()
verb=open('freqword_v.txt',encoding='utf-8').read().split()

for i in range(len(noun)):
    pinyinget_n.append(pinyin.get(noun[i],format='numerical'))
for i in range(len(pinyinget_n)):
    a=int(pinyinget_n[i][len(pinyinget_n[i])-1])
    if a==3:
        ze_n.append(noun[i])
    elif a==4:
        ze_n.append(noun[i])
    elif a==1:
        ping_n.append(noun[i])
    elif a==2:
        ping_n.append(noun[i])
for j in range(len(verb)):
    pinyinget_v.append(pinyin.get(verb[j],format='numerical'))
for j in range(len(pinyinget_v)):
    b=int(pinyinget_v[j][len(pinyinget_v[j])-1])
    if b==3:
        ze_v.append(verb[j])
    elif b==4:
        ze_v.append(verb[j])
    elif b==1:
        ping_v.append(verb[j])
    elif b==2:
        ping_v.append(verb[j])

def writeLine1():
    global nounlist
    global verblist
    i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(ze_n)-1)
    l=random.randint(0,len(ping_n)-1)
    m=random.randint(0,len(ze_v)-1)
    n=random.randint(0,len(ping_v)-1)
    if num==4:
        if words==[]:
            print(noun[i]+verb[j][1]+ze_n[k][1])
        else:
            print(words[0]+noun[i][1]+verb[j][1]+ze_n[k][1])
    if num==5:
        if words==[]:
            print(noun[i]+verb[j][1]+noun[i][1]+ze_n[k][1])
        else:
            print(words[0]+noun[i][1]+verb[j][1]+noun[i][1]+ze_n[k][1])
    if num==7:
        if words==[]:
            print(verb[j]+noun[i]+verb[j][1]+noun[i][1]+ze_n[k][1])
        else:
            print(words[0]+verb[j][1]+noun[i]+verb[j][1]+noun[i][1]+ze_n[k][1])
    
def writeLine2():
    global nounlist
    global verblist
    i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(ze_n)-1)
    l=random.randint(0,len(ping_n)-1)
    m=random.randint(0,len(ze_v)-1)
    n=random.randint(0,len(ping_v)-1)
    if num==4:
        if words==[]:
            print(noun[i]+verb[j][1]+ping_v[n][1])
        else:
            print(words[1]+noun[i][1]+verb[j][1]+ping_v[n][1])
    if num==5:
        if words==[]:
            print(noun[i]+verb[j]+ping_n[l][1])
        else:
            print(words[1]+noun[i][1]+verb[j]+ping_n[l][1])
    if num==7:
        if words==[]:
            print(noun[i]+noun[i]+verb[j]+ping_n[l][1])
        else:
            print(words[1]+noun[i][1]+noun[i]+verb[j]+ping_n[l][1])
    
def writeLine3():
    global nounlist
    global verblist
    i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(ze_n)-1)
    l=random.randint(0,len(ping_n)-1)
    m=random.randint(0,len(ze_v)-1)
    n=random.randint(0,len(ping_v)-1)
    if num==4:
        if words==[]:
            print(noun[i]+verb[j][1]+ze_n[k][1])
        else:
            print(words[2]+noun[i][1]+verb[j][1]+ze_n[k][1])
    if num==5:
        if words==[]:
            print(noun[i]+verb[j][1]+noun[i][1]+ze_n[k][1])
        else:
            print(words[2]+noun[i][1]+verb[j][1]+noun[i][1]+ze_n[k][1])
    if num==7:
        if words==[]:
            print(verb[j]+noun[i]+verb[j][1]+noun[i][1]+ze_n[k][1])
        else:
            print(words[2]+verb[j][1]+noun[i]+verb[j][1]+noun[i][1]+ze_n[k][1])
    
def writeLine4():
    global nounlist
    global verblist
    i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(ze_n)-1)
    l=random.randint(0,len(ping_n)-1)
    m=random.randint(0,len(ze_v)-1)
    n=random.randint(0,len(ping_v)-1)
    if num==4:
        if words==[]:
            print(noun[i]+verb[j][1]+ping_v[n][1])
        else:
            print(words[3]+noun[i][1]+verb[j][1]+ping_v[n][1])
    if num==5:
        if words==[]:
            print(noun[i]+verb[j]+ping_n[l][1])
        else:
            print(words[3]+noun[i][1]+verb[j]+ping_n[l][1])
    if num==7:
        if words==[]:
            print(noun[i]+noun[k]+verb[j]+ping_n[l][1])
        else:
            print(words[3]+noun[i][1]+noun[k]+verb[j]+ping_n[l][1])
writeLine1()
writeLine2()
writeLine3()
writeLine4()


