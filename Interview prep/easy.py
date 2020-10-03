import copy
import math
import string
from collections import defaultdict


def get_bits(A):
    bin_rep = bin(A)
    bin_rep = bin_rep[2:]
    sum_of_1 = 0
    for i in str(bin_rep):
        if i == '1':
            sum_of_1 += 1
    return sum_of_1

def singleNumber(A):
    new_list = list(A)
    new_list.sort()
    for elem in range(0,len(A),2):
        if A[elem] == A[-1]:
            return A[elem]
        elif A[elem] != A[elem+1]:
            return A[elem]

def is_polindrom(str):
    for index, obj in enumerate(str):
        if obj != str[len(str)-1 - index]:
            return False
    return True

def bulbs(A):
    cur = A
    counter = 0
    for index, elem in enumerate(A):
        if elem == 0:
            counter += 1
            for index_2, elem_2 in enumerate(cur[index:]):
                cur[index_2+index] = (elem_2 + 1) % 2
    return counter

def bulbs(A):
    count = 0
    for i, ele in enumerate(A):
        if (ele + count) % 2 == 0:
            count += 1
    return count

def bini(A):
    s = 0
    for index in range(len(A)-1, 0, -1):
        s += pow(A[index], index)

    binary = bin(s)
    print(type(binary))
    return int(binary[2:])


def is_prime(num):
    ret = True
    for cur in range(2 , int(math.sqrt(num) + 1)):
        if num % cur == 0:
            ret = False
            break
    return ret


def prime_up_to(n):
    ret = []
    for i in range(n):
        if i % 2 != 0 and n != 2:
            if is_prime(i):
                ret.append(i)
    return ret


def find_two_primes(A):
    # primes = prime_up_to(n)
    for index_1 in range(A):
        index_2 = A - index_1
        if is_prime(index_1) and is_prime(index_2):
            if index_1 + index_2 == A:
                return [index_1, index_2]

def power2(A,cur = 2):
    for i in range(2, int(math.sqrt(A)+1)):
        for j in range(i, A):
            if math.pow(i,j) == A:
                return True
    return False

def calc_helper(matrix, filter, row, col):
    x = matrix[row][col]
    n = len(matrix)
    if row == 0 and col == 0: #we are at the out most left upper pixel
        filter[0,0] * x + x*filter[0,1] + x*filter[0,2]
        # - image[row][column - 1] + 8 * image[row][column] - image[row][column + 1] -
        # - image[row + 1][column - 1] - image[row + 1][column] - image[row + 1][column + 1]

def downsample(image):
    new_martix = []
    row_counter = 0 # counters the rows in the new matrix
    col_counter = 0 # counters the cols in the new matrix
    filter = [[1,1,1],[1,1,1],[1,1,1]]
    for rows in range(0,len(image),3):
        new_martix.append([])  # we uppend a new line for the ret matrix
        for cols in range(0,len(image),3):
            new_martix[row_counter].append(0) # we uppend a new line for the ret matrix
            # cur_sum = calc_helper(image, rows+1, cols+1, filter)
            # result_sum = cur_sum / 9 # we take the avg
            new_martix[row_counter][col_counter] = 5
            row_counter += 1
            col_counter += 1


def gcd(A, B):
    if A == 0:
        return B
    elif B == 0:
        return A

    min_g = A if A < B else B
    for cur in range(min_g + 1, 1, -1):
        if A % cur == 0 and B % cur == 0:
            return cur
    return 1

def print_matrix(matrix, filter):
    new_matrix = copy.deepcopy(matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col])
            new_matrix[row][col] = calc_helper(matrix, row, col, filter)

def wave(self, A):
    A.sort()
    for index in range(0, len(A), 2):
        if A[index] == A[-1]:
            break
        A[index + 1], A[index] = A[index], A[index + 1]
    return A

def removeDuplicates(A):
    def removeDuplicates_helper(counter):

        while (counter < len(A)-1 and A[counter] == A[counter + 1]):
            del A[counter]
        if counter == len(A):
            return
        counter +=1
        removeDuplicates_helper(counter)

    counter = 0
    removeDuplicates_helper(counter)
    return len(A)

def diffPossible(A, B):
    A.sort()
    for start in range(0, len(A)):
        for end in range(len(A) - 1, -1, -1):
            if A[end] < B:
                break
            elif A[end] - A[start] == B and end != start:
                return 1
    return 0
def is_valid(row,col,n):
    return 0 <= row and row <= n and 0 <= col and col <= n

def diagonal(a):
    seen = set()
    ret = []
    n = len(a)
    for row in range(0, n):
        for col in range(0, n):
            x = a[row][col]
            if x in seen:
                continue
            to_add = []
            to_add.append(x)
            seen.add(x)
            u_row = row + 1
            u_col = col - 1
            while(is_valid(u_row, u_col, n - 1)):
                x = a[u_row][u_col]
                to_add.append(x)
                seen.add(x)
                u_row = u_row + 1
                u_col = u_col - 1
            ret.append(to_add)
    return ret

# trival solutionש
def is_step(num):
    str_rep = str(num)
    if len(str_rep) == 1: return True
    if abs(int(str_rep[0]) - int(str_rep[1])) == 1:
        for char in range(1, len(str_rep) - 1):
            if abs(int(str_rep[char]) - int(str_rep[char + 1])) != 1 or abs(
                            int(str_rep[char - 1]) - int(str_rep[char])) != 1:
                return False
    else:
        return False
    return True

