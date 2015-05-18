########################
# Author: Johnny Chang #
########################

## Description: Calculates Levenshtein distance between two strings.
## defined as : minimum number of single-character edits (ie: insertions, deletions, or substitutions)
##            : required to change one word into the other.
## TODO: add explanation

# Description: My first DP algorithm.
# params: string a and string b to be compared to each other.
# returns: Levenshtein edit distance between the two strings.

def levenshtein(a, b):
    len_a = len(a)
    len_b = len(b)
    e = [[0 for j in range(len_b + 1)] for i in range(len_a + 1)]

    for j in range(len_b + 1):
        e[0][j] = j

    for i in range(1, len_a + 1):
        e[i][0] = i
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                e[i][j] = min(e[i - 1][j] + 1, e[i][j - 1] + 1, e[i - 1][j - 1])
            else:
                e[i][j] = min(e[i - 1][j] + 1, e[i][j - 1] + 1, e[i - 1][j - 1] + 1)
    return e[len_a][len_b]

print(levenshtein("bitches", "hitches"))
print(levenshtein("algorithm", "altruistic"))
print(levenshtein("heisenberg", "gutenberg"))

