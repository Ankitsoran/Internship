#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[515]:


#Write a python program to display all the header tags from wikipedia.org
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6','h7'])
print('List all the header tags :', *titles, sep='\n')


# In[388]:


#Write a python program to display IMDB’s Top rated 100 movies’ data 
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Download IMDB's Top 100 data
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)-150):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-5]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    place = 0
    data = {"movie_title": movie_title,
            "year": year,
            "place": index+1,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'rating:', item['rating'], )
    



   


# In[389]:


#Write a python program to display IMDB’s Top rated 100 Indian movies’ data
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Download IMDB's Top 100 data
url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)-150):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-5]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    place = 0
    data = {"movie_title": movie_title,
            "year": year,
            "place": index+1,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'rating:', item['rating'], )
    



   


# In[570]:


#Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
url=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
url
soup=BeautifulSoup(url.content)
soup 
Team =[]
for i in soup.find_all('span',class_="u-hide-phablet"):
    Team.append(i.text)
Team[0:10]
team=Team[0:10]
l1=[]
for i in soup.find_all('td',class_="rankings-block__banner--matches"):
    l1.append(i.text) 
l2=[]
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    l2.append(i.text)
l3=l2[0:39:2] 
matches=l1+l3[0:9]
p1=[]
for i in soup.find_all('td',class_="rankings-block__banner--points"):
    p1.append(i.text)
p2=[]
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    p2.append(i.text)  
p3=p2[1:39:2] 
points=p1+p3[0:9]   
r1=[]
for i in soup.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    r1.append(i.text)
r1[0] = r1[0].strip()  
r2=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    r2.append(i.text)  
rating=r1+r2[0:9]
import pandas as pd
df=pd.DataFrame({'Team':team,'Matches':matches,'Points':points,'Rating':rating})
df
  


# In[562]:


#Top 10 ODI Batsmen in men along with the records of their team and rating.

url=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
url
soup=BeautifulSoup(url.content)
soup 
player=[]
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    player.append(i.text) 
player2=[]
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    player2.append(i.text.strip()) 
player=player+player2[0:9]
T=[]
for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    T.append(i.text.strip())    
T2=[]
for i in soup.find_all('span',class_="table-body__logo-text"):
    T2.append(i.text)
TEAM=T+T2[0:9]   
r1=[]
for i in soup.find_all('td',class_="u-text-left"):
    r1.append(i.text.strip())  
r2=[]
for i in soup.find_all('td',class_="table-body__cell rating"):
    r2.append(i.text)
RATING=r1+r2[0:9]
import pandas as pd
df=pd.DataFrame({'Player':player,'Team':TEAM,'Rating':RATING})
df
  


# In[569]:


#Top 10 ODI bowlers along with the records of their team and rating.

url=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
url
soup=BeautifulSoup(url.content)
soup 
bowler=[]
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    bowler.append(i.text)     
bowler2=[]
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    bowler2.append(i.text.strip()) 
bowler=bowler+bowler2[0:9]
T1=[]
for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    T1.append(i.text.strip())    
T3=[]
for i in soup.find_all('span',class_="table-body__logo-text"):
    T3.append(i.text)
TEAM=T1+T3[0:9]     
r1=[]
for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    r1.append(i.text.strip())  
r2=[]
for i in soup.find_all('td',class_="table-body__cell rating"):
    r2.append(i.text)
RATING=r1+r2[0:9]
import pandas as pd
df=pd.DataFrame({'BOWLER':bowler,'Team':TEAM,'Rating':RATING})
df
  


# In[828]:


#Top 10 ODI teams in women’s cricket along with the records for matches, points and rating
url=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
url
soup=BeautifulSoup(url.content)
soup 
Team =[]
for i in soup.find_all('span',class_="u-hide-phablet"):
    Team.append(i.text)
Team[0:10]
team=Team[0:10]
l1=[]
for i in soup.find_all('td',class_="rankings-block__banner--matches"):
    l1.append(i.text) 
l2=[]
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    l2.append(i.text)
l3=l2[0:39:2] 
matches=l1+l3[0:9]
p1=[]
for i in soup.find_all('td',class_="rankings-block__banner--points"):
    p1.append(i.text)
p2=[]
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    p2.append(i.text)  
p3=p2[1:39:2] 
points=p1+p3[0:9]   
r1=[]
for i in soup.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    r1.append(i.text)
r1[0] = r1[0].strip()  
r2=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    r2.append(i.text)  
rating=r1+r2[0:9]
import pandas as pd
df=pd.DataFrame({'Team':team,'Matches':matches,'Points':points,'Rating':rating})
df
  


# In[829]:


#Top 10 ODI Batsmen in men along with the records of their team and rating.
url=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
url
soup=BeautifulSoup(url.content)
soup 
player=[]
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    player.append(i.text) 
player2=[]
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    player2.append(i.text.strip()) 
player=player+player2[0:9]
T=[]
for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    T.append(i.text.strip())    
T2=[]
for i in soup.find_all('span',class_="table-body__logo-text"):
    T2.append(i.text)
TEAM=T+T2[0:9]   
r1=[]
for i in soup.find_all('td',class_="u-text-left"):
    r1.append(i.text.strip())  
r2=[]
for i in soup.find_all('td',class_="table-body__cell rating"):
    r2.append(i.text)
