# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def convert_damages(damages):
  converted_damages = []
  for damage in damages:
    if damage == 'Damages not recorded':
      converted_damages.append(damage)
    if damage[-1] == 'M':
      converted_damages.append(float(damage.strip('M')) * conversion['M'])
    if damage[-1] == 'B':
      converted_damages.append(float(damage.strip('B')) * conversion['B'])
  return converted_damages
converted_damages = convert_damages(damages)
print(converted_damages)

# 2 
# Create a Table
def hurricane_table(name, month, year, max_sustained, areas_affected, damage, death):
  hurricane_dictionary = {}
  for i in range(len(names)):
    hurricane_dictionary[name[i]] = {"Name": name[i], "Month": month[i], "Year": year[i], "Max Sustained Wind": max_sustained[i], "Areas Affected": areas_affected[i], "Damage": damage[i], "Deaths": death[i]}
  return hurricane_dictionary

# Create and view the hurricanes dictionary
hurricane_dictionary = hurricane_table(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths)

print(hurricane_dictionary)

# 3
# Organizing by Year
def hurricane_year_dictionary(hurricanes):
  hurricanes_by_year = {}
  for hurricane in hurricanes:
      current_year = hurricanes[hurricane]['Year']
      current_hurricane = hurricanes[hurricane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_hurricane]
      else:
          hurricanes_by_year[current_year].append(current_hurricane)
  return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = hurricane_year_dictionary(hurricane_dictionary)
print(hurricanes_by_year)

# 4
# Counting Damaged Areas
def affected_areas_counted(hurricanes):
  affected_areas_count = {}
  for hurricane in hurricanes:
    for area in hurricanes[hurricane]['Areas Affected']:
      if area not in affected_areas_count:
        affected_areas_count[area] = 1
      else:
        affected_areas_count[area] += 1
  return affected_areas_count

# create dictionary of areas to store the number of hurricanes involved in
number_times_affected = affected_areas_counted(hurricane_dictionary)
print(number_times_affected)

# 5 
# Calculating Maximum Hurricane Count
def most_affected(number_affected):
  most_affected = {}
  number = 0
  for area in number_affected:
    if number_affected[area] > number:
      number = number_affected[area]
      most_affected[area] = number_affected[area]
  return most_affected
# find most frequently affected area and the number of hurricanes involved in
most_affected_area = most_affected(number_times_affected)
print(most_affected_area)

# 6
# Calculating the Deadliest Hurricane
def max_mortality_function(hurricanes):
  max_mortality = {}
  number = 0
  for hurri in hurricanes:
    if hurricanes[hurri]['Deaths'] > number:
      max_mortality = {hurri: hurricanes[hurri]['Deaths']}
      number = hurricanes[hurri]['Deaths']
  return max_mortality
# find highest mortality hurricane and the number of deaths
max_mortality = max_mortality_function(hurricane_dictionary)
print(max_mortality)

# 7
# Rating Hurricanes by Mortality
def mortality_rating_function(hurricanes):
  hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  number = 0
  for hurri in hurricanes:
    if hurricanes[hurri]['Deaths'] == 0:
      hurricanes_by_mortality[0].append(hurri)
    elif 100 > hurricanes[hurri]['Deaths'] > 0:
      hurricanes_by_mortality[1].append(hurri)
    elif 500 > hurricanes[hurri]['Deaths'] >= 100:
      hurricanes_by_mortality[2].append(hurri)
    elif 1000 > hurricanes[hurri]['Deaths'] >= 500:
      hurricanes_by_mortality[3].append(hurri)
    elif 10000 > hurricanes[hurri]['Deaths'] >= 1000:
      hurricanes_by_mortality[4].append(hurri)
    elif hurricanes[hurri]['Deaths'] >= 10000:
      hurricanes_by_mortality[5].append(hurri)
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricane_mortality_scale = mortality_rating_function(hurricane_dictionary)
print(hurricane_mortality_scale)

# 8 Calculating Hurricane Maximum Damage
def max_damage_function(hurricanes):
  max_damage = {}
  number = 0
  for hurri in hurricanes:
    if hurricanes[hurri]['Damage'] == "Damages not recorded":
      continue
    elif hurricanes[hurri]['Damage'] > number:
      max_damage = {hurri: hurricanes[hurri]['Damage']}
      number = hurricanes[hurri]['Damage']
  return max_damage
# find highest damage inducing hurricane and its total cost
max_damage = max_damage_function(hurricane_dictionary)
print(max_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating_function(hurricanes):
  hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: []}
  number = 0
  for hurri in hurricanes:
    if hurricanes[hurri]['Damage'] == "Damages not recorded":
      continue
    elif hurricanes[hurri]['Damage'] == damage_scale[0]:
      hurricanes_by_damage[0].append(hurri)
    elif damage_scale[1] > hurricanes[hurri]['Damage'] > damage_scale[0]:
      hurricanes_by_damage[1].append(hurri)
    elif damage_scale[2] > hurricanes[hurri]['Damage'] >= damage_scale[1]:
      hurricanes_by_damage[2].append(hurri)
    elif damage_scale[4] > hurricanes[hurri]['Damage'] >= damage_scale[3]:
      hurricanes_by_damage[3].append(hurri)
    elif hurricanes[hurri]['Damage'] >= damage_scale[4]:
      hurricanes_by_damage[4].append(hurri)
  return hurricanes_by_damage


hurricane_damage_scale = damage_rating_function(hurricane_dictionary)
print(hurricane_damage_scale)