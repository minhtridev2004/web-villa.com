import requests
from bs4 import BeautifulSoup
from flask import Flask, request
import json 
import webbrowser as wb
app = Flask(__name__) 
def search(oder):
    url = f"https://www.google.com/search?q={oder}"
    page = requests.get(url)
    res =BeautifulSoup(page.content,'html.parser')
    link = res.find_all('a')
    ans = []
    for domain in link:
        href=domain.get('href')
        if href.startswith('/url?q='):
            ans.append(href.replace('/url?q=',''))
    return ans



@app.route('/source', methods = ['POST']) 
def link_br():
    data=request.get_json()   
     
    query = data['query']
    links = search(query)
    res=[]
    for link in links:
        res.append(link)
    return json.dumps(res)
# tim kiem 1 lien ket 
"""query = input("nhập nội dung cần tìm: ")
br = f"https://www.google.com/search?q={query}"
print(br)"""
if __name__ == "__main__": 
    app.run(port=5000)