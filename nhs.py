#!/usr/bin/env python


import numpy as np
from random import choice

"""Set of helper functions to determine if NHS Number is real or not"""


def set_weights():
    """Set weights for each digit in NHS number"""    
    weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    return np.array(weights)


def set_nhs_array(nhs_number):
    """Convert NHS number to an array of digits"""
    return np.array([int(i) for i in str(nhs_number)][:-1])


def get_random_checksum_number(checksum_digit):
    """Function to generate a random, incorrect checksum digit"""
    options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    options = options.remove(checksum_digit)

    return choice(options)


def generate_valid_nhs_number():
    """Generates valid NHS number from 9-digit number given as argument
    Else generates random 10-digit NHS number"""

    nhs = 123456789

    valid_nhs_number = nhs
    return valid_nhs_number


def generate_invalid_nhs_number():
    
    nhs = 123456789

    invalid_nhs_number = nhs
    return invalid_nhs_number


def get_last_digit(number):
    return int(str(number)[-1:])


def number_length():
    if

def is_valid(nhs_number):

    # Define weights (in numpy array)
    weights = set_weights()
 
    # Split NHS number into a numpy array of single digits
    nhs = set_nhs_array(nhs_number)

    # Multiple the two 1D arrays
    mult = nhs * weights

    # Find the dot product of the arrays (sum of products)
    dot = np.dot(nhs, weights)

    # Calculate the remainded, mod 11
    remainder = dot % 11

    # Calculate the valid checksum for the first 9 digits of the NHS number
    valid_checksum = 11 - remainder

    # Extract the actual checksum given with the 10-digit number (last digit)
    instance_checksum = get_last_digit(nhs_number)

    # Check if the valid checksum is equal to the one used in the 10-digit number
    if instance_checksum == valid_checksum:
        print "%s is a valid NHS Number - incorrect checksum" % (nhs_number)
        return True
    else:
        print "%s is an invalid NHS Number - incorrect checksum" % (nhs_number)
        return False


def main():

    nhs_number = 1745438914
    print "NHS Number:", nhs_number
    print is_valid(nhs_number)



if __name__ == '__main__':
    main()