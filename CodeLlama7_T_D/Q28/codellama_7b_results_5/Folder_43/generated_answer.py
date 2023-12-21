 def return_nth_smallest_ascii(string):
    # create a list of characters in the given string
    char_list = list(string)
    # calculate the smallest and largest ASCII values in the list
    min_ascii = min([ord(c) for c in char_list])
    max_ascii = max([ord(c) for c in char_list])
    # initialize a dictionary to store the frequency of each ASCII value
    ascii_freq = {}

    # iterate over the list of characters and calculate the frequency of each ASCII value
    for c in char_list:
        if ord(c) not in ascii_freq:
            ascii_freq[ord(c)] = 1
        else:
            ascii_freq[ord(c)] += 1

    # sort the dictionary by key (ASCII value)
    sorted_ascii = sorted(ascii_freq.items(), key=lambda x: x[0])

    # initialize a list to store the ASCII values that occur between indices 14 and 35, inclusive
    ascii_range = []

    # iterate over the sorted dictionary and add the ASCII values that occur between indices 14 and 35, inclusive, to the list
    for i in range(len(sorted_ascii)):
        if sorted_ascii[i][0] >= min_ascii + 13 and sorted_ascii[i][0] <= max_ascii - 12:
            ascii_range.append(sorted_ascii[i][0])

    # return the character with the 11th smallest ASCII value among those that occur between indices 14 to 35, both inclusive
    return chr(min(ascii_range))
