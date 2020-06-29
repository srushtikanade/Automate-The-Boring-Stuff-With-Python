# we search pictures on imgur and in jpg, you could alter program for bmp,png or other extension
import requests, os, bs4

def imageDownload(name):
    url = 'https://imgur.com/search?q='+name
    os.makedirs(name, exist_ok=True) #makes a directory/folder with the term you searched for 
    while not url.endswith('#'):
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        imgElem = soup.select('.post > .image-list-link img') # this is for bing webbrowser on edge
        if imgElem == []:
            print('Could not find image for '+ name)
        else:
            for i,image in enumerate(imgElem): # for the length of all found elements list
                imgUrl_thumbnail = 'https:' + imgElem[i].get('src') # this gives images in thumbnail, we have to convert it to fullsize
                imgUrl=imgUrl_thumbnail[:-5]+'.jpg' #here you could alter the extension
                print('Downloading image %s...' % (imgUrl))
                res = requests.get(imgUrl)
                res.raise_for_status()
                imageFile = open(os.path.join(name, os.path.basename(imgUrl)),'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            return len(imgElem)
            
         
            print('Done.The pictures are saved in a directory named '+name)


#imageDownload('cars')
nameOfObj=input('Enter the name/term of something you want pictures of :')
imageDownload(nameOfObj)
    

