
def return_n_greatest_chars(string):
    sorted_list = sorted([(ord(char), char) for char in string])
    return [char for _, char in sorted_list[-5:]]
