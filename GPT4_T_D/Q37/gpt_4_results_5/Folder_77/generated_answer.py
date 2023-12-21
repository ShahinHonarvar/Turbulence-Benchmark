
def filter_chars(my_string):
    to_remove = set([c for c in my_string[384:412] if c >= '/' and c <= '8'])
    modified_string = "".join([c for c in my_string if c not in to_remove])
    return modified_string
