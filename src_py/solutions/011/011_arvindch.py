#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def main():
    
    giv_mat = [[] for _ in xrange(20)]
    giv_mat[0] = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'.split(' ')
    giv_mat[1] = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'.split(' ')
    giv_mat[2] = '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'.split(' ')
    giv_mat[3] = '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'.split(' ')
    giv_mat[4] = '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'.split(' ')
    giv_mat[5] = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'.split(' ')
    giv_mat[6] = '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'.split(' ')
    giv_mat[7] = '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'.split(' ')
    giv_mat[8] = '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'.split(' ')
    giv_mat[9] = '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'.split(' ')
    giv_mat[10] = '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'.split(' ')
    giv_mat[11] = '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'.split(' ')
    giv_mat[12] = '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'.split(' ')
    giv_mat[13] = '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'.split(' ')
    giv_mat[14] = '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'.split(' ')
    giv_mat[15] = '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'.split(' ')
    giv_mat[16] = '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'.split(' ')
    giv_mat[17] = '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'.split(' ')
    giv_mat[18] = '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'.split(' ')
    giv_mat[19] = '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'.split(' ')

    for i in xrange(20):
        for j in xrange(20):
            giv_mat[i][j] = int(giv_mat[i][j])
    req_prod = 0

    for i in xrange(20):
        for j in xrange(20):
            products = {'horizontal': 0, 'vertical': 0, 'down_diag': 0, 'up_diag': 0}
            # horizontal products
            try:
                products['horizontal'] = giv_mat[i][j] * giv_mat[i][j + 1] * giv_mat[i][j + 2] * giv_mat[i][j + 3]
            except IndexError:
                products['horizontal'] = 0
            # vertical products
            try:
                products['vertical'] = giv_mat[i][j] * giv_mat[i + 1][j] * giv_mat[i + 2][j] * giv_mat[i + 3][j]
            except IndexError:
                products['vertical'] = 0
            # diagonal products
            try:
                products['down_diag'] = giv_mat[i][j] * giv_mat[i + 1][j + 1] * giv_mat[i + 2][j + 2] * giv_mat[i + 3][j + 3]
            except IndexError:
                products['down_diag'] = 0
            try:
                products['up_diag'] = giv_mat[i][j] * giv_mat[i - 1][j + 1] * giv_mat[i - 2][j + 2] * giv_mat[i - 3][j + 3]
            except IndexError:
                products['up_diag'] = 0
            
            # compare products
            for product in products.values():
                if product > req_prod:
                    req_prod = product

    return req_prod


if __name__ == '__main__':
    answer = main()
    print answer