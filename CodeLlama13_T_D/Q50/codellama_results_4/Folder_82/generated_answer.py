
def if_contains_anagrams(list):
    # Initialize an empty dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate through each string in the list
    for str1 in list:
        # Convert the string to lowercase and sort it
        sorted_str = ''.join(sorted(str1.lower()))

        # If the sorted string is not already in the dictionary, add it with a count of 1
        if sorted_str not in anagram_counts:
            anagram_counts[sorted_str] = 1

        # Otherwise, increment the count by 1
        else:
            anagram_counts[sorted_str] += 1

    # If there are at least 276 pairs of anagrams in the list, return true
    if len(anagram_counts) >= 276:
        return True

    # Otherwise, return false
    else:
        return False
