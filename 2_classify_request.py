import json
import re
import requests

everything=[]

with open("artists_books.txt") as artists_books_file:
    data = json.load(artists_books_file)
#we did a print as we were writing the script to see if each step was working
# print (data)

for a_book in data:
    # print (a_book)

    author = a_book["a"]
    title = a_book["t"]
    #print (author, title)

    author = author.replace(", artist.", "")
    author = author.replace(" artist.","")
    author = author.replace(", author.", "")
    author = author.replace(" author.", "")
    author = author.replace(", designer.", "")
    author = author.replace(" artist, designer.","")
    author = author.replace(", photographer.","")
    author = author.replace(", photographer, artist.","")
    author = author.replace(", photographer, author.","")

    base_url = "http://classify.oclc.org/classify2/Classify?author="+author+"&title="+title+"&summary=false"


    # print(base_url)
    r = requests.get(base_url)
    results = r.text
    #we used regular expressions to ensure we were getting the right numbers from the HTML
    if '<response code="2"/>'in results:
        p_responsecode = re.compile('[=]["][2]["][/][>]{1}')
        m_1 = p_responsecode.search(results)
        p_oclc_number = re.compile('[>](\d{5,})[<]')
        m_2 = p_oclc_number.search(results)
        p_holding_number = re.compile('[B][o][o][k]["]\s[h][o][l][d][i][n][g][s][=]["](\d{1,3})["]\s')
        m_3 = p_holding_number.search(results)
        p_oclc_numbers = re.compile('[o][c][l][c][=]["](\d{5,})')
        m_4 = p_oclc_numbers.findall(results)
	#our initial script gave us an attribute error, the if statement resolved that error
        if m_4 is not None and m_3 is not None:

            # print(title, m_2.group(1),m_3.group(1),m_4)

            a_book["oclc_number"]=m_4
            a_book["holding_number"]=m_3.group(1)
            # print(a_book)
            everything.append(a_book)
            print(len(everything))
            with open("everything.txt","w") as outfile:
                json.dump(everything, outfile, indent=4)
                #our everything text does not have the number of results we expected- 14, 764, instead there are 6,562 results
