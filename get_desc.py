import xml.etree.cElementTree as et
import urllib2
from time import sleep
from sys import exit

ID = "X1-ZWz1bceng556h7_4srxq"
zpid_path = "zpid.txt"
zpid_expanded_path = "zpid_expanded.txt"
write_path = "data2.txt"

attributes_dict = { 
	1: "price", 
	2: "street", 
	3: "city",
	4: "zipcode",
	5: "address",
	6: "state",
	7: "useCode",
	8: "bedrooms",
	9: "bathrooms", 
	10: "finishedSqFt",
	11: "numFloors",
	12: "numRooms",
	13: "exteriorMaterial",
	14: "view",
	15: "parkingType",
	16: "coveredParkingSpaces",
	17: "heatingSources",
	18: "heatingSystem", 
	19: "coolingSystem",
	20: "homeDescription",
	21: "whatOwnerLoves",
	22: "neighborhood",
	23: "zpid"
}

attributes = ['response/price', 'response/address/street', 'response/address/city','response/address/zipcode','response/address/state','response/editedFacts/useCode', 'response/editedFacts/bedrooms', 'response/editedFacts/bathrooms','response/editedFacts/finishedSqFt', 'response/editedFacts/numFloors','response/editedFacts/numRooms','response/editedFacts/exteriorMaterial','response/editedFacts/view','response/editedFacts/parkingType','response/editedFacts/coveredParkingSpaces','response/editedFacts/heatingSources','response/editedFacts/heatingSystem', 'response/editedFacts/coolingSystem','response/homeDescription','response/whatOwnerLoves','response/neighborhood','request/zpid']


# attributes = {'response': 
#	['price', 
#	{'address': 
#		['street', 
#		'city', 
#		'zipcode', 
#		'state']}, 
#	{'editiedFacts': 
#		['useCode', 
#		'bedrooms', 
#		'bathrooms', 
#		'finishedSqFt', 
#		'numFloors', 
#		'numRooms', 
#		'exteriorMaterial', 
#		'view', 
#		'parkingType', 
#		'coveredParkingSpaces', 
#		'heatingSources',
#		'heatingSystem', 
#		'coolingSystem']},
#	'homeDescription',
#	'whatOwnerLoves',
#	'neighborhood',
#	{'request':
#		'zpid'}
#	]
#}


def make_url(zpid, ID = ID):
	return "http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=%s&zpid=%s" % (ID, zpid)

with open(zpid_path) as f:
	zpids = f.readlines()
with open(zpid_expanded_path) as f:
	zpids_expanded = f.readlines()
	
zpids = [zpid.split("_")[-1] for zpid in zpids]
zpids_expanded = [zpid.split("_")[-1] for zpid in zpids_expanded if zpid not in zpids]

write_file = open(write_path, 'w')
def get_line(sxml, attributes = attributes, delim=';'):
	tree = et.fromstring(sxml)
	line = ""
	zpid = tree.findall('request/zpid')[0].text 
	response = int(tree.findall('message/code')[0].text)
	if response == 0:
		for attribute in attributes:
			try:
				line_append = tree.findall(attribute)[0].text
				line_append.replace(";",".")
				line += line_append + ';'
			except:
				line += ';'
		line = line.encode('ascii','ignore')	
		line = line.replace('\n','.')	
		return response, line[:-1]
	else:
		return response, None

def main():
	count = 1
	total = len(zpids_expanded)
	for zpid in zpids_expanded:
		result = 0
		try:
			url = make_url(zpid)
			response = urllib2.urlopen(url)
		except:
			print "unable to access website for %s \n%s" % (zpid, url)
			continue
		sxml = response.read()
		response, line = get_line(sxml)
		if response == 0:
			write_file.write(line + "\n")
			print "Success writing zpid %s" % (zpid)		
		else:
			print "Error %s when access zpid %s" % (response, zpid)


	write_file.close()

if __name__ == "__main__":
    main()

