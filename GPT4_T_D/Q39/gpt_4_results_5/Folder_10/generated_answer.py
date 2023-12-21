
def return_n_greatest_chars(string):
    sorted_characters = sorted(string, key=ord, reverse=True)
    return sorted_characters[:88]
