import string
from collections import defaultdict

def is_unique(s):
    dic = {}
    for c in s:
        if c in dic.keys():
            dic[c] += 1
        else: dic[c] = 1
    return max(dic.values()) <= 1

# print(is_unique('1243'))

ALPHABAT = (list(string.ascii_lowercase))

def is_premutation(str1, str2):

    dic1 = {}
    dic2 = {}
    if len(str1) != len(str2): return False
    for i in range(0, len(str1)):
        cur_char_1 = str1[i]
        cur_char_2 = str2[i]
        if cur_char_1 in dic1.keys():
            dic1[cur_char_1] += 1
        else: dic1[cur_char_1] = 1

        if cur_char_2 in dic2.keys():
            dic2[cur_char_2] += 1
        else:
            dic2[cur_char_2] = 1

    return dic1 == dic2

# print(is_premutation('abc', 'bad'))




def URLfiy(str1):

    l = list(str1)
    for index, v in enumerate(l):
        if v == ' ':
            l[index] = '%20'
    return ''.join(l)

# print(URLfiy('hello mister jonson as as ss s s'))


def prem_of_poli(str1):


    d = {}
    for c in str1:
        if c == ' ': continue
        if c in d.keys(): d[c] += 1
        else: d[c] = 1

    odd = False
    for value in d.values():
        if value % 2 != 0:
            if odd is False: odd = True
            else: return False
    return True

# print(prem_of_poli('tact coa'))



def one_way(str1, ret):
    one_chance = False

    if len(str1) +1 == len(ret): # might be inserable
        cur = 0
        for char1 in range(len(str1)):
            print(ret[char1])
            print(str1[cur])
            if ret[char1] != str1[cur]:
                if one_chance: return False
                else:
                    one_chance = True
                    char1 += 1
                    break
            else:
                cur += 1
        return True

    elif len(str1) == len(ret): #might be one change
        for c in range(len(str1)):
            if ret[c] != str1[c]:
                if one_chance: return False
                one_chance = True
        return True
    elif len(str1) -1 == len(ret): # might be removable
        cur = 0
        for char1 in range(len(ret)):
            if ret[char1] != str1[cur]:
                if one_chance:
                    return False
                else:
                    one_chance = True
                    cur += 1
                    break
            else:
                cur += 1
        return True

    else:
        return False

print(one_way('daba', 'daba'))

def commpars(str1):

    ret = str1[0]
    count = 0
    for c in str1:
        if ret[len(ret)-1] == c:
            count +=1
        else:
            ret += str(count)
            ret += c
            count = 1
    ret += str(count)
    return ret


print(commpars('ammmmaaaabbba'))

def roatate_matrix(matrix):

    for row in range(len(matrix),0):
        for col in range(len(matrix[0]),row):
            matrix[row][col],matrix[col][row]  =  matrix[col][row], matrix[row][col]

    return matrix

matrix = [[1,1,1],[2,2,2],[3,3,3]]
# print(matrix)
# print(roatate_matrix([[1,1,1],[2,2,2],[3,3,3]]))


def zero_matrix(matrix):

    dead_rows_cols = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                dead_rows_cols.append(row)
                dead_rows_cols.append(col)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in dead_rows_cols or col in dead_rows_cols:
                matrix[row][col] = 0

    return matrix



def get_elem(matrix, elem):
    def get_col(matrix, elem):
        mid = len(matrix) // 2
        mid_elem_start = matrix[mid][0]
        mid_elem_end = matrix[mid][-1]
        if mid_elem_start <= elem <= mid_elem_end:
            return matrix[mid]
        elif len(matrix) == 1:
            print('Not in matrix')
            return None
        elif elem < mid_elem_start:
            return get_col(matrix[0:mid], elem)
        elif elem > mid_elem_end:
            return get_col(matrix[mid:], elem)

    def get_final_elem(column, elem):
        if len(column) == 1 and column[0] != elem:
            print('Elem not in matrix')
            return None
        mid = len(column) // 2
        candidate = column[mid]
        if candidate == elem:
            return candidate
        elif elem < candidate:
            return get_final_elem(column[0:mid], elem)
        elif elem > candidate:
            return get_final_elem(column[mid:], elem)
    start = matrix[0][0]
    end = matrix[-1][-1]
    if elem < start or elem > end:
        print('elem not in matrix')
        return None
    col = get_col(matrix,elem)
    if not col:
        return
    element = get_final_elem(col, elem)
    print(element)


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.level = 0
        self.left = None
        self.right = None

def tree_lists(node):

    def dfs_helper(node:Node, parent):
        if not node:
            return
        if parent:
            node.parent = parent
            node.level = node.parent.level + 1
        dfs_helper(node.left, node)
        dfs_helper(node.right, node)

    def create_level_lists(node, levels:list):
        if not node:
            return
        if len(levels) <= node.level:
            levels.append([])
        levels[node.level].append(node.value)
        create_level_lists(node.left, levels)
        create_level_lists(node.right, levels)
    levels = []
    dfs_helper(node, None)
    create_level_lists(node, levels=levels)
    print(levels)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(3)
    root.right.left = Node(3)
    root.right.right = Node(3)
    tree_lists(root)

#
# if __name__ == '__main__':
#     # get_elem([[1, 2], [4, 5], [8,9]],2)
#     get_elem([[1, 2,3], [5,6,7], [8,9,10]],7)

# print(zero_matrix([[1,1,1],[2,2,2],[3,3,3]]))



