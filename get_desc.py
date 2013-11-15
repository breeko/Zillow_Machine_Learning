

file_path = "zpid.txt"
attributes = ["price", "street", "zipcode","city","state",
		"type","useCode","bedrooms",
		"bathrooms", "numFloors","numRooms",
		"exteriorMaterial","parkingType","coveredParkingSpaces",
		"heatingSources","heatingSystem","coolingSystem",
		"appliances", "floorCovering","floorCovering","rooms",
		"architecture","floorNumber","numUnits","homeDescription",
		"whatOwnerLoves","neighborhood"]


with open(file_ath) as f:
	zpids = f.readlines()

