
def filter_chars(string):
    return "".join([char for index, char in enumerate(string) if index not in range(124, 855) or not ('9' <= char <= 's')])
