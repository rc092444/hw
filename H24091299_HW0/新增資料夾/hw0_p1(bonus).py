# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 04:06:32 2021

@author: User
"""
def bonus(x):
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
    ddd=x[1:len(x)-1]
    lisss=ddd.split(")(")
    xxx="("
    for i in lisss:
        ap=one(i)
        for z in ap:
            xn=len(z)
            y=0
            cout=0
            while y==0 and cout<xn:
                aa=cout
                if z[aa].isalpha() and z[0]!="-"and z[0].isdigit():
                    z=z[:aa]+"*"+z[aa:]
                    y=1
                if z[aa].isalpha() and z[0]=="-"and z[1].isdigit():
                    z=z[:aa]+"*"+z[aa:]
                    y=1
                cout=cout+1
            xn=len(z)
            for aa in range(0,xn-1):
                if z[aa].isalpha() and z[aa+1].isdigit():
                    z=z[:aa+1]+"^"+z[aa+1:]
            if z[0]!="-":
                xxx=xxx+"+"+z
            else :
                xxx=xxx+z
        xxx=xxx+")("
    xxx=xxx+")"
    xxx=xxx[:len(xxx)-2] 
    for i in range(len(xxx)-1):
        if xxx[i]=="(" and xxx[i+1]=="+":
            xxx=xxx[:i+1]+xxx[i+2:]
            break
    for i in range(len(xxx)-1):
        if xxx[i]=="(" and xxx[i+1]=="+":
            xxx=xxx[:i+1]+xxx[i+2:]
            break
        
    for i in range(len(xxx)-1):
        if xxx[i]=="(" and xxx[i+1]=="+":
            xxx=xxx[:i+1]+xxx[i+2:]
            break
    for i in range(len(xxx)-1):
        if xxx[i]=="(" and xxx[i+1]=="+":
            xxx=xxx[:i+1]+xxx[i+2:]
            break
    for i in range(len(xxx)-1):
        if xxx[i]=="(" and xxx[i+1]=="+":
            xxx=xxx[:i+1]+xxx[i+2:]
            break
    return xxx     
    
        
print(bonus("(x+2y)(2x2-y2+z)"))
#????????????
def c(x):
    pandu=0
    if x[0]=="-":
        x=x[1:]
        pandu=1
    if "*" in x:
        t=x.find("*")
        a=int(x[0:t])
        #a=??????
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
#[a,b]=>[???????????????]
#???????????????x^2y=>xxy
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
#?????????????????????????????????
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

#???????????????
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
#????????????
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
            
            #a=??????
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
#????????????????????????
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
axa=int(input("1:?????????2:bonus"))

ddd=input("???????????????")
if axa==2:
    ddd=bonus(ddd)
#?????????
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
#ans=???????????????
imp=one(ans)
amp=""
for i in imp:
    if c(i)[1]!="":
        amp=amp+a(c(i)[1])
aam=set(amp)
ttt=len(imp)
#???????????????????????????
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
if axa==1:
    print(output)    
if axa==2:
    characters = "*^"

    string = ''.join( x for x in output if x not in characters)
    print(string)
        
    
