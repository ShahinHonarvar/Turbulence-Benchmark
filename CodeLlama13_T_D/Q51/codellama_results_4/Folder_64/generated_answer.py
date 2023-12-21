
def if_contains_anagrams(my_list):
    # Initialize a dictionary to store the anagram counts for each letter
    anagram_counts = {}

    # Iterate over the list of strings and count the anagrams for each letter
    for word in my_list:
        word = word.lower()
        if len(word) >= 3:
            for char in set(word):
                anagram_counts[char] = anagram_counts.get(char, 0) + 1

    # Check if there are at most 59 pairs of anagrams in the list
    return sum(anagram_counts.values()) <= 59
