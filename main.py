# Scrap Public Instagram profile details
# Usage:
#   $ python3 main.py -f path/to/file [-q] 

from bs4 import BeautifulSoup,SoupStrainer
import requests
import argparse
from datetime import datetime

BASE_URL = "https://www.instagram.com/"
only_meta = SoupStrainer("meta") # parse only the meta tags, leave rest of DOM tree as it it. Performace increase.

# CLI setup
parser = argparse.ArgumentParser(description="Get Details of Instagram handle's posts, followers and following")
parser.add_argument("-f", "--file", help="path to the text file containing instagram Ids seprated by newline.", required=True)
parser.add_argument("-q", "--quite", help="to quite all the errors", action='store_true')
parser.add_argument("-o", "--output", help="path to output file.")
args = parser.parse_args()


def getDetails(instaId):
    """
    @params
    instaId:String  instagram username
    @returns
    result:Dictionary  dictionary containing profile details
    """
    url = BASE_URL + instaId
    html_doc = requests.get(url).content
    parsed_html = BeautifulSoup(html_doc, features="lxml",parse_only=only_meta)
    
    try:
        details = parsed_html.findAll(attrs={'name':'description'})
        details = details[0]["content"]
        details_parsed = details.split(" ")

        followers = details_parsed[0]
        following = details_parsed[2]
        posts = details_parsed[4]
    except Exception:
        raise ValueError('Couldn\'t parse the data for %s ' % instaId)

    return {
        "instaId": instaId,
        "followers":followers,
        "following":following,
        "posts":posts,
    }


def main():
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(time)
    
    output = False
    if args.output is not None:
        output = True
        
    if output:
        try:
            outputfile = open(args.output, "a")
        except:
            if not args.quite:
                print("Error in opening the output file")
                return 1
    try:
        with open(args.file,"r") as instaIdList:
            print("Fetching Data...")
            for instaId in instaIdList:
                try:
                    if not instaId.strip():
                        continue
                    result = getDetails(instaId.strip())
                    print(result)
                    if output:
                        outputfile.write("{},{},{},{},{}\n".format(time, instaId.strip(), result["followers"].strip(), result["following"].strip(), result["posts"].strip()))
                except Exception as e:
                    if not args.quite:
                        print(e.args[0])
            if output:
                outputfile.close()
        print("Done")
    except FileNotFoundError:
        if not args.quite:
            print("File not found. Make sure the file exists at the specified path and is accesible for reading.")
    except Exception as e:
        if not args.quite:
            print("Some Error Occured")
        print(e)

if __name__ == "__main__":
    main()
