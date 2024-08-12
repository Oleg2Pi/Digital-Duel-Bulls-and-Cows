import random

def rand_number()-> str:
    """This function creates a random number and returns it as a string. 
    The minimum number of numbers that can be in the hidden number is two, 
    and the maximum number is eight."""

    return str(random.randint(10, 99999999))



# assert type(rand_number()) == str