
def if_contains_anagrams(my_list):
    # Define the set of English letters
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    # Initialize variables to keep track of anagrams
    num_anagrams = 0
    num_pairs = 0
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string is an anagram of the English letters
        if set(lowercase_string) == english_letters:
            # Increment the number of anagrams
            num_anagrams += 1
        # Check if the string is a pair of anagrams
        for i in range(len(my_list) - 1):
            for j in range(i + 1, len(my_list)):
                if set(lowercase_string) == set(lowercase_string[::-1])):
                    # Increment the number of pairs of anagrams
                    num_pairs += 1
    # Check if there are at most 181 pairs of anagrams in the given list
    return num_anagrams + num_pairs <= 181
