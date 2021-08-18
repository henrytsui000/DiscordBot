

import urllib.request as req
import time as tm

def rtmonth(whattime):
    url="https://invoice.etax.nat.gov.tw/"
    with req.urlopen(url) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("td")
    cnt=0
    tmp=[]
    for title in titles:
        if title.span != None:
            #print(title.span.get_text())
            tmp.append(title.span.get_text().split("、"))
    np=[]
    lp=[]
    for ary in tmp:
        if len(ary[0])==3 and cnt==3:
            np.append(ary[0])
            continue
        if len(ary[0])==3 and cnt==6:
            lp.append(ary[0])
            continue
        cnt+=1
        if cnt==1:
            np.append(ary[0])
        if cnt==2:
            np.append(ary[0])
        if cnt==3:
            np.append(ary[0])
            np.append(ary[1])
            np.append(ary[2])
        if cnt==4:
            lp.append(ary[0])
        if cnt==5:
            lp.append(ary[0])
        if cnt==6:
            lp.append(ary[0])
            lp.append(ary[1])
            lp.append(ary[2])
    if whattime=="n":
        #print(np)
        return np
    if whattime=='l':
        return lp


      