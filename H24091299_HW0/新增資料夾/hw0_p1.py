# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 04:06:32 2021

@author: User
"""

#提取常數
def c(x):
    pandu=0
    if x[0]=="-":
        x=x[1:]
        pandu=1
    if "*" in x:
        t=x.find("*")
        a=int(x[0:t])
        #a=常數
        b=x[t+1:]
    else :
        if x.isdigit():
            a=int(x)
            b=""
        else:
            a=1
            b=x
    if pandu==1:
        a=a*(-1)
    return[a,b]
#[a,b]=>[常數，係數]
#將格式整理x^2y=>xxy
def a(x):
    c=""
    if "^" in x:
        lst=[]
        for pos,char in enumerate(x):
            if(char == "^"):
                lst.append(pos)
        for i in lst:
            m=i
            while m+1<len(x):
                if x[m+1].isdigit():
                    m=m+1
                else:
                    break
            dig=int(x[i+1:m+1])
            for aaa in range(dig):
                c=c+x[i-1]
        for i in range(len(x)):
            tf=False
            if i+1==len(x):
                tf=True
            elif x[i+1]!="^":
                tf=True
                
            if x[i].isalpha() and tf:
                c=c+x[i]
                
        x=c
    return(x)
#確認變數是否相同會用到
def dicaaa(x):
    def a(x):
        c=""
        if "^" in x:
            lst=[]
            for pos,char in enumerate(x):
                if(char == "^"):
                    lst.append(pos)
            for i in lst:
                m=i
                while m+1<len(x):
                    if x[m+1].isdigit():
                        m=m+1
                    else:
                        break
                dig=int(x[i+1:m+1])
                for aaa in range(dig):
                    c=c+x[i-1]
            for i in range(len(x)):
                tf=False
                if i+1==len(x):
                    tf=True
                elif x[i+1]!="^":
                    tf=True
                    
                if x[i].isalpha() and tf:
                    c=c+x[i]
                    
            x=c
        return(x)
    dic={}
    sss=""
    x=a(x)
    a=set(x)
    for i in a:
        dic[i]=0
        for b in x:
            if b==i:
                dic[i]=dic[i]+1
    for i in a:
        if dic[i]==1:
            sss=sss+i
        else:
            sss=sss+i+"^"+str(dic[i])
    return dic 

#返回原格式
def jia(x):
    dic={}
    sss=""
    a=set(x)
    for i in a:
        dic[i]=0
        for b in x:
            if b==i:
                dic[i]=dic[i]+1
    for i in a:
        if dic[i]==1:
            sss=sss+i
        else:
            sss=sss+i+"^"+str(dic[i])
    return sss   
#定義乘法
def mult(x,y):
    def a(x):
        c=""
        if "^" in x:
            lst=[]
            for pos,char in enumerate(x):
                if(char == "^"):
                    lst.append(pos)
            for i in lst:
                m=i
                while m+1<len(x):
                    if x[m+1].isdigit():
                        m=m+1
                    else:
                        break
                dig=int(x[i+1:m+1])
                for aaa in range(dig):
                    c=c+x[i-1]
            for i in range(len(x)):
                tf=False
                if i+1==len(x):
                    tf=True
                elif x[i+1]!="^":
                    tf=True
                    
                if x[i].isalpha() and tf:
                    c=c+x[i]
                    
            x=c
        return(x)
    def c(x):
        if "*" in x:
            t=x.find("*")
            n=x[0:t]
            a=int(n)
            
            #a=常數
            b=x[t+1:]
        else :
            if x.isdigit():
                a=int(x)
                b=""
            else:
                a=1
                b=x
        return[a,b]
    def jia(x):
        dic={}
        sss=""
        a=set(x)
        for i in a:
            dic[i]=0
            for b in x:
                if b==i:
                    dic[i]=dic[i]+1
        for i in a:
            if dic[i]==1:
                sss=sss+i
            else:
                sss=sss+i+"^"+str(dic[i])
        return sss   
    p=c(x)
    d=c(y)
    aaa=p[0]*d[0]
    b=a(p[1])+a(d[1])
    if aaa==1 and b=="":
        c=1
    elif aaa==1:
        c=jia(b)
    elif b=="":
        c=aaa
    else:
        c=str(aaa)+"*"+str(jia(b))
    return str(c)
#將括號裡東西分開
def one(c):
    c=str(c)
    
    if "-" in c:
        st=[]
        for pos,char in enumerate(c):
                if(char == "-"):
                    st.append(pos)
        st.reverse()
        if 0 in st:
            st.remove(0)
        a=[]
        for i in st:
            a.append(c[i:])
            c=c[:i]
        a.append(c)
    else:
        a=[c]
    b=[]
    for i in a:
        if "+" in i:
            lst=[]
            for pos,char in enumerate(i):
                if(char == "+"):
                    lst.append(pos)
            lst.reverse()
            for aa in lst:
                b.append(i[aa+1:])
                i=i[:aa]
            b.append(i)
        else :
            b.append(i)
    return b
ddd=input("輸入多項式")
#去頭尾
ddd=ddd[1:len(ddd)-1]
lisss=ddd.split(")(")
ans=1
for i in lisss:
    li=one(i)
    lians=one(ans)
    b=""
    for xxx in lians:
        for zzz in li:
            zzzz=zzz
            xxxx=xxx
            if zzz[0]=="-"and xxx[0]!="-":
                b=b+"-"   
                if zzz[0]=="-":
                    zzzz=zzz[1:]
                if xxx[0]=="-":
                    xxxx=xxx[1:]
                b=b+mult(xxxx,zzzz)
            elif zzz[0]!="-"and xxx[0]=="-":
                b=b+"-"
                if zzz[0]=="-":
                    zzzz=zzz[1:]
                if xxx[0]=="-":
                    xxxx=xxx[1:]
                b=b+mult(xxxx,zzzz)
            elif zzz[0]!="-"and xxx[0]!="-":
                b=b+"+"+mult(xxx,zzz)
            elif zzz[0]=="-"and xxx[0]=="-":
                if zzz[0]=="-":
                    zzzz=zzz[1:]
                if xxx[0]=="-":
                    xxxx=xxx[1:]
                b=b+"+"+mult(xxxx,zzzz)
    if b[0]=="+":
        b=b[1:]
    ans=b
#ans=未整理答案
imp=one(ans)
amp=""
for i in imp:
    if c(i)[1]!="":
        amp=amp+a(c(i)[1])
aam=set(amp)
ttt=len(imp)
#整理重複變數並合併
final=imp[0]
x=one(final)
for i in range(1,ttt):
    xx=x
    assa=0
    for z in x:
        wac=c(imp[i])
        wab=c(z)
        wac[0]=int(wac[0])
        wab[0]=int(wab[0])
        if dicaaa(wac[1])==dicaaa(wab[1]):
            wac=[wac[0]+wab[0],wac[1]]
            assa=1
            xx.remove(z)
            if wac[0]>1 and wac[1]!="":
                xx.append(str(wac[0])+"*"+wac[1])
            elif wac[0]==1 and wac[1]!="":
                xx.append(wac[1])
            elif wac[0]==0 and wac[1]!="":
                xsxsxsxs=0
            elif wac[0]==-1 and wac[1]!="":
                xx.append("-"+wac[1])
            elif wac[0]<-1 and wac[1]!="":
                xx.append(str(wac[0])+"*"+wac[1])
            elif wac[0]==0 and wac[1]=="":
                xxxxxxwws=0
            elif wac[1]=="":
                xx.append(str(wac[0]))
            break
    if assa==0:
        xx.append(imp[i])
    x=xx
            
output=""
for i in x:
    fn=c(i)
    if fn[0]<0:
        output=output+i
    else:
        output=output+"+"+i
if output[0]=="+":
    output=output[1:]
print(output)    
        
    
