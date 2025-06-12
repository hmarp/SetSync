"""
Main script to fetch setlist information from setlist.fm based on user input.
"""

import setlist_fm

print('\n\n')
artist_name = input("Artist Name: ")
city = input("City Name: ")
date = input("Date (format dd-MM-yyyy): ")

setlist = setlist_fm.get_setlist(artist_name, city, date)
print('\n')
print(setlist)
