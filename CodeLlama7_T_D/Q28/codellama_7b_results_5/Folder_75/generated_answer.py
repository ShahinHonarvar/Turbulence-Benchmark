
def return_nth_smallest_ascii(string):
    # create a list of all the characters in the string
    char_list = list(string)
    # create a dictionary to store the ASCII values and their corresponding indices

    ascii_dict = {}

    for i, char in enumerate(char_list):
        ascii_value = ord(char)
        if ascii_value not in ascii_dict:
            ascii_dict[ascii_value] = [i]

        else:

            ascii_dict[ascii_value].append(i)

    # sort the dictionary by key (ASCII value) and extract the indices of the 9th smallest ASCII value

    sorted_ascii_dict = dict(sorted(ascii_dict.items(), key=lambda x: x[0]))

    nth_smallest_ascii_value = list(sorted_ascii_dict.keys())[8]

    indices_of_nth_smallest_ascii_value = sorted_ascii_dict[nth_smallest_ascii_value]

    # return the character with the 9th smallest ASCII value among those characters in the string that occur between indices 62 to 83, both inclusive

    return char_list[indices_of_nth_smallest_ascii_value[0]]
