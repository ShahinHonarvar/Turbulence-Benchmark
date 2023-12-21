
def return_n_greatest_chars(s):
    # sort the string in descending order based on ASCII values
    sorted_list = sorted(s, key=ord, reverse=True)
    # return the top 37 characters from the sorted list
    return sorted_list[:37]
