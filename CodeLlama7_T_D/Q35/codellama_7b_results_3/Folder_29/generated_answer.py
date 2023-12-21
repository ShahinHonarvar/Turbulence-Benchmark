
def remove_repeat_chars(s):
    # create a set of unique characters in the string
    unique_chars = set(s)
    # for each character in the set, check if it occurs more than once between indices 70 and 98
    for char in unique_chars:
        # get the index of the first occurrence of the character
        first_index = s.index(char)
        # get the index of the last occurrence of the character
        last_index = s[first_index::].index(char) + first_index
        # if the character occurs more than once between indices 70 and 98, remove all occurrences
        if (last_index > 70) and (first_index < 98):
            # create a list of tuples containing the index and character of each occurrence
            occurrences = [(i, char) for i in range(first_index, last_index + 1)]
            # sort the list of tuples by index
            occurrences.sort(key=lambda x: x[0])
            # remove all occurrences from the string
            for occurrence in occurrences:
                s = s[:occurrence[0]] + s[occurrence[0] + 1:]
    return s
