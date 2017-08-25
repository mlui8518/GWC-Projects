####### BINARY SEARCH #######

import string


countriesList = ["Afghanistan", "Argentina", "Brazil", "China", "Colombia", "Cuba", "Caech Republic", "El Salvador", "France", "Greece", "Guatemala", "Honduras", "Indonesia", "Iran", "Jamaica", "Japan", "Kazakhstan", "Moldova", "New Zealand", "Norway", "Pakistan", "Peru", "Poland", "Portugal", "Russia", "South Africa", "Sweden", "Tonga", "Ukraine", "Venezuela", "Zambia"]

# Start your search algorithm here.
print("Enter a Country Name")
countryName = (input())


first = 0
last = len(countriesList)-1
found = False

while( first<=last and not found):
	# Midpoint is 15 
	mid = int((first + last)/2)

	if countriesList[mid] == countryName:
		found = True

	elif countriesList[mid] != countryName:
		if countryName < countriesList[mid]:
			last = mid - 1
			mid = int((first + last)/2)
					
		elif countryName > countriesList[mid]:
			first = mid + 1	
			mid = int((first + last)/2)
			

# If the country is found, then print the country name. Else, print an error message!
if (found == True):
    print("Your country is in the country list. It is %s." % countryName)
else:
    print("Your country is not in the country list!")

