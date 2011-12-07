import urllib, httplib

print "Google calculator:"

while True:
    # get expression to calc from user
    expression = raw_input("? ")
    # exit?
    if len(expression) == 0 or expression == "q":
        break
    # establish connection to google
    connection = httplib.HTTPConnection("www.google.com")
    # encode the expression to url (using a dict to create q=...)
    expression = urllib.urlencode({"q": expression})
    # request to search for expression
    connection.request("GET","/search?"+expression)

    # get the response data
    data = connection.getresponse().read()

    # rly bad code warning ;P
    # found no good way to retrieve this with 're'
    # start to read answer from the bold part written in font-size:138
    # (hope Google never ever change it)
    start = '<h2 class=r style="font-size:138%"><b>'
    # end when bold part's over
    end = "</b>"

    # if start string wasn't found the expression isn't valid and made google do another search
    if data.find(start) == -1:
        print "Invalid Google calc expression."

    # retrieve the result
    else:
        # the answer starts from the index of the end of the start string
        start = data.index(start)+len(start)
        # remove data before starting index
        data = data[start:]
        # now ending index is at the first found end string
        end = data.index(end)
        # remove data after ending index
        result = data[:end]
        
        # special deluxe fixes
        # fix proper a*10^b=aEb and a^b notation
        result = result.replace(" &#215; 10<sup>", "E").replace("<sup>", "^").replace("</sup>", "")
        # fix proper 3-digits notation
        result = result.replace("\xa0", " ").replace("<font size=-2> </font>"," ")
        
        # print the answer to user
        print result
