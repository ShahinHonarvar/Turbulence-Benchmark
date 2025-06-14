
def if_contains_anagrams(my_list):
# create a dictionary to store the anagram pairs
anagram_pairs = {}

# loop through each string in the list
for string in my_list:

    # convert the string to lowercase
    lowercase_string = string.lower()

    # sort the letters of the string
    sorted_letters = ''.join(sorted(lowercase_string))

    # check if the sorted letters are already in the anagram pairs dictionary
    if sorted_letters in anagram_pairs:

        # increment the count of the pair by 1
        anagram_pairs[sorted_letters] += 1

    else:

        # add the pair to the dictionary with a count of 1
        anagram_pairs[sorted_letters] = 1

# check if there are more than 475 pairs of anagrams in the list
if len(anagram_pairs) > 475:

    # return false if there are more than 475 pairs of anagrams
    return False

else:

    # return true if there are no more than 475 pairs of anagrams
    return True
