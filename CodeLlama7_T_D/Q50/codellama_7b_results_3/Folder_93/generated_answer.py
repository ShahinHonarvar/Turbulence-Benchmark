
def if_contains_anagrams(str_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for str in str_list:
        # Convert the string to lowercase
        # so that we can ignore case while comparing strings
        str = str.lower()

        # Check if the current string is an anagram of any other string
        # in the list using the 'in' operator
        for other_str in str_list:
            # Convert the other string to lowercase
            other_str = other_str.lower()

            # Check if the current string and the other string are anagrams of each other
            if sorted(str) == sorted(other_str):
                # If they are anagrams, add them to the dictionary
                # with the count of 1
                if str not in anagram_counts:
                    anagram_counts[str] = 1
                else:
                    anagram_counts[str] += 1

            # Check if any of the strings have a length of at least three
            # so that we can only consider anagrams of the length of at least three
            if len(str) < 3 or len(other_str) < 3:
                continue

            # Check if the current string and the other string are not equal but are similar
            # using the 'difflib.SequenceMatcher' class
            match = difflib.SequenceMatcher(a=str, b=other_str).ratio()

            # If the strings are similar enough to be considered anagrams of each other
            # then add them to the dictionary with the count of 1
            if match > 0.9:
                if str not in anagram_counts:
                    anagram_counts[str] = 1
                else:
                    anagram_counts[str] += 1

    # Check if the dictionary contains at least 18 pairs of anagrams
    if len(anagram_counts) >= 18:
        return True
    else:
        return False
