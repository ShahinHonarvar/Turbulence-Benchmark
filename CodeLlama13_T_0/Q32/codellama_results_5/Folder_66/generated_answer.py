
def insert_after_character(string, k):
    return "".join([char + k if char == k else char for char in string])
