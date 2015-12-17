from bs4 import BeautifulSoup
import requests
import json

base_url = "http://arcade.nyarc.org/search~S15?/X*&searchscope=15&SORT=D/X*&searchscope=15&SORT=D&SUBKEY=*/"

change_url = ",15486,15486,B/browse"
artists_books = []
#each page on arcade gives 50 results, the counter tells soup to loop through the 50 results
for counter in range(1,15486,50):

    search_url= base_url + str(counter) + change_url
    # print (artists_books)
    print("Request this url:")
    print(search_url)
    print(counter/50,15486/50)
    r = requests.get(search_url)
    # print (r.text)

    soup = BeautifulSoup(r.text, "html.parser")
    details = soup.find_all("td", attrs = {"class": "briefcitDetail"})

    for detail in details:

        lines = detail.text.split("\n")
        title = lines[3]
        author = lines[5]
        if author !="":
            artists_books.append({"t":title,"a":author})
   #We added the len function so that we would be sure the process was working
        print(len(artists_books))
    with open('artists_books.txt','w') as outfile:
	# this gave us a cleaner result in our text file
	# the text file contains 14,764 results. We have not resolved why there aren't 15,486 results yet
        json.dump(artists_books, outfile, indent=4)


