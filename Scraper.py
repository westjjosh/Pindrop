import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import csv


#Create a engine for connecting to SQLite3.




#This section pulls the table containing recent call entries into a table
url = 'https://s3.us-east-2.amazonaws.com/gsd-auth-callinfo/callnotes.html'
response = requests.get(url)
html = response.content
content = []
info = {}
areaCode = re.compile(r"AreaCode.aspx")
phoneNum = re.compile(r"Phone.aspx")

soup = BeautifulSoup(html, "html.parser")
table = soup.find(id="previews")

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

for row in table.findAll("div",class_="oos_preview"):
## still working on parsing out the tags
    area1 = row.findAll("a", href=areaCode)
    area1 = cleanhtml(area1)
    print(area1)
    info = {
        "area":     cleanhtml(row.findAll("a", href=areaCode)),
        "phone":    cleanhtml(row.findAll("a", href=phoneNum)),
        "reports":  cleanhtml(row.findAll("span", class_="postCount")),
        "comment":  cleanhtml(row.findAll("div", class_="oos_previewBody")),
    }
    content.append(info)


    


## create api resources
class results_all(Resource):
    def get(self):
        for row in content
            for cell in row
                print(cell)
        return {}

class results_areaCode(Resource):
    def get(self, areaCode):
        for row in content
            for cell in row
                print(cell)

        return {}
        
 
api.add_resource(results_all, '/all')
api.add_resource(results_areaCode, '/areacode')

if __name__ == '__main__':
     app.run()