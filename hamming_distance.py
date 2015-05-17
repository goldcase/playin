########################
# author: Johnny Chang #
########################

## Description: Calculates Hamming Distance

def hamming_distance(x, y):
    diff_len = len(x) - len(y)     # take care of differences in string length
    hamming_dist = abs(diff_len)   # initialize Hamming distance holder with absolute value of differences in string length
    if diff_len < 0:               # if the length of x is smaller than y:
        for i in range(0, len(x)): # limit the comparison to the smaller length, in this case x
            if x[i] != y[i]:       # if the character at that index of x does not match with the character at that index of y, increase hamming distance by 1
                hamming_dist += 1
    else:                          # don't use another comparison, because the equal case is captured by len(y) as well
        for i in range(0, len(y)): # same as above
            if x[i] != y[i]:
                hamming_dist += 1

    return hamming_dist

print(hamming_distance("cat", "hat")) # expected: 1
print(hamming_distance("holy shit", "holy fuck")) # expected: 4
print(hamming_distance("gutenberg", "heisenberg")) # note that Levenshtein distance here would be a different story... tune in for next time
