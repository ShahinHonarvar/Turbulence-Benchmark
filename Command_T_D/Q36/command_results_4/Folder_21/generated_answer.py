def filter_chars(string):
    return string.translate(str.maketrans("23456789ABCEFGHJKLMNPQRSTUVWXX", "23456789ABCDEFGHJKLMNPQRSTUVWXX"))
