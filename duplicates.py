import json
#def prod_reform(prod_model):
#    if prod_model.strip().isdigit() == False:
#        p_output = re.sub(r"(.+?)\s*(\d+)", r"\1-\2", prod_model)
#        return p_output
#
#def camera_check(listing_obj):
#    if "battery" in listing_obj["title"].lower() or "batterie" in listing_obj["title"].lower() or "remote" in listing_obj["title"].lower():
#        if "+" in listing_obj["title"].lower() or "mm" in listing_obj["title"].lower() or "with" in listing_obj["title"].lower():
#            return True
#    else:
#        return True      
#def listing_reform(listing_title):
#    output_l = re.sub(r"(.+?)\s*(\d+)", r"\1 \2",listing_title)
#    return output_l
#
#def mixed_form(prod_model):
#    prod_model = prod_model.strip()
#    if prod_model.isdigit() == False and prod_model.isalpha() == False:
#        return True
#    else:
#        return False
    

#line_dict = {"product_name":"Fujifilm-F500-EXR","manufacturer":"Fujifilm","model":"F500EXR","family":"FinePix","announced-date":"2011-01-04T19:00:00.000-05:00"}
#
#listing_obj = {"title":"Fujifilm FINEPIX F500EXR Digitalkamera (16 Megapixel, 15-fach opt. Zoom, 7,6 cm (3 Zoll) Display, bildstabilisiert)champagner","manufacturer":"FUJIFILM","currency":"GBP","price":"291.09"}
#
#if line_dict.get("manufacturer").lower() in listing_obj["manufacturer"].lower():
#    prod_model = " " + line_dict.get("model").lower().replace("-"," ") + " "
#    listing_title = listing_obj["title"].lower().replace("-"," ").replace(","," ")
#    prod_name = line_dict.get("product_name").replace("_"," ").replace("-"," ").lower() + " "
#    print("A manufacturer in listing")
#if camera_check(listing_obj) is True:
#                    if prod_name in listing_title:
#                        listings.append(listing_obj)
#                    elif prod_model in listing_title:
#                        if prod_model.strip().isdigit():
#                            if line_dict.get("family") != None:
#                                prod_family = line_dict.get("family").lower()
#                                if prod_family in listing_title:
#
#                                     if prod_model.rstrip() in listing_title.split()[:4]:
#                                         listings.append(listing_obj)
#
#
#                        elif mixed_form(prod_model) == True:
#                            listings.append(listing_obj)
#                    elif prod_reform(prod_model) != None and prod_reform(prod_model) in listing_obj["title"].lower():
#                        listings.append(listing_obj)
#                    elif mixed_form(prod_model) and prod_model.strip() in listing_reform(listing_title):
#                        listings.append(listing_obj)
#
#
#
prodz = open("products.txt", "r", encoding = 'utf-8')
for line in prodz:
    prod = json.loads(line)
    if prod["model"].isalpha():
        if len(prod["model"].split()) == 1:
            print(prod)
    








#duplicates = []
#duplicates_final = []
#results_file = open("results.txt","r", encoding='utf-8')
#for line in results_file:
#    result_obj = json.loads(line)
#    listing = result_obj.get("listings")
#    dic = listing[0]
#    if dic not in duplicates:
#        duplicates.append(dic)
#    else:
#        print(dic)
#    
#    
##for items in duplicates:
##    if items in duplicates_final:
##        print(items)
##    else:
##        duplicates_final.append(items)
#
##print(duplicates_final)
##    if dic in duplicates:
##        print(line)
##    else:
##        duplicates.append(result_obj)
#results_file.close()
#Leica V-LUX 20 12.1 MP Digital Camera with 12x Wide Angle Optical Zoom and 3.0-Inch LCD
#Samsung SL202 10MP Digital Camera with 3x Optical Zoom and 2.7 inch LCD (Pink)
#Canon PowerShot ELPH 300 HS (Black)
#PENTAX Optio WG-1 GPS 14 MP Rugged Waterproof Digital Camera with 5X Optical Zoom, 2.7-inch LCD and GPS Funtionality (Green )
#stylus diff families in listings--- Olympus Mju TOUGH 6010 Digital Compact Camera - Lava Red (12MP, 3.6x Wide Digital Zoom) 2.7 inch LCD

#Leica V-LUX 20 12.1 MP Digital Camera with 12x Wide Angle Optical Zoom and 3.0-Inch LCD
#Samsung SL202 10MP Digital Camera with 3x Optical Zoom and 2.7 inch LCD (Pink)
#Canon PowerShot ELPH 300 HS (Black)

#{'title': 'Samsung SL202 10MP Digital Camera with 3x Optical Zoom and 2.7 inch LCD (Pink)', 'manufacturer': 'Samsung', 'currency': 'USD', 'price': '83.76'}
#{'title': 'Canon PowerShot ELPH 300 HS (Black)', 'manufacturer': 'Canon Canada', 'currency': 'CAD', 'price': '259.99'}
#{'title': 'PENTAX Optio WG-1 GPS 14 MP Rugged Waterproof Digital Camera with 5X Optical Zoom, 2.7-inch LCD and GPS Funtionality (Green )', 'manufacturer': 'Pentax Canada', 'currency': 'CAD', 'price': '387.33'}
#{'title': 'Olympus Mju TOUGH 6010 Digital Compact Camera - Lava Red (12MP, 3.6x Wide Digital Zoom) 2.7 inch LCD', 'manufacturer': 'Olympus', 'currency': 'GBP', 'price': '292.85'}
#from operator import itemgetter
#p_file = open("resultsTEST.txt","r", encoding='utf-8')
#my_list = []
#for line in p_file:
#    p_obj = json.loads(line)
#    my_list.append(p_obj)
#
#newlist = sorted(my_list, key=itemgetter('announced-date'))

#l_count = 0
#r_count = 0 
#for line_l in listings_file:
#    listing_obj = json.loads(line_l)
#    if "tz20" in str(listing_obj).lower():
##        print(listing_obj)
#        l_count += 1
#listings_file.close()
#results = open("resultsREFACT.txt","r", encoding='utf-8')
#for line_r in results:
#    listing_obj = json.loads(line_r)
#    for prod in listing_obj:
#        if "tz20" in prod.lower():
#            print(listing_obj)
#            r_count += 1
#