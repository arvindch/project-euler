#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.py.custom import checks


def main():

    giv_low = 100
    giv_high = 1000
    req_num = 0

    for a in xrange(giv_low, giv_high):
        for b in xrange(a, giv_high):
            product = a * b
            if product > req_num:
                if checks.is_palindrome(product):
                    req_num = product

    return req_num


if __name__ == '__main__':
    answer = main()
    print answer
