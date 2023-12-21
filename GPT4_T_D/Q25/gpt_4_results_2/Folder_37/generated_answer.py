
def insert_at_index(given_list):
    if len(given_list) < 35:
        return "Error: The length of the given list is less than 35."
    else:
        given_list.insert(35, 88)
        return given_list
