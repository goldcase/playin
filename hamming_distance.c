#include <string.h>
#include <stdio.h>
#include <assert.h>

/*
char ** ARR_TEST_1 = {  "holy SHIT",
                        "",
                        "ARUBA",
                        "BITCHES",
                        "AMAZING",
                        "LOREM",
                        "KODALINE",
                        "KANYE WEST",
                        "holy fuck"}
*/

int hamming_distance(char * a, char * b) {
    int len_a = strlen(a);
    int len_b = strlen(b);

    /* take care of some edge cases */
    if (len_a == 0) {
        return len_b;
    } else if (len_b == 0) {
        return len_a;
    }

    int hamming_dist = len_a - len_b;
    if (hamming_dist < 0) { // this means that a is the smaller string
        while (*a) {        // while the character is not the NULL character
            if (*a != *b) { // increment Hamming distance if character differs
                hamming_dist++;
            }
            a++;            // increment the char we're looking at
            b++;
        }
    } else {                // this is also the len_a == len_b case
        while (*b) {
            if (*a != *b) {
                hamming_dist++;
            }
            a++;
            b++;
        }
    }

    return hamming_dist;
}

int main() {
    int ham_cat = hamming_distance("cat", "hat");
    printf("%d\n", ham_cat);
    //printf("'cat' and 'hat' Hamming distance is %d\n", ham_cat);
    //assert(hamming_distance("cat", "hat") == 1);

    int ham_holy = hamming_distance("holy shit", "holy fuck");
    printf("%d\n", ham_holy);

    int ham_berg = hamming_distance("heisenberg", "gutenberg");
    printf("%d\n", ham_berg);

    return 0;
}
