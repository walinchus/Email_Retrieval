# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".



# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
import lxml.html
import mechanize
import urllib2



'''def scrape_table(root):
    #grab all table rows <tr> in table class="tblSearchResults"
    rows = root.cssselect("table.caseCourtTable tr")
    #create an ID number set at 0 - will add 1 every time we store a record (below)
    idno = 0
    #create a record to hold the data
    record = {}
    #for each row, loop through this
    for row in rows:
        #create a list of all cells <td> in that row
        table_cells = row.cssselect("td")
        if table_cells: 
        #if there is a cell, record the contents in our dataset, the first cell [0] in 'recipient' and so on
            record['Case Number'] = table_cells[0].text_content()
            record['Date Filed'] = table_cells[1].text_content()
            #this line adds 1 to the ID no. we set at 0 earlier
            #idno=idno+1
            #record['ID'] = idno 
            List_of_FileDates = [table_cells[1].textcontent()]
            Last_Date_Filed = List_of_FileDates[-1]
            print Last_Date_Filed, "is the last date filed."
            record['Caption'] = table_cells[2].text_content()
            record['Found Party'] = table_cells[3].text_content()
            table_cellsurls = table_cells[0].cssselect("a")
            #grab the href=" attribute of the first <a ... and store
            record['URL'] = table_cellsurls[0].attrib.get('href')
                # Print out the data we've gathered
            print record, '------------'
            # Save the record to the datastore - 'ID' is our unique key - 
            scraperwiki.sqlite.save(["Case Number"], record)'''
            

SearchSites = ['https://search.yahoo.com/search?p=The+Columbus+Foundation%20.org@',
'https://search.yahoo.com/search?p=UNIVERSITY+OF+CINCINNATI+FOUNDATION%20%.org@',
'https://search.yahoo.com/search?p=Toledo+Hospital.org@',
'https://search.yahoo.com/search?p=Fidelity+Charitable+Gift+Fund.org@',
'https://search.yahoo.com/search?p=CHILDRENS+HOSPITAL.org@']            
            
user_agent = 'Mozilla/5.0 (Mac) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,} 

for url in SearchSites:
  request=urllib2.Request(url,None,headers) #The assembled request
  response = urllib2.urlopen(request)
  data = response.read()# The data u need 
  print data

  #root = lxml.html.fromstring(html)
#scrape_table(root)


#print 'ALL DATA:', record
#scraperwiki.sqlite.save(unique_keys=['Date Filed and Judge'], data=record)
