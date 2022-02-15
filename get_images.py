import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 

sources = []
    
htmldata = getdata("https://generated.photos/faces/female") 
soup = BeautifulSoup(htmldata, 'html.parser') 

f = open("components/home/data/scores.txt", "a")

for item in soup.find_all('img'):
    source = item["src"]
    formated_source = source.replace("https://images.generated.photos/", "")
    formated_source = formated_source.replace(".jpg", "")

    source_id = formated_source.split("/")[5]
    starting_score = 1400

    write_data = f"{source_id}|{starting_score}|{source}\n"

    f.write(write_data)

f.close()