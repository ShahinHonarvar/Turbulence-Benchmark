
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    anagram_count = {}
    for word in my_list:
        # Sort the letters in the word to form an anagram
        sorted_letters = ''.join(sorted(word))
        if sorted_letters in anagram_count:
            # Increment the count of this anagram
            anagram_count[sorted_letters] += 1
        else:
            # Add a new entry for this anagram with a count of 1
            anagram_count[sorted_letters] = 1
    # Check if there are at most 277 pairs of anagrams in the list
    return len(anagram_count) <= 277