def stepnum(A, B):
    ret = []
    for num in range(A, B + 1):
        if is_step(num):
            ret.append(num)
    return ret


def preix(words):
    ret = []
    index = 0
    while(words):
        cur = []
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for obj in words:
            cur.append(obj[index])
        un_index = find_uncommon(cur,d)
        if un_index == -1:
            index += 1
            continue
        ret.append(words[un_index][0:index+1])
        del words[un_index]
    return ret


def find_uncommon(cur, dict):
    for char in cur:
        dict[char] += 1
    for key in dict.keys():
        if dict[key] == 1:
            return cur.index(key)
    return -1
# עבור הערכים הבאים ['a', 'b'], ['x','y']
# אני רוצה להחזיר את זה
# [{'x': 'a', 'y': 'a'}, {'x': 'a', 'y': 'b'}, {'x': 'b', 'y': 'a'}, {'x': 'b', 'y': 'b'}]

def premutations(values, keys):
    v_premut = []
    for x in values:
        for y in values:
            for z in values:
                v_premut.append([x,y,z])
    print(v_premut)


def cont_sub_array(arr:list):
    # sums = []
    # for i in range(len(arr)):
    #     cur_sums = []
    #     cur_sums.append(arr[i])
    #     for j in range(i+1,len(arr)):
    #         cur_sums.append(cur_sums[j-1] + arr[j])
    #     sums.append(cur_sums)
    # print(sums)
    import numpy as np
    # args = np.argsort(arr)
    cur_max = -np.inf
    cur_last = -np.inf

    for i in range(len(arr)):
        if arr[i] > cur_last + arr[i]:
            cur_last = arr[i]
        else:
            cur_last += arr[i]

        if cur_last > cur_max:
            cur_max = cur_last
    print(cur_max)

def remove_dups_sorted(arr):
    import numpy as np
    cur_elem = arr[0]
    minimal_pointer = 1
    for i in range(1,len(arr)):
        if cur_elem < arr[i]:
            arr[minimal_pointer] = arr[i]
            cur_elem = arr[i]
            minimal_pointer += 1
    arr = arr[0:minimal_pointer]
    print(len(arr))
    print(arr)

def prettyPrint(A):
    import numpy as np
    rows = cols = A*2 -1
    ret = np.zeros((rows,cols),dtype=int)
    for i in range(rows):
        if i == A: # mid
            break
        if i > 0:
            ret[i] = ret[i-1]
        for j in range(i,cols-i):
            ret[i][j] = A-i
    for i in range(0,A):
        ret[rows-1-i] = ret[i]
    print(ret)

def LongestConsecutiveSequence(A):
    d = {}
    for i in A:
        if i in range(45,55):
            print(i)
        if i in d.keys():
            continue
        if i + 1 in d.keys() and i - 1 in d.keys():
            d[i + 1] += d[i - 1] + 1
            d[i - 1] = d[i + 1]
            d[i] = d[i + 1]
        else:
            if i + 1 in d.keys():
                d[i + 1] += 1
                d[i] = d[i + 1]
            if i - 1 in d.keys():
                d[i - 1] += 1
                d[i] = d[i - 1]
            elif i not in d.keys():
                d[i] = 1
    return (max(d.values()))





def longest(A):
    s = set(A)
    m = min(min(A),0)
    t = max(A)
    r = [0] * (abs(t - m) + 1)

    for i in range(0,abs(t-m) +1):
        if i+m in s:
            r[i] = 1
    cur_counter = 0
    max_counter = 0
    for j in r:
        if j == 1:
            cur_counter += 1
        else:
            cur_counter = 0

        if cur_counter > max_counter:
            max_counter = cur_counter
    return max_counter


if __name__ == '__main__':
    # cont_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    # remove_dups_sorted([1,1,1,1,2,3,4,5,5,6,7])
    # print(LongestConsecutiveSequence( [ 50, 51, 15, 101, 23, 66, 69, 24, 75, 40, 30, 10, 61, 73, 95, 119, 106, 60, 26, 111, 54, 79, 18, 28, 72, 110, 37, 63, 5, 102, 53, 42, 49, -4, -2, 64, 93, 117, 103, 115, -5, 87, 47, 12, 48, 1, 9, 91, 85, -3, 68, 76, 59, 38, 35, 45, 0, 78, 62, 70, 46, 90, 52, 3, 83, 43, 11, 89, 21, 80, 77, 33, 17, 92, 113 ]))
    # print(longest([ 50, 51, 15, 101, 23, 66, 69, 24, 75, 40, 30, 10, 61, 73, 95, 119, 106, 60, 26, 111, 54, 79, 18, 28, 72, 110, 37, 63, 5, 102, 53, 42, 49, -4, -2, 64, 93, 117, 103, 115, -5, 87, 47, 12, 48, 1, 9, 91, 85, -3, 68, 76, 59, 38, 35, 45, 0, 78, 62, 70, 46, 90, 52, 3, 83, 43, 11, 89, 21, 80, 77, 33, 17, 92, 113 ]))
    # print(find_two_primes(400000000000))
    # print(longest([-5]))
    print(longest([2,3,4,5,6]))
    # print(downsample([[1,2,3],[4,5,6],[7,8,9]]))
    # A = [[1,2,3],[4,5,6],[7,8,9]]
    # A = [[1,2],[3,4]]
    # print(stepnum(10,20))

    # print(premutations(['a', 'b','c'], ['x', 'y']))


