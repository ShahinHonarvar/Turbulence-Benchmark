
def if_contains_anagrams(my_list):
    # Initialize a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for word in my_list:
        # Convert the string to lowercase and remove any punctuation or whitespace
        word = word.lower().translate(str.maketrans("", "", ".,?!"))
        
        # Check if the word is at least three letters long
        if len(word) < 3:
            continue

        # Sort the letters in the word to form an anagram key
        key = "".join(sorted(word))

        # Increment the count for this anagram key
        anagram_counts[key] = anagram_counts.get(key, 0) + 1

    # Check if there are at most 401 pairs of anagrams in the list
    return len(anagram_counts) <= 401
