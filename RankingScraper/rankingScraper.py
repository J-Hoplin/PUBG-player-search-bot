import os
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re # Regex for youtube link
import warnings
import requests
import unicodedata
import json
import time

 # 'https://dak.gg/profile/andrewyoon20/pc-2018-07/steam'
    # 'https://dak.gg/profile/Plmm_JieDaWenn'
testURL = 'https://dak.gg/profile/Plmm_JieDaWenn'


html = urlopen(testURL)
html = BeautifulSoup(html,'html.parser')


# 경쟁전 정보가 담겨있는 레이아웃 정보

 # squad ranked Item : 경쟁전 정보 존재 squad ranked Item not found : 경쟁전 정보 미존재.

# index 0: fpp 1 : tpp
rankElements = html.findAll('div',{'class' : re.compile('squad ranked [A-Za-z0-9]')})


'''
-> 클래스 값을 가져와서 판별하는 것도 있지만 이 방법을 사용해 본다.
-> 만약 기록이 존재 하지 않는 경우 class 가 no_record라는 값을 가진 <div>가 생성된다. 이 태그로 데이터 유무 판별하면된다.
print(rankElements[1].find('div',{'class' : 'no_record'}))
'''

if rankElements[0].find('div',{'class' : 'no_record'}) != None: # 인덱스 0 : 경쟁전 fpp -> 정보가 있는지 없는지 유무를 판별한다.
    print("해당 경쟁전 정보가 존재하지 않습니다.")
else:
    
    #Short of fpp Rank
    fR = rankElements[0]
    # Tier Information
    
    # Get tier medal image
    tierMedalImage = fR.find('div',{'class' : 'grade-info'}).img['src']
    # Get tier Information
    tierInfo = fR.find('div',{'class' : 'grade-info'}).img['alt']
    
    # Rating Inforamtion
    # RP Score
    RPScore = fR.find('div',{'class' : 'rating'}).find('span',{'class' : 'caption'}).text
    
    #Get top rate statistics
    
    topRatioRank  = topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'rank'}).text
    topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'top'}).text
    
    # Main : Stats all in here.
    
    mainStatsLayout = fR.find('div',{'class' : 'stats'})
    
    #Stats Data Saved As List
    
    statsList = mainStatsLayout.findAll('p',{'class' : 'value'})
    statsRatingList = mainStatsLayout.findAll('span',{'class' : 'top'})
    
    
    for r in range(0,len(statsList)):
        # \n으로 큰 여백이 있어 split 처리
        statsList[r] = statsList[r].text.strip().split('\n')[0]
        statsRatingList[r] = statsRatingList[r].text
    # 평균등수는 stats Rating을 표시하지 않는다.
    statsRatingList = statsRatingList[0:5]
    
    print(tierMedalImage)
    print(tierInfo)
    print(topRatioRank)
    print(topRatio)
    print(statsList)
    print(statsRatingList)
    print(RPScore)
