
def if_contains_anagrams(words):
    # Check that the input is a list of strings
    if not isinstance(words, list) or len(words) == 0 or not all([isinstance(word, str) for word in words])):
        raise ValueError("Input must be a non-empty list of strings")
    # Get the number of anagrams in the list
    num_anagrams = sum([len(set(word)) > 1 for word in words])
    # Check that there are at most 74 pairs of anagrams in the list
    if num_anagrams > 74:
        return False

    # Check that all anagrams have a length of at least three
    for word in words:
        if len(set(word)) > 1 and len(word) < 3:
            return False

    # If all checks pass, return True
    return True
