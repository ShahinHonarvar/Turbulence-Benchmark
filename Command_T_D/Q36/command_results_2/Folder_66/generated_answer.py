import re
def filter_chars(string):
    return re.sub(r'<(39,87)[^>]*>(39,87)[^>]*>(39,87)', '', string)
