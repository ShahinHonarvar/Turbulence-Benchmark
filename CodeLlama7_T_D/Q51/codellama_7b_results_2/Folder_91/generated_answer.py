
def if_contains_anagrams(my_list):
    # Convert the list of strings to lowercase
    my_list = [s.lower() for s in my_list]
    # Create a dictionary to store the counts of each letter
    letter_counts = {}

    # Loop through each string in the list
    for s in my_list:
        # Loop through each character in the string
        for c in s:
            # If the character is not already in the dictionary, add it with a count of 1
            if c not in letter_counts:
                letter_counts[c] = 1

            # Otherwise, increment the count of the character by 1
            else:
                letter_counts[c] += 1

    # Create a list to store the anagrams
    anagrams = []

    # Loop through each string in the list again
    for s in my_list:
        # If the string is not already in the list of anagrams, add it
        if s not in anagrams:
            anagrams.append(s)

    # Create a variable to store the number of pairs of anagrams found
    num_pairs = 0

    # Loop through each string in the list again
    for i in range(len(anagrams)):
        # If there are at least three letters in the string, check if it is an anagram of any other strings in the list
        if len(anagrams[i]) >= 3:
            for j in range(i+1, len(anagrams)):
                # If the string is an anagram of another string, add a pair to the number of pairs found variable
                if sorted(anagrams[i]) == sorted(anagrams[j]):
                    num_pairs += 1

    # Return True if there are at most 88 pairs of anagrams in the given list, otherwise return False
    return num_pairs <= 88
