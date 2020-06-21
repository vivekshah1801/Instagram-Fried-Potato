from bs4 import BeautifulSoup,SoupStrainer
import requests

print("*************")
print("FRIED POTATO")
print("*************")

try:
    BASE_URL = "https://www.instagram.com/"
    only_meta = SoupStrainer("meta") # parse only the meta tags, leave rest of DOM tree as it it. Performace increase.

    instaid = input("Enter Instagram Public ID: ")
    url = BASE_URL + instaid

    cont = requests.get(url).content
    data = BeautifulSoup(cont, features="lxml",parse_only=only_meta)
    details = data.findAll(attrs={'name':'description'})[0]["content"]

    a = details.split(" ")

    followers = a[0]
    following = a[2]
    posts = a[4]

    print()
    print("----------------------------")
    print("Instagram Public Information")
    print("----------------------------")
    print("Account Id: ", instaid)
    print("Followers:  ", followers)
    print("Following:  ", following)
    print("Posts:      ", posts)
    print("----------------------------")
    print()
except Exception:
    print("Some Error Occured.")

