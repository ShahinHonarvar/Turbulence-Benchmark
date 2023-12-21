
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j])):
                num_pairs += 1
    # Return true if there are at least 153 pairs of anagrams in the list
    return num_pairs >= 153
def is_anagram(string1, string2):
    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()
    # Check if both strings have a length of at least three
    if len(string1) < 3 or len(string2) < 3:
        return False

    # Count the number of characters in each string
    num_chars1 = len(set(string1))
    num_chars2 = len(set(string2)))
    # Check if both strings have at least three different characters
    if num_chars1 < 3 or num_chars2 < 3:
        return False

    # Check if the two strings are anagrams of each other
    return sorted(list(set(string1)))) == sorted(list(set(string2)))))
