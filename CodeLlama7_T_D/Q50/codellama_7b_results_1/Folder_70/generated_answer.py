
def if_contains_anagrams(strings):
    # Calculate the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings)):
        # Get the current string and its length
        s1 = strings[i]
        slen1 = len(s1)
        # Check if the current string is a valid anagram
        if slen1 >= 3:
            # Get the characters of the current string
            chars1 = [c for c in s1]
            # Sort the characters of the current string
            sorted_chars1 = sorted(chars1)
            # Loop through the remaining strings in the list
            for j in range(i+1, len(strings)):
                # Get the next string and its length
                s2 = strings[j]
                slen2 = len(s2)
                # Check if the next string is a valid anagram
                if slen2 >= 3:
                    # Get the characters of the next string
                    chars2 = [c for c in s2]
                    # Sort the characters of the next string
                    sorted_chars2 = sorted(chars2)
                    # Check if the current string and the next string are anagrams of each other
                    if sorted_chars1 == sorted_chars2:
                        # Increment the number of pairs of anagrams found in the list
                        num_pairs += 1
                        # If we have found at least 189 pairs of anagrams, return True immediately
                        if num_pairs >= 189:
                            return True
    # If we have not found at least 189 pairs of anagrams in the list, return False
    return False
