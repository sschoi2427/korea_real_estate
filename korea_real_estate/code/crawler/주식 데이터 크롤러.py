# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:48:24 2019

@author: sec
"""
# 크롤링하기 전에 아래의 두 사이트를 먼저 확인해주세요.
# https://www.naver.com/robots.txt
# https://blog.naver.com/imredviolet/10068504314



import os
DATA_PATH = os.getcwd().replace('\\','/')
RESULT_PATH = DATA_PATH + "/result/"
dir_path = DATA_PATH
dir_name = 'result'
if not os.path.exists('./result/'):    
    os.mkdir(dir_path + '/' + dir_name + '/')

first_page = int(input("크롤링 대상의 첫 페이지를 입력하세요 : "))
last_page = int(input("크롤링 대상의 마지막 페이지를 입력하세요 : "))

import pandas as pd   
def finance_crawler(first , last):
    
    df = pd.DataFrame()

    for i in range (first, last+1):
        base_url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page={}".format(i) # 코스피데이터
        df = df.append(pd.read_html(base_url, header=0)[0], ignore_index=True).dropna()
    
        print(i, '페이지 완료')
        
    df = df[::-1] #역순정렬
    print(df[:3])
    
    df.to_csv(RESULT_PATH + 'stock_data.csv', encoding='euc-kr', index=False)
    
finance_crawler(first_page, last_page)



# first : 9
# last : 131

