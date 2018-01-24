def extract_headline_text(txt):
    htags=parse_headline_tags(txt)
    for n in range [0,len(htags)]:
        hedz=htags[n].split('>')
        print(hedz)

def parse_headline_tags(txt):
    fetch_html(url)
    lines=txt.splitlines()
    htags=[]
    for line in lines:
        if '<h3><a href' in line:
            htags.append(line)
    return(htags)


def fetch_html(url):
    import requests
    resp=requests.get(url)
    txt=resp.text
    return(txt)

url="https://wgetsnaps.github.io/stanford-edu-news/news/simple.html"
txt=fetch_html(url)
htags=parse_headline_tags(txt)
print(htags)



    
