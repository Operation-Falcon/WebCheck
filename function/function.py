import requests


def web_check(domain):
    try:
        r=requests.get(url='%s%s' % ('http://', domain), allow_redirects=False, timeout=20)
        if r.status_code==200:
            print('http://'+f"{domain}")
        elif r.status_code != 200:
            r=requests.get(url='%s%s' % ('https://', domain), timeout=20)
            if r.status_code==200:
                print("https://"+f"{domain}")
    except Exception as e:
        pass

