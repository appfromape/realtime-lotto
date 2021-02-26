# you have to pip install requests and beautifulsoup4 to get it work.
# we can use chrome devlopment tools to figure out the website CSS and HTML syntax.
import requests
from bs4 import BeautifulSoup

# get the url to html data.
url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

# through CSS id="rightdown" we can use select method and find_all method.
# data1 = sp.select("#rightdown")  # method 1
data1 = sp.find_all(id = "rightdown") # method 2

# then you can find out the data1 just has one [], so we can use [0] to get data from data1.
# use the find function to find "威力彩" section, it's located on <div, class:"contents_box02">.
# data2 = data1[0].find('div', {'class':'contents_box02'}) # method 1
data2 = data1[0].find('div', class_= "contents_box02") # method 2

# you can use bs4 prettify() function to look up more clearly from html structure. 
# print(data2.prettify())

# you can use find_all method to find "威力彩" numbers in <div class="ball_tx ball_green">34 </div>.
# data3 = data2.find_all('div', {'class':'ball_tx'}) # method 1
data3 = data2.find_all('div', class_= "ball_tx") # method 2

# realtime "威力彩" numbers.
print("開出順序：", end = "")
for n in range(0,6):
    print(data3[n].text, end = "  ") 

print("\n大小順序：",end="")    
for n in range(6,len(data3)):
    print(data3[n].text, end = "  ")

# the second zone.
# red = data2.find('div', {'class':'ball_red'}) # method 1
red = data2.find('div', class_= "ball_red") # method 2
print("\n第二區：{}".format(red.text))