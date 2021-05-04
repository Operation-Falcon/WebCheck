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

def web_check_file(filename):
    try:
        with open(filename, 'r') as file:
            file=file.readlines()
            for i in range(0, len(file)):
                r=requests.get(url=str("http://"+file[i]), allow_redirects=False, timeout=20)
                try:
                    if r.status_code==200:
                        print("http://"+file[i])
                    elif r.status_code !=200:
                        r = requests.get(url="https://"+file[i], timeout=20)
                        if r.status_code == 200:
                            print("https://"+file[i])
                except Exception as e:
                    print("Error caused")

    except Exception as e:
        print("Max retries exceeded with url. Caused by NewConnectionError")
