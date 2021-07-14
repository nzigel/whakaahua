#python -m pip install requests

import requests

csvfilename = "sample.csv"

# open file to read
with open("{0}".format(csvfilename), mode='r', encoding='utf-8-sig') as csvfile:
    for line in csvfile:
        splitline = line.split(',')
        name = splitline[0]
        url = splitline[1].replace('\n','')

        r = requests.get(url)
        with open("images/{0}.jpg".format(name), "wb") as f:
            f.write(r.content)

