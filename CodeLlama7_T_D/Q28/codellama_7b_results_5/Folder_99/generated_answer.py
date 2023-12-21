
def return_nth_smallest_ascii(s):
    # create a list of the characters in the string
    char_list = list(s)
    # create a dictionary to store the frequency of each character
    freq_dict = {}
    # loop through the characters in the string and update the frequency dictionary
    for c in char_list:
        if c not in freq_dict:
            freq_dict[c] = 1
        else:
            freq_dict[c] += 1
    # sort the dictionary by key (character)
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[0]))
    # get the 8th smallest ASCII value from the sorted dictionary
    nth_smallest = list(sorted_dict.values())[7]
    return nth_smallest
