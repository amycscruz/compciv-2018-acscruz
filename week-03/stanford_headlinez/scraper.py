def print_hedz(url='https://www.stanford.edu/news/'):
    txt=fetch_html(url)
    htags=parse_headline_tags(txt)
    for t in htags:
        hedtxt=extract_headline_text(t)
        print(hedtxt)

def extract_headline_text(txt):
    htags=parse_headline_tags(txt)
    n=len(htags)
    for i in range(0,n):
        tags=htags[i].split('>')
        x=tags[2].split('<')[0]
    return(x)

def parse_headline_tags(txt):
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
