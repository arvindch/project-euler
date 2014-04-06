__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.custom import checks


def main():
    
    giv_low = 100
    giv_high = 1000
    req_num = 0

    for x in xrange(giv_low, giv_high):
        for y in xrange(x, giv_high):
            product = x * y
            if checks.is_palindrome(product) and product > req_num:
                req_num = product

    return req_num


if __name__ == '__main__':
    answer = main()
    print answer