# **IG Message Analyzer**


## **Introduction** 

IG Message Analyzer , analyzes IG inbox messages , evaluates relationship : )

## **Motivation**

Just for fun~

*Wish this tool helps you , ENJOY LEARNING !*

***

## **Requirements**

Before you begin, ensure you have met the following requirements:

* You have a machine that is able to execute python 
* You have installed all python extensions in requirements.txt
* You have read the instructions for using IG Message Analyzer

***

## **How to install**

### To install, follow these steps:


1.
```
git clone https://github.com/deeeelin/messageanalyzer.git <folder path>
```

2. install required module in requirements.txt:

```
pip3 install -r <path of requirements.txt>
```

3.Go to the installed folder and execute main.py

***

## **How to use**


### Material gathering :

REQUEST MESSAGE RECORDS:

   1. Use your computer sign in IG , and go to settings->your files and media ->reuqest download
![Image](./README_sources/1.png)
   
   2. Set download format as "HTML"
![Image](./README_sources/2.png)

   3. Wait for the download url in mail
![Image](./README_sources/3.png)

   4. Download the records
![Image](./README_sources/4.png)
![Image](./README_sources/5.png)

   5. Open download folder ,and go messages
![Image](./README_sources/6.png)

   6. go to ->inbox 
![Image](./README_sources/7.png)
    
   7. Find the folder name with the person's name you want to anlayze ,below example : lisa
![Image](./README_sources/8.png)
    
   8. copy/paste the folder's path to the program , press enter
![Image](./README_sources/input.png)

   9. Result document "text.txt" will be produce under the same folder of IG Message Analyzer.
    

**Sample result by following above instructions :**

╒══════════════════════════════════════════════════════════════════════════════════════════════════════╕
│ chat_person: Brandon                                                                                 │
╞══════════════════════════════════════════════════════════════════════════════════════════════════════╡
│ Total amount of messages sent :                                                                      │
│                                                                                                      │
│ US: 2157                                                                                             │
│ YOU : 852                                                                                            │
│ Brandon : 1305                                                                                       │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of images sent :                                                                              │
│                                                                                                      │
│ US: 276                                                                                              │
│ YOU : 120                                                                                            │
│ Brandon : 156                                                                                        │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of audios sent :                                                                              │
│                                                                                                      │
│ US: 0                                                                                                │
│ YOU : 0                                                                                              │
│ Brandon : 0                                                                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of reactions sent :                                                                           │
│                                                                                                      │
│ US: 56                                                                                               │
│ YOU : 39                                                                                             │
│ Brandon : 17                                                                                         │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of other's personal profiles shared :                                                         │
│                                                                                                      │
│ US: 0                                                                                                │
│ YOU : 0                                                                                              │
│ Brandon : 0                                                                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of posts shared :                                                                             │
│                                                                                                      │
│ US: 14                                                                                               │
│ YOU : 0                                                                                              │
│ Brandon : 14                                                                                         │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of stories replied :                                                                          │
│                                                                                                      │
│ US: 24                                                                                               │
│ YOU : 0                                                                                              │
│ Brandon : 24                                                                                         │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of text messages sent :                                                                       │
│                                                                                                      │
│ US: 1786                                                                                             │
│ YOU : 716                                                                                            │
│ Brandon : 1070                                                                                       │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Average length of every text message :                                                               │
│                                                                                                      │
│ US: 4.06                                                                                             │
│ YOU : 4.05                                                                                           │
│ Brandon : 4.07                                                                                       │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Average amount of message sent everyday :                                                            │
│                                                                                                      │
│ US: 1.14                                                                                             │
│ YOU : 0.46                                                                                           │
│ Brandon : 0.68                                                                                       │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Average amount of message sent for every chat day (Only considering the days that we sent message) : │
│                                                                                                      │
│ US: 13.13                                                                                            │
│ YOU : 5.26                                                                                           │
│ Brandon : 7.87                                                                                       │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of different text mentioned :                                                                 │
│                                                                                                      │
│ US: 1254                                                                                             │
│ YOU : 559                                                                                            │
│ Brandon : 748                                                                                        │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Percentage of repeating a same text :                                                                │
│                                                                                                      │
│ US: 29.79                                                                                            │
│ YOU : 21.93                                                                                          │
│ Brandon : 30.09                                                                                      │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of facetime chats:                                                                            │
│                                                                                                      │
│ US: 0                                                                                                │
│ YOU : 0                                                                                              │
│ Brandon : 0                                                                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Amount of audio chats:                                                                               │
│                                                                                                      │
│ US: 0                                                                                                │
│ YOU : 0                                                                                              │
│ Brandon : 0                                                                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ total facetime (in minutes): 0 miniutes                                                              │
│ with 0 minutes the longest chat ever                                                                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ total audio time(in minutes): 0 miniutes                                                             │
│ with 0 minutes the longest chat ever                                                                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Days between our first and last message:1569                                                         │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ we chat every 11.54 days for average!                                                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Longest text sent :                                                                                  │
│                                                                                                      │
│ US: brandon started a video chat     , with 32 characters                                            │
│ YOU : In home washing dish allday  , with 28 characters                                              │
│ Brandon    : brandon started a video chat     , with 32 characters                                   │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Shortest text sent :                                                                                 │
│                                                                                                      │
│ US: 嗨 , with 1 characters                                                                           │
│ YOU : 🫡 , with 1 characters                                                                         │
│ Brandon    : 約 , with 1 characters                                                                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ The mantra of :                                                                                      │
│                                                                                                      │
│ US: 哇 , talked 83 times                                                                             │
│ YOU : 👍 , talked 32 times                                                                           │
│ Brandon    : 好 , talked 64 times                                                                    │
╘══════════════════════════════════════════════════════════════════════════════════════════════════════╛



## **Very welcome to make contributes to NTHU_SELECT**

To contribute to this project:

1. Fork this repository.
2. Create branch
3. Make changes and commit them
4. Push to your github
5. Create pull request.
6. Send a message to me via email

## **List of contributors**

* [@deeeelin](https://github.com/deeeelin) 

## **Contact me**

If you want to contact me you can reach me at <dereklin100503@gmail.com>

## **MIT License**

This project uses the following license: [MIT License](https://choosealicense.com/licenses/mit/#).

***

