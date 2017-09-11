#==============================================================================
# Import modules
#==============================================================================
import time
import json
import re
#==============================================================================
# Function that inserts "-" between letters and numbers of product model to match
#with listings formatted differently e.g. Product for Olympus-vg120 with Listing
# titled "Olympus vg-120..."
#==============================================================================
def prod_reform(prod_model):
    if prod_model.strip().isdigit() == False:
        p_output = re.sub(r"(.+?)\s*(\d+)", r"\1-\2", prod_model)
        return p_output
    
#==============================================================================
# This function may seem a bit imprecise but it really does the trick. Checks
# whether item is just accessory made by an acceptable manufacturer. 
#==============================================================================
def camera_check(listing_obj):
    if "battery" in listing_obj["title"].lower() or "batterie" in listing_obj["title"].lower() or "remote" in listing_obj["title"].lower():
        if "+" in listing_obj["title"].lower() or "mm" in listing_obj["title"].lower() or "with" in listing_obj["title"].lower():
            return True
    else:
        return True
#==============================================================================
# Function that reformats listings so they can match with products formatted
# in a way not already addressed e.g. Casio QV3000EX vs Casio QV 300EX 
#==============================================================================      
def listing_reform(listing_title):
    output_l = re.sub(r"(.+?)\s*(\d+)", r"\1 \2",listing_title)
    return output_l
#==============================================================================
# Checks if model is a mix of letters/numbers
#============================================================================== 
def mixed_form(prod_model):
    prod_model = prod_model.strip()
    if prod_model.isdigit() == False and prod_model.isalpha() == False:
        return True
    else:
        return False
#==============================================================================
# Wrapping everything in a function so variables are local and not global
#==============================================================================
def sort():
#==============================================================================
#     creating an array to index listings so when a listing is ascribed to a 
# product its reference in the array can be removed  and will therefore not be
# included in a search of listings 
#==============================================================================
    short_list = []
    listings_file = open("listings.txt","r", encoding="utf-8")
    for line in listings_file:
        short_obj = json.loads(line)
        short_list.append(short_obj)
    listings_file.close()
    products_file = open("products.txt","r", encoding="utf-8")
#==============================================================================
#     'For' loops are faster than 'while' loops
#==============================================================================
    for lines_p in products_file:
        line_dict = json.loads(lines_p)
#==============================================================================
# Listings array for each product
#==============================================================================
        listings = []
        for listing_obj in short_list:
#==============================================================================
#                 If Product's manufacturer is in Listings, generate variables and move to next
#               "if" statement. Uses "in" over "==" because of cases like "kodak" vs. "kodakstock account"
#==============================================================================
            if line_dict["manufacturer"].lower() in listing_obj["manufacturer"].lower():
                prod_model = " " + line_dict["model"].lower().replace("-"," ") + " "
                listing_title = listing_obj["title"].lower().replace("-"," ").replace(","," ")
                prod_name = line_dict["product_name"].replace("_"," ").replace("-"," ").lower() + " "
                if camera_check(listing_obj) is True:
#==============================================================================
#                 If product_name(reformatted) is in Listing's "title," append 
#                to product listing
#==============================================================================
                    if prod_name in listing_title:
                        listings.append(listing_obj)
#==============================================================================
#                     Look for Product's "model" in Listing's "title"
#==============================================================================
                    elif prod_model in listing_title:
#==============================================================================
#                  If Product's model is only numbers it can easily be 
#                sprinkled in title somewhere irrelevant. If it is, checks to 
#                verify that the "family" of the product is in the title
#==============================================================================
                        if prod_model.strip().isdigit():
                            if line_dict.get("family") != None:
                                prod_family = line_dict.get("family").lower()
                                if prod_family in listing_title:
#==============================================================================
#                                 Make sure Product's "model" is in the first
#                               four words of Listing's Title. If so, append to
#                                "listings" array  
#==============================================================================
                                     if prod_model.rstrip() in listing_title.split()[:4]:
                                         listings.append(listing_obj)
#==============================================================================
#                          This "elif" statement could be redundant, but it 
#                         exists in case its coresponding "if" statement 
#                           returns "NoneType"                   
#==============================================================================
                        elif mixed_form(prod_model) == True:
                            listings.append(listing_obj)
#==============================================================================
#               Check that listing does not match a reformatted product_name(see
#               form_check function)
#==============================================================================
                    elif prod_reform(prod_model) != None and prod_reform(prod_model) in listing_obj["title"].lower():
                        listings.append(listing_obj)
                    elif mixed_form(prod_model) and prod_model.strip() in listing_reform(listing_title):
                        listings.append(listing_obj)
#==============================================================================
#      This could be done more efficiently, but removes listings of given product
#       from array that references listings.
#==============================================================================
        for items in listings:
            del short_list[short_list.index(items)]
        if len(listings) > 0:
            final = json.dumps({'product_name':line_dict.get("product_name"),'listings':listings})
            file = open("results.txt","a", encoding="utf-8")
            file.write(final + "\n")
    listings_file.close()
#start_time = time.time()    
sort()
#print("----- %s seconds ----" % (time.time() - start_time))      