RATING=r1+r2[0:9]
import pandas as pd
df=pd.DataFrame({'Player':player,'Team':TEAM,'Rating':RATING})
df
  


# In[831]:


#Top 10 women’s ODI all-rounder along with the records of their team and rating.

url=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
url
soup=BeautifulSoup(url.content)
soup 
bowler=[]
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    bowler.append(i.text)     
bowler2=[]
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    bowler2.append(i.text.strip()) 
bowler=bowler+bowler2[0:9]
T1=[]
for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    T1.append(i.text.strip())    
T3=[]
for i in soup.find_all('span',class_="table-body__logo-text"):
    T3.append(i.text)
TEAM=T1+T3[0:9]     
r1=[]
for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    r1.append(i.text.strip())  
r2=[]
for i in soup.find_all('td',class_="table-body__cell rating"):
    r2.append(i.text)
RATING=r1+r2[0:9]
import pandas as pd
df=pd.DataFrame({'BOWLER':bowler,'Team':TEAM,'Rating':RATING})
df
  


# In[596]:


#Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content
#and the code for the video from the link for the youtube video from the post.
url=requests.get('https://coreyms.com/development/python/python-tutorial-zip-files-creating-and-extracting-zip-archives')
url#To get the data 
soup=BeautifulSoup(url.content)
soup 
title =[]#titel details
for i in soup.find_all('h1',class_="entry-title"):
        title.append(i.text)
date=[]    #to find date and time    
for i in soup.find('time',class_="entry-time"):
        date.append(i.text)      
content=[]     #summery of video  
for i in soup.find('div',class_="entry-content"):
        content.append(i.text)
link=[]    #scraping link using sibling tag    
for i in soup.find('span',class_="embed-youtube"):
        link.append(i['src'])
#joining all the above lists        
print(title,date,content[1],link)        


# In[670]:


# Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from nobroker.in.
url=requests.get('https://www.nobroker.in/property/sale/gurgaon/Sec-43?searchParam=W3sibGF0IjoyOC40NTA4MDkxLCJsb24iOjc3LjA3ODY2MTA5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSmRUb092ZW9ZRFRrUnFmSEJjaElIM3JBIiwicGxhY2VOYW1lIjoiU2VjLTQzIn1d&radius=2.0&city=gurgaon&locality=Sec-43')
url#To get the data 
soup=BeautifulSoup(url.content)
soup
title =[]
#titel details
location=[]
for i in soup.find_all('h2',class_="heading-6 font-semi-bold nb__25Cl7"):
        title.append(i.text)       
for i in soup.find_all('div',class_="nb__1EwQz"):
        location.append(i.text)  
price=[]    
area =[]
content=[]
for i in soup.find_all('div',class_="font-semi-bold heading-6"):
        content.append(i.text)
for i in range(0,len(content)-1,3):
    price.append(content[i+2])
    area.append(content[i])
emi=content[1:len(content):3]
df=pd.DataFrame({'Title':title,'Location':location,'Area':area,'EMI':emi,'Price':price})
df


# In[737]:


#Write a python program to scrape mentioned details from dineout.co.in
#url=requests.get('https://www.dineout.co.in/delhi')

url=requests.get('https://www.dineout.co.in/mumbai-restaurants?loc=Mumbai')
url

soup=BeautifulSoup(url.content)
soup
Restaurant_name =[]
Cuisine=[]
Location=[]
Ratings=[]
R2=[]
Image_URL=[]

for i in soup.find_all('a',class_="restnt-name ellipsis"):
        Restaurant_name.append(i.text) 
            
for i in soup.find_all('span',class_="double-line-ellipsis"):
       Cuisine.append(i.text.split('|')[1]) 
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
      Location.append(i.text)
for i in soup.find_all('div',class_="restnt-rating rating-4"):
      Ratings.append(i.text)
for i in soup.find_all('div',class_="restnt-rating rating-5"):
      R2.append(i.text) 
Rating=Ratings+R2
for i in soup.find_all('img',class_="no-img"):
    Image_URL.append(i['data-src'])          
df=pd.DataFrame({'Restaurant':Restaurant_name,'Cuisine':Cuisine,'Location':Location,'Ratings':Rating,'Image_URL':Image_URL}) 
df


# In[750]:


#Write a python program to scrape weather details for last 24 hours from Tutiempo.net


url=requests.get('https://www.tutiempo.net/')
url
#*Is not responding*


# In[827]:


# Write a python program to scrape monument name, monument description, image URL about top 10 monuments
# from puredestinations.co.uk
url=requests.get('https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/')
url
soup=BeautifulSoup(url.content)
soup
monument_name =[]
special_divs = soup.find_all('div',class_= 'blog--single__content column--3-4 u-spacing-third')
for text in special_divs:
    download = text.find_all('p')
for text in download:
    download1 = text.find_all('strong')    
    
monument_name=download[1:len(download):3]
monument=[]
for i in monument_name:
      monument.append(i.text)
Description=download[2:len(download):3]
monument_Description=[]
for i in Description:
      monument_Description.append(i.text)
Image_URL=[]
for i in soup.find_all('img',class_="lazyload"):
    Image_URL.append(i['data-src'])       
Image_URL=Image_URL[3:len(Image_URL)] 
df=pd.DataFrame({'monument':monument,'monument_Description':monument_Description,'Image_URL':Image_URL}) 
df

        


# In[ ]:





# In[ ]:




