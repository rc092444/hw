# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:05:58 2021

@author: User
"""
#binla=>並列者
f = open("C:/Users/User/Downloads/IMDB-Movie-Data.csv")
data = f.readlines()
c=[]
for line in data:
    a=line.split(",")
    c.append(a)
#[名字，rate]
print("#1")
del c[0]
rate1=[0,0]
rate2=[0,0]
rate3=[0,0]
for a in c:
    if int(a[5])==2016:
        rate=float(a[7])
        if rate>rate1[1]:
            rate3=rate2
            rate2=rate1
            rate1=[a[1],float(a[7])]
        elif rate>rate2[1]:
            rate3=rate2
            rate2=[a[1],float(a[7])]   
        elif rate>rate3[1]:
            rate3=[a[1],float(a[7])]   
binla=[]
for a in c:
     if int(a[5])==2016:
        rate=float(a[7])
        if rate ==rate3[1] and a[1]!=rate1[0]and a[1]!=rate2[0]and a[1]!=rate3[0]:
            binla.append(a[1])
            
print("1:",rate1[0],"2:",rate2[0],"3:",rate3[0])
if binla!=[]:
    print("並列:",binla)
#2
print("#2")
actr=[]
for a in c:
    actor=a[4].split("|")
    for i in actor:
        if i.lstrip() not in actr:
            actr.append(i.lstrip())  
e=[]
ar={}
#[revenue總和,個數]
for i in actr:
    ar[i]=[0,0]
for a in c:
    if a[9]!="":
        actor=a[4].split("|")
        for i in actor:
           e.append(i.lstrip())  
        for i in e:
            p=ar[i]
            p[0]=p[0]+float(a[9])
            p[1]=p[1]+1
            ar[i]=p
    e=[]        
ma=0
for i in actr:
    p=ar[i]
    if p[1]!=0:
        ffff=p[0]/p[1]
    if ffff>ma:
        ma=ffff
        g=i
binla=[]
for i in actr:
    p=ar[i]
    if p[1]!=0:
        ffff=p[0]/p[1]
    if ffff==ma and i!=g:
        binla.append(i)
print(g)
if binla!=[]:
    print("並列:",binla)
#3
print("#3")
rat=[0,0]
#[rating總和,個數]
for a in c:
    if  "Emma Watson" in a[4]:
        rat[0]=rat[0]+float(a[7])
        rat[1]=rat[1]+1
print(rat[0]/rat[1])        
#4
print("#4")
daoyan=set()
for a in c:
    daoyan.add(a[3].lstrip())
colla={}
for i in daoyan:
    colla[i]=set()
for a in c:
    i=a[3].lstrip()
    p=colla[i]
    e=[]
    actor=a[4].split("|")
    for abc in actor:
        e.append(abc.lstrip()) 
    p=set(p) | set(e)
    colla[i]=p
colla1=[0,0]
colla2=[0,0]
colla3=[0,0]
#[名字，總數]
for i in daoyan:
    x=colla[i]
    num=len(x)
    if num>colla1[1]:
        colla3=colla2
        colla2=colla1
        colla1=[i,num]
    elif num>colla2[1]:
        colla3=colla2
        colla2=[i,num]   
    elif num>colla3[1]:
        colla3=[i,num] 
binla=[]
for i in daoyan:
    x=colla[i]
    num=len(x)
    if num==colla3[1]and i!=colla1[0]and i!=colla2[0] and i!=colla3[0]:
        binla.append(i)
print(colla1,colla2,colla3)   
if binla!=[]:
    print("並列:",binla) 
#5
print("#5")
genre={}
for i in actr:
    genre[i]=set()
for a in c:
    e=[]
    
    actor=a[4].split("|")
    for abc in actor:
        e.append(abc.lstrip()) 
    gen=a[2].split("|")
    for i in e:
        p=genre[i]
        p=p|set(gen)
        genre[i]=p
genre1=[0,0]
genre2=[0,0]
#[名字，總數]
for key in genre:
    x=genre[key]
    num=len(x)
    if num>genre1[1]:
        genre2=genre1
        genre1=[key,num]
    elif num>genre2[1]:
        genre2=[key,num]
binla=[]
for key in genre:
    x=genre[key]
    num=len(x)
    if num==genre2[1]and key!=genre1[0]and key!=genre2[0]:
        binla.append(key)
print(genre1,genre2)
if binla!=[]:
    print("並列:",binla) 
#6
print("#6")
year={}
for i in actr:
    year[i]=[0,9999]#[最大年分，最小年分]
for a in c:
    e=[]
    actor=a[4].split("|")
    for abc in actor:
        e.append(abc.lstrip()) 
    for i in e:
        p=year[i]
        if int(a[5])>p[0]:
            p[0]=int(a[5])
        if int(a[5])<p[1]:
            p[1]=int(a[5])
        year[i]=p
#[名字，gap]
gap1=[0,0]
gap2=[0,0]
gap3=[0,0]
for i in actr:
    x=year[i]
    num=x[0]-x[1]
    if num>gap1[1]:
        gap3=gap2
        gap2=gap1
        gap1=[i,num]
    elif num>gap2[1]:
        gap3=gap2
        gap2=[i,num]   
    elif num>gap3[1]:
        gap3=[i,num] 
binla=[]
for key in year:
    x=year[key]
    num=x[0]-x[1]
    if num==gap3[1]and key!=gap1[0]and key!=gap2[0]and key!=gap3[0]:
        binla.append(key)
        
print(gap1,gap2,gap3)
if binla!=[]:
    print("並列:",binla) 
#7
print("#7")
ans=set(["Johnny Depp"])
def dee(ans):
    for a in c:
        e=[]
        actor=a[4].split("|")
        for abc in actor:
            e.append(abc.lstrip()) 
        for i in e:
            if i in ans:
                ans=ans|set(e)
    return ans
le=len(ans)
while le!=len(dee(ans)):
    le=len(dee(ans))
    ans=dee(ans)

print(ans)

