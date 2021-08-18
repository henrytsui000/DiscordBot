import random                                                                                       
import urllib.request as req 

def find_poetry():                                                                                                    
    url="https://fanti.dugushici.com/"                                                                  
    request=req.Request(                                                                                
            url,                                                                                        
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 S    afari/537.36"}
            )                                                                                           
    with req.urlopen(request) as response:                                                              
        data=response.read().decode("utf-8")                                                            
                                                                                                        
    import bs4                                                                                          
    a=[]                                                                                                
    root=bs4.BeautifulSoup(data,"html.parser")                                                          
    titles=root.find_all("div",class_="people_1")                                                       
    for title in titles:                                                                                
        if title.ul!=None and title.ul.li!=None:                                                        
            people=title.find_all("li")                                                                 
            for person in people:                                                                       
                a.append(person.a["href"])                                                              
                                                                                                        
    url="https://fanti.dugushici.com/"+a[random.randrange(10000000)%len(a)]                             
    request=req.Request(         
            url,                                                                                        
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 S    afari/537.36"})
    with req.urlopen(request) as response:                                                              
        data=response.read().decode("utf-8")                                                            
                                                                                                        
    b=[]                                                                                                
    root=bs4.BeautifulSoup(data,"html.parser")                                                          
    titles=root.find_all("div",class_="line")    
                                                         
    for title in titles:                                                                                
        b.append(title.a["href"])   
    
    poet="我是吟遊詩人"                                                                                  
    if len(b)==0:                                                                          
        poet="禪宗六祖慧能，為您帶來＜六祖壇經＞\n菩提本無樹，明鏡亦非台。本來無一物，何處惹塵埃?"                                                                                         
        return poet                                                                                                                                                                       
    url="https://fanti.dugushici.com/"+b[random.randrange(10000000)%len(b)]                             
    request=req.Request(                                                                                
            url,                                                                                        
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 S    afari/537.36"})
    with req.urlopen(request) as response:                                                              
        data=response.read().decode("utf-8")                                                            
    #print(url)                                                                                         
                                                                                                        
    root=bs4.BeautifulSoup(data,"html.parser")                                                          


    titles=root.find("td",style="padding-right:10px;vertical-align:top;")                               
    poet+=titles.img["title"]          
    poet+="，為您帶來＜"
    titles=root.find("h1",itemprop="name")                                                              
    poet+=titles.string+'＞    \n'                                                                     
                                                                                                        
                                                                 
                                                                                                        
    titles=root.find("div",class_="content")                                                            
    '''if titles.string != None:                                                                        
    56     print(titles.string)                                                                            
    57 else:                                                                                               
    58     print(titles)                                                                                   
    59 '''                                                                                                 
    for br in titles.find_all('br'):                                                                    
        br.insert(0,'\n      ')                                                                         
    #print(titles)                                                                                      
    poet+=titles.get_text()  
    return poet                                                                        
    #print(type(titles.get_text()))                                                                     
                               
import urllib.request as req 

def find_poetry():                                                                                                    
    url="https://fanti.dugushici.com/"                                                                  
    request=req.Request(                                                                                
            url,                                                                                        
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 S    afari/537.36"}
            )                                                                                           
    with req.urlopen(request) as response:                                                              
        data=response.read().decode("utf-8")                                                            
                                                                                                        
    import bs4                                                                                          
    a=[]                                                                                                
    root=bs4.BeautifulSoup(data,"html.parser")                                                          
    titles=root.find_all("div",class_="people_1")                                                       
    for title in titles:                                                                                
        if title.ul!=None and title.ul.li!=None:                                                        
            people=title.find_all("li")                                                                 
            for person in people:                                                                       
                a.append(person.a["href"])                                                              
                                                                                                        
    url="https://fanti.dugushici.com/"+a[random.randrange(10000000)%len(a)]                             
    request=req.Request(         
            url,                                                                                        
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 S    afari/537.36"})
    with req.urlopen(request) as response:                                                              
        data=response.read().decode("utf-8")                                                            
                                                                                                        
    b=[]                                                                                                
    root=bs4.BeautifulSoup(data,"html.parser")                                                          
    titles=root.find_all("div",class_="line")    
                                                         
    for title in titles:                                                                                
        b.append(title.a["href"])   
    
    poet="我是吟遊詩人"                                                                                  
    if len(b)==0:                                                                          
        poet="禪宗六祖慧能，為您帶來＜六祖壇經＞\n菩提本無樹，明鏡亦非台。本來無一物，何處惹塵埃?"                                                                                         
        return poet                                                                                                                                                                       
    url="https://fanti.dugushici.com/"+b[random.randrange(10000000)%len(b)]                             
    request=req.Request(                                                                                
            url,                                                                                        
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 S    afari/537.36"})
    with req.urlopen(request) as response:                                                              
        data=response.read().decode("utf-8")                                                            
    #print(url)                                                                                         
                                                                                                        
    root=bs4.BeautifulSoup(data,"html.parser")                                                          


    titles=root.find("td",style="padding-right:10px;vertical-align:top;")                               
    poet+=titles.img["title"]          
    poet+="，為您帶來＜"
    titles=root.find("h1",itemprop="name")                                                              
    poet+=titles.string+'＞    \n'                                                                     
                                                                                                        
                                                                 
                                                                                                        
    titles=root.find("div",class_="content")                                                            
    '''if titles.string != None:                                                                        
    56     print(titles.string)                                                                            
    57 else:                                                                                               
    58     print(titles)                                                                                   
    59 '''                                                                                                 
    for br in titles.find_all('br'):                                                                    
        br.insert(0,'\n      ')                                                                         
    #print(titles)                                                                                      
    poet+=titles.get_text()  
    return poet                                                                        
    #print(type(titles.get_text()))                                                                     
    for br in titles.find_all('br'):                                                                
        br.insert(0,'\n      ')                                                                         
    #print(titles)                                                                                      
    poet+=titles.get_text()  
    return poet                                                                        
    #print(type(titles.get_text()))                                                                     
                               