
def if_contains_anagrams(strings):
    # Initialize a set to store anagrams
    anagrams = set()

    # Iterate over the strings and check if they are anagrams of each other
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                return True
    # If no pairs of anagrams are found, return False
    return False
