
def return_n_greatest_chars(s):
    # sort the characters in descending order using sorted() function
    sorted_characters = sorted(s, reverse=True)
    # create a list with 39 elements and fill it with the first 39 characters of the sorted list
    greatest_characters = sorted_charaters[:39]
    return greatest_characters
