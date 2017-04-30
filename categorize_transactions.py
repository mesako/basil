
# Category object
# properties
# tags = keywords
# desc = string description of category

CATEGORIES = {}
CATEGORIES["Food"] = {"Food", "Restaurants", "Grocery Store", "Groceries", "Supermarket", "Market",
    "Coffee Shop", "Fast Food", "Snacks", "Dessert", "Drinks", "Bars", "Alcohol", "Cafe", "Dining"}
CATEGORIES["Travel"] = {"Travel", "Cruise", "Hotel", "Lodging", "Accommodations",
    "Air Travel", "Flights", "Airlines", "Rental Car", "Taxi", "Vacation"}
CATEGORIES["Car and Transit"] = {"AAA", "Gas", "Fuel", "Car Insurance", "Auto",
    "Parking", "Mechanic", "Auto Repair", "Train", "Subway", "Metro"}
CATEGORIES["Bills/Utilities"] = {"Housing", "Rent", "Energy", "Electricity",
    "Heat", "Water", "Garbage", "Internet", "Phone", "Renter's Insurance", "Television"}
CATEGORIES["Health"] = {"Dentist", "Doctor", "Prescription", "Medication",
    "Pharmacy", "Eyecare", "Health Insurance", "Copay"}
CATEGORIES["Fun"] = {"Fun", "Entertainment", "Arts", "Music", "Movies", "Hobbies",
    "Spa", "Games"}
CATEGORIES["Savings"] = {"House", "IRA", "Brokerage", "Investments", "Wedding",
    "Honeymoon"}
CATEGORIES["Life/Household"] = {"Clothes", "Household Supplies",
    "Personal Care", "Charity", "Gifts", "Shopping", "Education", "Books",
    "Electronics", "Laundry", "Hair", "Salon", "Donations"}
CATEGORIES["Taxes"] = {"Federal", "State", "Tax"}
CATEGORIES["Income"] = {"Income", "Paycheck", "Gift", "Bonus", "Investment",
    "Interest"}

def generate_possible_category_list(transaction):
    possible_categories = []
    for k in CATEGORIES.keys():
        for v in CATEGORIES[k]:
            match = re.search(pattern = v, string = transaction.merchant)
            if match:
                possible_categories.append(k)
                break
    return possible_categories

def add_categories_key_tags_pair(new_category_tags_pair):
    for new_key in list(new_category_tags_pair.keys()):
        CATEGORIES[new_key] = new_category_tags_pair.pop(new_key)
    
def change_categories_key(old_key, updated_key):
    CATEGORIES[updated_key] = CATEGORIES.pop(old_key)

def remove_categories_key(remove_key):
    CATEGORIES.pop(remove_key)

def add_categories_tag(which_key, new_tag):
    CATEGORIES[which_key].add(new_tag)

def remove_categories_tag(which_key, remove_tag):
    CATEGORIES[which_key].remove(remove_tag)



# Reimbursement	
# Refund
# Split



### Discover ### 
# Category
# Automotive
    # auto service
    # auto maintenance
    # auto repairs
    # auto supplies
# Department Stores
# Education
    # schools
    # day-care
    # trade schools
    # universities
# Gasoline
# Government Services
    # taxes
    # city services and fees
    # traffic tickets
# Home Improvement
    # hardware stores
    # paint stores
    # garden centers
    # flooring warehouses
# Medical Services
    # doctor visits
    # insurance copays
    # prescriptions
# Merchandise
    # apparel
    # beauty products
    # music
# Others and Miscellaneous
# Restaurants
    # cafes
    # fast food
    # coffee shops
# Services
    # utilities
    # shipping
    # salons
    # dry cleaning
# Supermarkets
# Travel and Entertainment
    # air travel
    # hotels
    # accommodations
    # tickets for events
    # concerts
    # sporting events
    # movies
# Warehouse Clubs
    # Sam's Club
    # Costco
    # BJs


### Chase ###
# Category
# Grocery Stores & Drugstores
# Automotive
    # Gas Stations
# Shopping
    # Department & Clothing Stores/Catalogs
    # Wholesale Clubs & Discount Stores
    # Office Supply Stores
    # Electronic & Appliance Stores
    # Furniture & Decore Stores
    # Other Retail
# Travel & Entertainment
    # Transit
# Home Improvement & Maintenance
    # Landscaping
    # Utilities
# Tax Deductible & Related Expenses
    # Charities & Other Organizations
    # Education & Child Care Services
    # Medical Supply Stores
    # Services
# Restaurants
# Other Expenditures
    # Dry Cleaners and Laundromats
    # Health Clubs & Memberships
    # Pet Supply Stores & Services
    # Salons & Beauty Supply Stores
    # Insurance
    # Tax
    # Legal & Financial Services
    # Shipping and Storage
    # Miscellaneous Services
    # Other


### BarclayCard ###
# Category (not included in CSV)
# Automotive
    # oil changes
    # car washes
    # tires
# Healthcare
# doctor visits
# prescriptions
# Merchandise
    # mall
    # online
    # other retail venues
# Restaurants & Entertainment
    # meals
    # movies
    # sporting events
# Travel
# airlines
    # car rentals
    # lodging
    # railroad tickets
    # cruises
# Everyday Spending
    # gas
    # groceries
    # utilities
# Other
    # home improvement
    # education

