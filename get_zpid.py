import urllib2
import re

def scrape_search(start=1, end=20, path = "zpid.txt"):
	""" Seaches through Zillow search results 'start' to 'end' and writes zpids into 'path' """	
	websites = []
	zpid_txt = open(path,"w")

	for i in xrange(start, end):
		manhattan = "http://www.zillow.com/homes/for_sale/Manhattan-New-York-NY/pmf,pf_pt/12530_rid/days_sort/40.915329,-73.787956,40.643917,-74.158745_rect/10_zm/%i_p/" % i
		bronx = "http://www.zillow.com/homes/for_sale/Bronx-New-York-NY/pmf,pf_pt/17182_rid/days_sort/40.918312,-73.756542,40.782751,-73.941936_rect/11_zm/%i_p/" % i
		queens = "http://www.zillow.com/homes/for_sale/Queens-New-York-NY/pmf,pf_pt/270915_rid/days_sort/40.807313,-73.645821,40.53546,-74.016609_rect/10_zm/%i_p/" % i
		brooklyn = "http://www.zillow.com/homes/for_sale/Brooklyn-New-York-NY/pmf,pf_pt/37607_rid/days_sort/40.791199,-73.752251,40.51928,-74.123039_rect/10_zm/%i_p/" % i
		staten_island = "http://www.zillow.com/homes/for_sale/Staten-Island-New-York-NY/pmf,pf_pt/27252_rid/days_sort/40.708491,-73.968544,40.436234,-74.339333_rect/10_zm/%i_p/" % i
		websites.extend((manhattan,bronx,queens,brooklyn,staten_island))

	for website in websites:
		try: 
			response = urllib2.urlopen(website)
			html = response.read()
		except:
			print "error opening %s" % website
			continue

		data = [line for line in html.split()]

		for item in data:
			zpid = re.search("zpid_[0-9]{5,15}", item)
			if zpid:
				zpid_txt.write("%s\n" % zpid.group(0))

	zpid_txt.close()
	print "Done writing to %s!" % path


