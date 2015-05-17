########################
# author: Johnny Chang #
########################

## assumptions: all functions use book of genesis lol

# we want flaot division
from __future__ import division

# we want default dict for sorted dict
from collections import defaultdict

import nltk

# get dataset
from nltk.book import *

# description: naive implementation of function
#            : word_frequency, basically a freq dict 
#
# return     : dict of all the word types in text3
#            : and the frequency of occurences

def word_frequency():
    words = sorted(set(text3))                  # take the set (non-duplicated entries) of text3 and sort it
    count = [text3.count(x) for x in words]     # take the number of times each word appears in text3
    freq_dict = {x:y for x in words for y in count} # create a dict with key: word and value: frequency

    return freq_dict

# description: naive implementation of a freq dict but
#            : with percentage of the text occupied by the word
#
# return     : dict with percentage of text the word occupies
#            : also sorted set

def word_occupation():
    freq_dict = word_frequency()                                         # get dict from word_frequency()
    occupation_dict = {100 * freq_dict[k]/len(text3) for k in freq_dict} # calculate percentage for each key in freq_dict

    return occupation_dict

# descrption: takes the x most frequent words and calculates
#           : how much of the book is composed of them.
#           : hypothesis: power law distribution
#
# param     : how many of the top entreis in the frequency dict
#           : you would like information about
# return    : percentage the top x entries in the book of geneis occupy

def top_occupants(x):
    occupation_dict_sorted = word_occupation().sort()  # get occupation dictionary and sort it
    total = 0
    i = 0                                              # iterator variables
    for k in occupation_dict_sorted and i < x:         # iteration loop
        total += occupation_dict_sorted[k]             # adds occupancy to total
        i += 1

    return total # returns total occupancy of top x entries

print(top_occupants(50))
