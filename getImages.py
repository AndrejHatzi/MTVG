import os
import re
import urllib.request
import requests
from bs4 import BeautifulSoup


#get music from
#https://www.youtube.com/watch?v=Lt6TY-H5uqM&list=PLSXJETi8b1AjeJ3jtOGEhJzUz9XHyDAsg&index=5

#MAX IMGS = 115;

'''
site = 'https://www.memedroid.com/memes/top/day'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img', {"class" : "img-responsive"})

urls = [img['src'] for img in img_tags]


print(urls)
'''

def image_to_video()->None:
	os.system("ffmpeg -f image2 -r 1/5 -i MEMES/%0d.jpg -vcodec mpeg4 -y current.mp4");

def retrieveImg()->None:
	page : int = 1;
	i : int = 20;
	for page in range(5):
		site = "https://www.memedroid.com/memes/top/day/{}".format(str(page));
		response = requests.get(site)
		soup = BeautifulSoup(response.text, 'html.parser')
		img_tags = soup.find_all('img', {"class" : "img-responsive"})
		urls = [img['src'] for img in img_tags]
		for url in urls:
			try:
				urllib.request.urlretrieve(url, "MEMES/{}.jpg".format(i));
				i+=1;
			except:
				pass;

retrieveImg();
