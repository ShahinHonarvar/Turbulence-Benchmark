
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        string = string.lower()

        # Check if the string is at least three characters long
        if len(string) < 3:
            continue

        # Create a list of all possible anagrams of the string
        possible_anagrams = []
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                possible_anagrams.append(''.join(sorted(string[i:j]))))

        # Loop through each possible anagram and check if it is already in the dictionary
        for anagram in possible_anagrams:
            if anagram in anagram_pairs:
                anagram_pairs[anagram] += 1
            else:
                anagram_pairs[anagram] = 1

    # Check if there are at least 54 pairs of anagrams in the list
    for pair, count in anagram_pairs.items():
        if count >= 54:
            return True

    return False
