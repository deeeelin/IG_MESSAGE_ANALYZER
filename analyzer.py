
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
from typing import List,TypeVar,Tuple
from tabulate import tabulate

import sys
from parse import ig_parser
import os 

class analyzer:
    def __init__(self,path) -> None:
        def make_root(path:str)->bs:
            """create the root bs4 object of a html """
            data=open(path,mode='r',encoding='utf-8')
            root=bs(data.read(),"html.parser")
            return root
    
        def sort_key(f):
            return int(f[f.index("_")+1:f.index(".")])
        
        tmp=[f for f in os.listdir(path) if (("message_" in f) and (".html" in f))]

        tmp.sort(key=sort_key)

        root_lis=[]

        for i in tmp:
            root_lis.append(make_root(path+i)) # if root=None is outside the function as a global variable,python will let this root inside the function as a local variable
        
        self.parser = ig_parser(root_lis)


    def all_message_count(self)->List[int]: #all of the message
        """return the number of message chatroom members sent"""
        return self.parser.tag_count("div")

    def image_count(self)->List[int]:
        """return the numbers of image that chatroom members sent"""
        return self.parser.tag_count("img")

    def audio_count(self)->List[int]:
        """return the numbers of audio that chatroom members sent"""
        return self.parser.tag_count("audio")

    def react_count(self)->List[int]:
        """counts reacts that the chatroom member sent"""
        return self.parser.tag_count("ul",att={"class":"_a6-q"})
        
    def person_info_count(self)->List[int]:
        """counts person info shared that the chatroom member sent"""
        return self.parser.url_count("a",["https://www.instagram.com/_u/"])
        
    def share_post_count(self)->List[int]:
        """counts post shared that the chatroom member sent"""
        return self.parser.url_count("a",["https://www.instagram.com/p/","?feed_type=reshare_chaining"])
    
    def story_count(self)->List[int]:
        """counts story reply that the chatroom member sent"""
        return self.parser.url_count("a",["https://instagram.com/stories/"])

    def teltime(self)->(Tuple[int]):
        """return the information of audio call from chatroom members"""
        return self.parser.call_count("tel")

    def facetime(self)->(Tuple[int]):  
        """return the information of video chat from chatroom members"""
        return self.parser.call_count("face")

    def text_count(self)->int:
        """count text sent by chatroom members"""
        return self.parser.tag_count("div",func=self.parser.get_pure_text)
    
    def precise_day(self)->int:
        """return the number of days that have a chat"""
        days=[]
        for i in self.parser.box_lis:

            day=str(self.parser.get_date(i))[:-9]

            days.append(day)
        
        return len(set(days))
        
    def rough_day(self)->List[int]: #could be upgrade,consider time inside to be more specific
        """return the days between the first date of chat and the last chat's date """
        t=self.parser.start_end_date()
        d=(t[0]-t[1]).days
        return d if d!=0 else 1

    def average_message(self)->List[list]: 
        """return the average number of text that chatroom members sent everyday,with precise and rough"""
        ans=[[],[]]
        for i in self.text_count():
            rd=self.rough_day()
            pd=self.precise_day()
            ans[0].append(round(i/(rd if rd!= 0 else 1),2))
            ans[1].append(round(i/(pd if pd!= 0 else 1),2))

        return ans

    def chat_per(self)->float: 
        """return the percentage of the days that have chat """
        return self.precise_day()/self.rough_day() if self.rough_day() >0 else 1

    def longest_text(self)->list:
        """return the longest text's info that the chatroom memeber sent"""
        return self.parser.long_short_text(1)

    def shortest_text(self)->tuple:
        """return the shortest text's info that the chatroom memeber sent"""
        return self.parser.long_short_text(-1)
    
    def av_textlen(self):
        """retrun average len of tex that chatroom member sent"""
        texts=[i for i in self.text_count()]
        textlen=[0,0,0]
        
        for i in self.parser.box_lis:
            tex=self.parser.get_pure_text(i)
            if tex:
                if self.parser.sender(i)==self.parser.get_person():
                    textlen[1]+=len(tex)
                
                else:
                    textlen[2]+=len(tex)
                textlen[0]+=len(tex)

        for i in range(len(texts)):
            texts[i]=round(textlen[i]/texts[i],2)
        return tuple(texts)

    def mantra(self)->list:
        """return the mantra info of the chatroom members"""
        text_dic=self.parser.text_dict()
        ans=[]
        for _ in text_dic:
            mx=0
            mxstr=""
            for i in _.keys():
                if _[i]>mx:
                    mx=_[i]
                    mxstr=i
            ans.append([mxstr,mx])

        return ans

    def tex_sets(self):
        """return the number of different text that a chatroom member have said,and the percentage of repeating a message"""
        
        total=[i for i in self.text_count()]
        text_dic=self.parser.text_dict()

        ans=[]
        for i in range(len(text_dic)):
            temp=len(text_dic[i].keys())
            ans.append([temp,round( (1-(temp/total[i])) *100 , 2) ])
            
        ans=[[i[0] for i in ans],[i[1] for i in ans]]
        return ans

    ###################output zone#####################################################################
    def debug(self):
        print("chat_person:",self.parser.get_person())
        print("all_message_count",self.all_message_count())
        print("image_count",self.image_count())
        print("audio_count",self.audio_count())
        print("react_count",self.react_count())
        print("person_info_count",self.person_info_count())
        print("share_post_count",self.share_post_count())
        print("story_count",self.story_count())
        print("text_count",self.text_count())
        print("rough_day",self.rough_day())
        print("average_message",self.average_message())
        print("chat_per",self.chat_per())
        print("longest_text",self.longest_text())
        print("shortest_text",self.shortest_text())
        print("av_textlen",self.av_textlen())
        print("mantra",self.mantra())
        print("tex_sets",self.tex_sets())
        print("facetime",self.facetime())
        print("teltime",self.teltime())
        return 

    def print_report(self):
        p=self.parser.get_person()

        sys.stdout=open(os.path.dirname(__file__)+"/text.txt","w")  
        to_print=[]
        
        to_print.append(["chat_person: "+p])
        
        count_description={
            """
            Total amount of messages sent :
            """: self.all_message_count(),
            """
            Amount of images sent :
            """:self.image_count(),
            """
            Amount of audios sent :
            """:self.audio_count(),
            """
            Amount of reactions sent :
            """:self.react_count(),
            """
            Amount of other's personal profiles shared :
            """:self.person_info_count(),
        """
            Amount of posts shared :
            """:self.share_post_count(),
            """
            Amount of stories replied :
            """:self.story_count(),
            """
            Amount of text messages sent :
            """:self.text_count(),
            """
            Average length of every text message :
            """:self.av_textlen(),
            """
            Average amount of message sent everyday :
            """:self.average_message()[0],
            """
            Average amount of message sent for every chat day (Only considering the days that we sent message) :
            """:self.average_message()[1],
            """
            Amount of different text mentioned :
            """:self.tex_sets()[0],
            """
            Percentage of repeating a same text :
            """:self.tex_sets()[1],
            """
            Amount of facetime chats:
            """:self.facetime()[2:],
            """
            Amount of audio chats:
            """:self.teltime()[2:]


        }

        for i in count_description:
            to_print.append([i + "\nUS: "+ str(count_description[i][0]) + "\nYOU : "+str(count_description[i][2]) +"\n"+p+" : "+str(count_description[i][1])])
        
        
        to_print.append(["total facetime (in minutes): "+str(self.facetime()[0])+" miniutes"+"\nwith "+str(self.facetime()[1])+" minutes the longest chat ever"])
        to_print.append(["total audio time(in minutes): "+str(self.teltime()[0])+" miniutes"+"\nwith "+str(self.teltime()[1])+" minutes the longest chat ever"])


        to_print.append(["Days between our first and last message:"+ str(self.rough_day())])
        
        to_print.append(["we chat every "+str(round(1/self.chat_per(),2))+" days for average!"])
        

        

        count_description={
            """
            Longest text sent :
            """:(self.longest_text(),"with","characters"),
            """
            Shortest text sent :
            """:(self.shortest_text(),"with","characters"),
            """
            The mantra of : 
            """:(self.mantra(),"talked","times"),
        }
        
        for i in count_description:
            tmp=count_description[i][0]
            front=str(count_description[i][1])+" "
            last=" "+str(count_description[i][2])
            to_print.append([i + "\nUS: "+ str(tmp[0][0]) + " , "+front+str(tmp[0][1])+last+"\nYOU : "+ str(tmp[2][0]) + " , "+front+str(tmp[2][1])+last+"\n"+p+" : "+ str(tmp[1][0]) + " , "+front+str(tmp[1][1])+last ])

        print(tabulate(to_print,headers="firstrow",tablefmt="fancy_grid"))

        
        

        
    
        sys.stdout=sys.__stdout__
        return 

