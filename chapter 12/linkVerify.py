import requests, bs4

def linkVerify(url):
    print('Downloading Links on page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links= soup.select('a')
    notLinks=[]

    for link in links:
        checkUrl=link['href']
        if checkUrl.startswith('http'):
            toCheck=checkUrl
        elif checkUrl.startswith('//'):
            toCheck='https:'+checkUrl
        elif checkUrl.startswith('#'):
            toCheck=url+checkUrl
        results=requests.get(toCheck)

        if results.status_code==404:
            notLinks.append(toCheck)
    print('Number of broken links for this URL are :' +str(len(notLinks)))

myUrl=input('Enter the url of site you wish to verify links for :')
linkVerify(myUrl)
    
