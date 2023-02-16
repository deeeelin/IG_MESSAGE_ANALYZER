# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
from datetime import date,datetime
from typing import List,TypeVar


Box=TypeVar('Box') # a message box 's bs object 

class ig_parser:
  
    def __init__(self,roots:List[bs]) -> None:
        
        def make_box_lis(root:bs)->List[Box]:
            """parse all the box messages in the bs4 root and gather to a list"""
            tmp=[]
            for i in root.find_all("div",attrs={"class":"pam _3-95 _2ph- _a6-g uiBoxWhite noborder"}):
                tmp.append(i)
            return tmp
        
        self.box_lis=[]
        self.person= str(roots[0].find("title").string)

        for root in roots:
            self.box_lis.extend(make_box_lis(root))
        

    def get_text(self,box:Box)->str:
        """ get none-emty texts """
        
        string=box.find("div",attrs={"class","_3-95 _a6-p"}).contents[0].contents[1].string
        if not string:
            string="\n"
        #print(string)
        if string=="\n":
            string=None
        
        return string

    def get_pure_text(self,box:Box)->str:
        """get only word texts """
        

        string=box.find("div",attrs={"class","_3-95 _a6-p"}).contents[0].contents[1].string
        if not string:
            string="\n"
        #print(string)
        to_d=["\n","Audio call ended","You started an audio call","You started a video chat","Video chat ended"]
        if (string in to_d) or ("https://" in string) or ((" to your message") in string and ("Reacted " in string)):
            string=None
        
        return string


    def get_date(self,box:Box)->datetime:
        """return a datetime object : year-month-day hour:minite:00"""
        date_str=list(box.find("div",attrs={'class':"_3-94 _a6-o"}).string)
        temp=0
        for i in range(len(date_str)):
            if date_str[i]=="年": 
                
                year=int("".join(date_str[:i]))
                temp=i+1
            if date_str[i]=="月": 
                month=int("".join(date_str[temp:i]))
                temp=i+1
            if date_str[i]=="日": 
                day=int("".join(date_str[temp:i]))
                temp=i+4
            if date_str[i]==":":
                if "下" in date_str:
                    if int("".join(date_str[temp:i]))!=12:
                        hour=int("".join(date_str[temp:i]))+12
                    else:
                        hour=int("".join(date_str[temp:i]))
                else:
                    if int("".join(date_str[temp:i]))==12:
                        hour=0
                    else:
                        hour=int("".join(date_str[temp:i]))
                temp=i+1
        minit=int("".join(date_str[temp:]))
        x=datetime(year,month,day,hour,minit)
        return x
    
    def is_face(self,cur:int)->bool:
        """determine whether a pair of boxes is a video chat box,return bool"""
        if self.get_text(self.box_lis[cur+1])=="You started a video chat" and self.get_text(self.box_lis[cur])=="Video chat ended":
            return True
        else: return False

    def is_tel(self,cur:int)->bool:
        """determine whether a pair of boxes is a audio call box,return bool"""
        if self.get_text(self.box_lis[cur+1])=="You started an audio call" and self.get_text(self.box_lis[cur])=="Audio call ended":
            return True
        else: return False

    def sender(self,box:Box)->str:
        """find the sender of a box"""

        return box.find("div",attrs={"class":"_3-95 _2pim _a6-h _a6-i"}).string

    def tag_count(self,tag,att=None,func=None):
        total=0
        me=0
        cp=0
        
        for i in self.box_lis: #message for one of the person
            if att:
                f=i.find(tag,attrs=att)
            elif func :
                f=func(i)
            else:
                f=i.find(tag)

            if f==None:
                continue
            else:
                total+=1
                if self.get_person()==self.sender(i):
                    cp+=1
                else:
                    me+=1
        return [total,cp,me]
    
    def url_count(self,tag,target):
        total=0
        me=0
        cp=0
        
        for i in self.box_lis: #message for one of the person
        
            if i.find(tag):
                p=i.find(tag).string
            else :
                continue
            if not p:
                continue
            else:
                if all([i in p for i in target]):
                    if self.sender(i)==self.get_person(): cp+=1
                    else: me+=1
        total=me+cp
        return [total,cp,me]
    
    def call_count(self,t):
        count=0
        totaltime=0

        maxtime=0
        fl=[]
        for i in range(len(self.box_lis)-1):
            do=False
            if t=="tel":
                if self.is_tel(i):do=True
            
            elif t=="face":
                if self.is_face(i):do=True

            if do:
                fl.append(self.box_lis[i+1])
                count+=1
            
                late=self.get_date(self.box_lis[i])
                ear=self.get_date(self.box_lis[i+1])
            
                delt=int((late-ear).total_seconds()/60)
                totaltime+=delt
                if delt>maxtime:
                    maxtime=delt
        cp=0
        m=0
        for i in fl:
            if self.sender(i)==self.get_person():
                cp+=1
            else:
                m+=1

        return (totaltime,maxtime,count,cp,m)

    def long_short_text(self,m=1):
        """return the longest text's info that the chatroom memeber sent"""
        mlen=[0 if m==1 else 1e9,0 if m==1 else 1e9]
        mtex=["",""]
        for i in self.box_lis:
            tex=self.get_pure_text(i)
            if tex:
                texlen=len(tex)
                if self.sender(i)==self.get_person():
                    if (m*texlen>m*mlen[0]):          
                        mlen[0]=texlen
                        mtex[0]=tex
                else:
                    if (m*texlen>m*mlen[1]):
                        mlen[1]=texlen
                        mtex[1]=tex

        if m>0: mlen.insert(0,max(mlen[0],mlen[1]))
        else :mlen.insert(0,min(mlen[0],mlen[1]))

        mtex.insert(0,mtex[0] if m*len(mtex[0]) >= m*len(mtex[1]) else mtex[1] )
        return [[mtex[i],mlen[i]] for i in range(len(mtex))]

    def text_dict(self):
        text_dic=[dict(),dict(),dict(),]
        for i in self.box_lis:
            tex=self.get_pure_text(i)
            if tex:
                if self.sender(i)==self.get_person():
                    if not tex in text_dic[1]:
                        text_dic[1][tex]=1
                    else:
                        text_dic[1][tex]+=1
                else:
                    if not tex in text_dic[2]:
                        text_dic[2][tex]=1
                    else:
                        text_dic[2][tex]+=1

                if not tex in text_dic[0]:
                        text_dic[0][tex]=1
                else:
                    text_dic[0][tex]+=1
        return text_dic

    def start_end_date(self):
        def replacing(string:str)->str:
            string=string.replace("年","-")
            string=string.replace("月","-")
            return string
        datec_str=(self.box_lis[0].find("div",attrs={'class':"_3-94 _a6-o"}).string)
        datep_str=(self.box_lis[-1].find("div",attrs={'class':"_3-94 _a6-o"}).string)
        datec_str=replacing(datec_str)
        datep_str=replacing(datep_str)
        t=[]
        for i in [datec_str, datep_str]:
            ind=i.index("日")
            tmp=list(map(int,i[:ind].split("-")))
            t.append(date(tmp[0],tmp[1],tmp[2]))
        return t   
    
    def get_person(self)->str:
        """return the person whom you're chatting with"""
        return self.person

