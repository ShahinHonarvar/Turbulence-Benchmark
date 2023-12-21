def all_right_truncatable_prime(n):
    #Function to find all right-truncatable prime numbers less than x
    #Input: n, a tuple of positive integers
    #Output: a sorted list of all right-truncatable prime numbers less than x
    #If there is no such right-truncatable prime number, the function should return an empty list
    #A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
    #Example: all_right_truncatable_prime((94,))
    #Output: []
    #Example: all_right_truncatable_prime((95,))
    #Output: []
    #Example: all_right_truncatable_prime((96,))
    #Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    #Example: all_right_truncatable_prime((97,))
    #Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    a, b, l = n[0], n[1], []
    #Add all prime numbers less than x to the list
    while a != 0:
        l += [a]
        a = int(str(a)[-1])
    #Remove all non-prime numbers from the list
    l = [i for i in l if all(str(i) % d != 0 for d in range(2, int(str(i)[-1]) + 1))]
    #Sort the list
    l.sort()
    #Return the list
    return l
