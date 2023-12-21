
def return_nth_smallest_ascii(string):
    # create a list of all the characters in the string
    char_list = list(string)
    # create a dictionary to store the frequency of each character

    freq_dict = {}
    for char in char_list:
        if char not in freq_dict:
            freq_dict[char] = 1

        else:
            freq_dict[char] += 1

    # sort the dictionary by frequency

    sorted_freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    nth_smallest_ascii = sorted_freq_dict[19][0]

    return nth_smallest_ascii
