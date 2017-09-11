import json
original_file = open("resultsRF.txt","r", encoding="utf-8")
original = []
for lines in original_file:
    obj = json.loads(lines)
    o_listings = obj.get("listings")
    for lines4 in o_listings:
        prod_hash = lines4
    original.append(prod_hash)
#print(other)

refact_file = open("results.txt","r", encoding="utf-8")
RF = []
for lines2 in refact_file:
    obj = json.loads(lines2)
    r_listings = obj.get("listings")
    for lines3 in r_listings:
        list_hash = lines3
#    print(r_listings)
    RF.append(list_hash)
#print(RF)

missing_from_O = []
for stuff in RF:
    if stuff not in original:
        missing_from_O.append(stuff)
print("Missing from original")
print(missing_from_O)       
#print(missing_from_O[0])
missing_from_RF = []
for my in original:
    if my not in RF:
        missing_from_RF.append(my)
print("Missing From Refactored")
print(missing_from_RF)


##isdigit check if is letters
##{"product_name":"Panasonic-
##TZ20","manufacturer":"Panasonic","model":"DMC-
##TZ20","family":"Lumix","announced-
##date":"2011-01-24T19:00:00.000-05:00"}
##
##{"title":"PANASONIC Lumix DMC-TZ20 -
##silver","manufacturer":"Panasonic","currency":"GBP","price":"399.99"}
