import time
import random

def string_teletyper(string):
    '''Prints out each character in a string with time delay'''
    for chr in string:
        print(chr, end='', flush=True)
        time.sleep(random.randint(1,2)/20)


if __name__ == "__main__":
    test_st = 'My string to test as an argument'
    string_teletyper(test_st)