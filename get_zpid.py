import urllib2
import re

file_name = "zpid.txt"

websites = ["http://www.zillow.com/new-york-ny/"]
zpid_txt = open(file_name,"w")


for i in xrange(100):
	website = "http://www.zillow.com/homes/for_sale/New-York-NY/pmf,pf_pt/6181_rid/days_sort/40.977306,-73.66951,40.433882,-74.287491_rect/9_zm/%i_p/" % i
	websites.append(website)

for website in websites:
	response = urllib2.urlopen("http://www.zillow.com/new-york-ny/")
	html = response.read()
	data = [line for line in html.split()]

	for item in data:
		zpid = re.search("zpid_[0-9]{5,15}", item)
		if zpid:
			zpid_txt.write("%s\n" % zpid.group(0))

zpid_txt.close()
print "Done writing to %s!" % file_name


		
