
def if_contains_anagrams(str_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for str in str_list:
        # Convert the string to lowercase
        lowercase_str = str.lower()

        # If the length of the string is at least three,
        # then count the anagram pairs in the string
        if len(lowercase_str) >= 3:
            # Create a list of all the anagram pairs in the string
            anagram_pairs = []

            # Iterate over each character in the string
            for i in range(len(lowercase_str)):
                # If the current character is not the last character in the string,
                # then check if the next character is also present in the string
                if i < len(lowercase_str) - 1:
                    # If the next character is also present in the string,
                    # then create a pair of anagrams using the current character and the next character
                    if lowercase_str[i + 1] in lowercase_str[i + 2:]:
                        anagram_pairs.append((lowercase_str[i], lowercase_str[i + 1]))

            # Add the count of each anagram pair to the dictionary
            for pair in anagram_pairs:
                if pair not in anagram_counts:
                    anagram_counts[pair] = 0

                anagram_counts[pair] += 1

        # If there are at least 95 pairs of anagrams in the string,
        # then return True
        if sum(anagram_counts.values()) >= 95:
            return True

    # Otherwise, return False
    return False
