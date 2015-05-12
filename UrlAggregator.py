import requests
import re

i = 0
text_file = open("output.txt", "w")
while i < 5:
    r = requests.get("http://homertribune.com/category/news/page/" + str(i) +"/")
    urlFinderExpression = re.compile(r'(\<h2\>\<a href=\")(.+)(" rel="bookmark")')
    articleUrl = urlFinderExpression.findall(r.text)
    for x in articleUrl:
        text_file.write(x[1] + "\n")
        print x[1]
    
    # If we have not found any valid urls, we have come to the end of the archives
    # and we exit the loop, else, we incrememnt i to point us to the next numbered page
    if not articleUrl:
        i = 6
    else:
        i+=1

text_file.close()