import sys
def find_original_set(*arg):
    # Some black magic to find the original set
    # This is a very basic implementation, but you can
    # customize it to be faster if you'd like
    return set.intersection(*arg)
