
def if_contains_anagrams(str_list):
    # count the number of anagram pairs in the list
    anagram_count = 0
    for i in range(len(str_list)):
        # get the current string and its lowercase version
        curr_str = str_list[i]
        curr_str_lower = curr_str.lower()
        # check if there are at least three characters in the string
        if len(curr_str) >= 3:
            # loop through the remaining strings in the list
            for j in range(i + 1, len(str_list)):
                # get the current string and its lowercase version
                other_str = str_list[j]
                other_str_lower = other_str.lower()
                # check if the two strings are anagrams of each other
                if sorted(curr_str_lower) == sorted(other_str_lower):
                    # increment the anagram count if a pair is found
                    anagram_count += 1
                    break
    # return true if there are at least 48 pairs of anagrams in the list; otherwise, return false
    if anagram_count >= 48:
        return True
    else:
        return False
