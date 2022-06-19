import requests

S = requests.Session()

firstTerm = " "
secondTerm = " "

firstTerm = "Albert Einstein"
secondTerm = "Typhoid Fever"

foundLinks = {}
foundLinkKeys = []
foundLinkDepths = {}
totalFound = []
foundContexts = {}

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "links",
    "iwurl": 1,
    "titles": "Albert Einstein",
    "plnamespace": "0",
    "pllimit": "500",
    "redirects": "1"
}

CATPARAMS = {
    "action": "query",
    "format": "json",
    "prop": "categories",
    "iwurl": 1,
    "titles": "Albert Einstein",
    "cllimit": "500",
    "redirect": 1
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    for l in v["links"]:
        totalFound.append(l["title"])
        foundLinkKeys.append(l["title"])
        foundLinks[l["title"]] = "Albert Einstein then " + l["title"]
        #print(l["title"])


#Get categories
R = S.get(url=URL, params=CATPARAMS)
DATA = R.json()

foundContexts[PARAMS["titles"]] = []

PAGES = DATA["query"]["pages"]
for k, v in PAGES.items():
    for l in v["categories"]:
        foundContexts[PARAMS["titles"]].append(l["title"])
        print(l["title"])

#For second term

PARAMS["titles"] = "Typhoid fever"

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    for l in v["links"]:
        totalFound.append(l["title"])
        foundLinkKeys.append(l["title"])
        foundLinks[l["title"]] = "Albert Einstein then " + l["title"]
        #print(l["title"])

CATPARAMS["titles"] = "Typhoid fever"

#Get categories
R = S.get(url=URL, params=CATPARAMS)
DATA = R.json()

foundContexts[PARAMS["titles"]] = []

PAGES = DATA["query"]["pages"]
for k, v in PAGES.items():
    for l in v["categories"]:
        foundContexts[PARAMS["titles"]].append(l["title"])
        print(l["title"])




"""
while secondTerm not in foundLinks:
    print(foundLinkKeys)

    
    
    titleToLookFor = foundLinkKeys.pop()
    PARAMS["titles"] = titleToLookFor
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    print(titleToLookFor)

    for k, v in PAGES.items():
        if "links" in v.keys():
            for l in v["links"]:

                value = l["title"]

                if value not in totalFound:
                    totalFound.append(value)
                    foundLinkKeys.append(value)
                    foundLinks[value] = PARAMS["titles"] + " then " + value
                    
                    """

for link in foundLinkKeys:

    CATPARAMS['titles'] = link
    R = S.get(url=URL, params=CATPARAMS)
    DATA = R.json()

    foundContexts[CATPARAMS["titles"]] = []

    PAGES = DATA["query"]["pages"]
    for k, v in PAGES.items():
        if k != '-1':
            if 'categories' in v:
                for l in v["categories"]:
                    if 'articles' not in l and 'Articles' not in l:
                        foundContexts[CATPARAMS["titles"]].append(l["title"])
                        #print(l["title"])
            else:
                print("no categories for " + CATPARAMS['titles'])



print(foundLinks[secondTerm])
