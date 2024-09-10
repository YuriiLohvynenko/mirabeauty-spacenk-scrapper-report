'''571Gustavus_Adolphus_College'''
import re
import csv
import requests
import numpy as np
import os
import time
from bs4 import BeautifulSoup
durl = 'https://gustavus.edu/general_catalog/current/'
page = requests.get(durl)
soup = BeautifulSoup(page.content,"html.parser")
# print(soup) 

data2 = soup.find_all('a')
print(data2[0].text)
lst =[]
for i in range(525,572):
    print(i)
    print(data2[i].text)
    print(data2[i].get('href'))
    page2 = requests.get('https://gustavus.edu/general_catalog/current/' + data2[i].get('href'))
    soup2 = BeautifulSoup(page2.content,"html.parser")
    data3 = soup2.find('div',attrs ={'id':'generalCatalog'})
    ps = data3.find_all('p')
    for j in range(len(ps)):
        try:
            course = ps[j].find('span').text
            course_name = ps[j].find('span').text.split()[0]
            sort_des = course.replace(str(course_name),'')
            long_des = ps[j].find('em').text
            print('course name ; ',course_name) 
            print('sort des : ',sort_des)     
            print('long des : ',long_des)
            print('course : ',course)
            print('-------------')
            lst.append(course_name)
            lst.append(sort_des) 
            lst.append(long_des)
            lst.append(course)
        except Exception:
            pass
A = np.array(lst)
B = np.reshape(A, (-1, 4))
# print(B)
fields = ['course_name', 'short_descript','long_descriptioin','course'] #, 'long_description'
with open('571Gustavus_Adolphus_College_course.csv', 'w',newline='',encoding='utf-8') as csvfile:  
# creating a csv writer object  
    csvwriter = csv.writer(csvfile)     
    csvwriter.writerow(fields)      
    csvwriter.writerows(B)