
def all_left_right_truncatable_prime(nums):
    #Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    #Function to check if a number is left- and right-truncatable prime
    def is_left_right_tprime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s)-i])):
                return False
        return True

    #Extract x
    x = nums[630]

    #Return list of left-and-right-truncatable prime numbers
    prime_list = [i for i in range(x, 1, -1) if is_left_right_tprime(i)]
    
    #Return the sorted prime list 
    return sorted(prime_list, reverse = True)
