import csv
from collections import defaultdict
from numpy import median

comp_path = 'comps.csv'
comp_file = open(comp_path, 'rb')

for skip in xrange(4):
	next(comp_file, None) # skip the first three header rows

data = defaultdict(list)

comps = {}

for i, row in enumerate(csv.reader(comp_file)):
	if not i or not row:
		continue
	zipcode = int(row[10])
	price = float(row[19].replace(',','').replace('$',''))
	if price != 0:			# bad/missing data
		data[zipcode].append(price)

for zipcode, prices in data.iteritems():
	comps[zipcode] = median(prices)

