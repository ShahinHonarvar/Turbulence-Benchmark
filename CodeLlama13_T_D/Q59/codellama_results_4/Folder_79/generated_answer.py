
def all_left_truncatable_prime(x):
    # initialize an empty list to store left-truncatable prime numbers
    ltp = []
    
    # loop through each integer in the range 2..x and check if it is a left-truncatable prime number
    for i in range(2, x+1):
        # convert the integer to a string
        s = str(i)
        
        # initialize a flag to indicate whether the integer is a left-truncatable prime number
        is_ltp = True
        
        # loop through each character in the string and check if it is 0
        for j, c in enumerate(s):
            # if the current character is 0, set the flag to False
            if c == '0':
                is_ltp = False
                break
        
        # if the integer is a left-truncatable prime number, add it to the list
        if is_ltp:
            ltp.append(i)
    
    # return the sorted list of left-truncatable prime numbers
    return sorted(ltp)
