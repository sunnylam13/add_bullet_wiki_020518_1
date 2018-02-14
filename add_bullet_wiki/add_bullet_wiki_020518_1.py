# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# Adding Bullets to Wiki Markup

# add_bullet_wiki_020518_1.py
# adds Wiki bullet points to the start of each line of text on the clipboard
# 1.  Paste text from the clipboard
# 2.  Do something to it
# 3.  Copy the new text to the clipboard

# good program for understanding how to use the clipboard, and alter text with Python programs

import pyperclip

text = pyperclip.paste()

#####################################
# SEPARATE LINES, ADD STARS
#####################################

# Separate lines and add stars.
# we split the lines at the `\n` carriage return ASCII

lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i] # add star to each string in "lines" list

#####################################
# END SEPARATE LINES
#####################################

#####################################
# JOIN LINES
#####################################

text = '\n'.join(lines)

#####################################
# END JOIN LINES
#####################################

pyperclip.copy(text)
