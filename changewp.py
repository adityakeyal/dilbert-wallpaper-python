import requests
import time
import ctypes
import shutil
def extract_src(responsebody):

    idx = 0
    for i  in range(0,4):
        idx = responsebody.find('<img')
        responsebody = responsebody[idx+4:]
    start = responsebody.find("src=\"")+5
    end = responsebody.find("\"",start)
    return responsebody[start:end]
    pass


def find_latest_url():

    date = time.strftime('%y-%m-%d', time.localtime())
    response = requests.get(f"https://dilbert.com/strip/{date}")
    responsebody = response.text
    src = extract_src(responsebody)
    return src
    
    pass


def set_url_as_wallpaper(src):
    imgresp = requests.get("https:"+src, stream = True)
    with open('d:/tmp/a.jpg','wb') as f:
        shutil.copyfileobj(imgresp.raw,f)
    del imgresp
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'd:/tmp/a.jpg' , 0)

    pass


if __name__ == '__main__':
    src = find_latest_url()
    set_url_as_wallpaper(src)