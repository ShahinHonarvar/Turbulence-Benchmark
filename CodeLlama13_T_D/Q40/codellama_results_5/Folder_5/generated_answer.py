
def return_n_smallest_chars(distinct_chars):
    # create a dictionary where the key is each character and value is its ASCII value
    ascii_dict = {char: ord(char) for char in distinct_chars}
    
    # sort the dictionary by value in descending order
    sorted_ascii_dict = dict(sorted(ascii_dict.items(), key=lambda x: x[1], reverse=True))
    
    # create a list of exactly 46 characters from the sorted dictionary
    n_smallest_chars = [char for char, _ in sorted_ascii_dict.items()][:46]
    
    return n_smallest_chars
