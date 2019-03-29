import builtwith
import sys


try:
    host = sys.argv[1]
    read = builtwith.parse(host)
    data = read.items()

    for a,b in data:
        print (a+":",':'.join(b))
except:
    print("check syntax or your internet connection !")
    print("*Syntax",sys.argv[0],"http://www.example.com")
#whatweb
