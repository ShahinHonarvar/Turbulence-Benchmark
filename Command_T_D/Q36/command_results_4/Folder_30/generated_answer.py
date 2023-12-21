 
import re
def filter_chars(string):
    return re.sub(r'([^3][^I]{%d}[^3][^I]{%d})', '', string)
