import xml.etree.cElementTree as et
import urllib2
from time import sleep
from sys import exit

ID = "X1-ZWz1bceng556h7_4srxq"
zpid_path = "zpid.txt"
write_path = "data2.txt"

attributes = ["price", "street", "zipcode","city","state",
		"type","useCode","bedrooms",
		"bathrooms", "numFloors","numRooms",
		"exteriorMaterial","parkingType","coveredParkingSpaces",
		"heatingSources","heatingSystem","coolingSystem",
		"appliances", "floorCovering","floorCovering","rooms",
		"architecture","floorNumber","numUnits","homeDescription",
		"whatOwnerLoves","neighborhood"]

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


def make_url(ID, zpid):
	return "http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=%s&zpid=%s" % (ID, zpid)

with open(zpid_path) as f:
	zpids = f.readlines()
	
zpids = [zpid.split("_")[-1] for zpid in zpids]


write_file = open(write_path, 'w')
def writeline(sxml, url, attributes = attributes, path = write_path, delim=';'):
	tree = et.fromstring(sxml)
	line = ""
	zpid = tree.findall('request/zpid')[0].text 
	response = int(tree.findall('message/code')[0].text)
	if response == 0:
		for attribute in attributes:
			try:
				line += tree.findall(attribute)[0].text + ';'
			except:
				line += ';'
		write_file.write(line[:-1]+'\n')
		print 'print success for %s' % zpid
		return True
	elif response == 501:
		print 'data not available for zpid: %s' % zpid
		return True
	else:
		print "error access zpid %s with error %i \n\n%s\n" % (zpid, response, url)
		return False

count = 1
total = len(zpids)
for zpid in zpids:
	result = 0
	url = make_url(ID, zpid)
	response = urllib2.urlopen(url)
	sxml = response.read()
	success = writeline(sxml, url)
	if success == False:
		break

write_file.close()
