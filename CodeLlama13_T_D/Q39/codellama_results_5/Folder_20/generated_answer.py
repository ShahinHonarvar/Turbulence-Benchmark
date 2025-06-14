
def return_n_greatest_chars(string):
    # create a list of tuples containing character and its ASCII value
    char_ascii = [(char, ord(char)) for char in string]

    # sort the list in descending order based on ASCII values
    sorted_list = sorted(char_ascii, key=lambda x: x[1], reverse=True)

    # return the first 40 characters from the sorted list
    return [char for char, _ in sorted_list[:40]]
