"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    list = [2]
    number = 3
    count = 1

    while count < number_of_primes:
        
        for x in list:

            if number%x == 0:
                break
        else:
            list.append(number)
            count += 1

        number += 1


    return list
