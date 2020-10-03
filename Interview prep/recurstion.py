def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def permutList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res


def range_to_n(n, stack):
    if (n == 0):
        print('we have reached the end')
        stack.append(n)
        print('we have just appened', n)
        return
    stack.append(n)
    print('we just appened: ', n)
    range_to_n(n-1, stack)
    print('we are now coming back from:' , n)

def make_range_of_n(n):
    stack = []
    range_to_n(n, stack)
    print(stack)


def num_of_steps(n, dic):
    counter = 0
    if n >= 1:
        if n-1 in dic:
            counter += dic[n-1]
        else:
            ret = num_of_steps(n-1, dic)
            dic[n-1] = ret
            counter += ret
    if n >= 2:
        if n-2 in dic:
            counter += dic[n-2]
        else:
            ret = num_of_steps(n-2, dic)
            dic[n-2] = ret
            counter += ret
    if n >= 3:
        if n-3 in dic:
            counter += dic[n-3]
        else:
            ret = num_of_steps(n-3, dic)
            dic[n-3] = ret
            counter += ret
    if n == 0:
        counter += 1
    return counter

# print(num_of_steps(289,{}))

def Magic(arr):
    mid = len(arr)//2

    if arr == []:
        return False

    if arr[mid] == mid:
        return True


    if arr[mid] > mid:
        if arr[mid] >= 0 :
           return Magic(arr[0:mid])
    elif arr[mid] < len(arr):
            return Magic(arr[mid:len(arr)])
    return False

def power_set(set:set , pow_set:set):
    pass


arr = [1,1]
def make_fib_arr(n):
    print(len(arr))
    if n-2 == 0:
        return
    arr.append(arr[len(arr)-1] + arr[len(arr)-2])
    make_fib_arr(n-1)

def magic(arr, start, end):
    if end < start:
        return None
    middle = (start + end) // 2
    if middle == arr[middle]:
        return middle

    if arr[middle] > middle : return magic(arr, start, middle)
    else: return magic(arr, middle +1 , end)

def coins(n, ways):
    if n-25 > 0:
        ways = coins(n-25, ways)
    elif n-25 == 0:
        ways +=1

    if n-10 > 0:
        ways = coins(n-10, ways)
    elif n-10 == 0:
        ways += 1

    if n-5 > 0:
        ways = coins(n-5, ways)
    elif n-5 == 0:
        ways +=1

    if n-1 > 0:
        ways = coins(n-1, ways)
    elif n-1 == 0:
        ways+=1
    return ways



def anagrams(strings):
    def get_char_dict(string):
        dict_rep = {}
        for char in list(string):
            if char in dict_rep.keys():
                dict_rep[char] += 1
            else:
                dict_rep[char] = 1
        return dict_rep

    anagrm_sorted = []
    while strings:
        cur_string = strings.pop()
        anagrm_sorted.append(cur_string)
        dict_rep = get_char_dict(cur_string)
        for string_iter in strings:
            if string_iter == cur_string:
                continue
            string_iter_dict = get_char_dict(string_iter)
            if dict_rep == string_iter_dict:
                anagrm_sorted.append(string_iter)
                del strings[strings.index(string_iter)]
    return anagrm_sorted

def rotated(arr, start, end, x):
    if end < start :
        return None
    middle = (end + start) //2
    if arr[middle] == x:
        return middle

    elif x < arr[middle] or x >= arr[start]:
        return rotated(arr, start, middle-1, x)

    elif x > arr[middle] and x < arr[end]:
        return rotated(arr, middle, end ,x)

def interveaveing(arr):
    arr.sort()
    start = 0
    ret = []
    for end in range(len(arr), 0):
        if start == end:
            break
        ret.append(arr[end])
        ret.append(arr[start])
        start += 1
    return ret

def prem_without_dup(s:str):
    ret = set(s)
    ret.add(s)
    char_set = list(set(s))
    char_set_len = len(char_set)
    for i in range(char_set_len):
        for j in range(char_set_len):
            if i == j:
                continue
            else:
                cur_sum = char_set_len - j
                while cur_sum > 0:
                    cur_ret = str(char_set[j + cur_sum:])
                    cur_ret = cur_ret.strip("\n")
                    cur_ret = cur_ret.strip("\'")
                    cur_ret = cur_ret.strip("[")
                    cur_ret = cur_ret.strip("]")
                    print(cur_ret)
                    print(len(cur_ret))
                    if len(cur_ret) > 2:
                        ret.add(str(char_set[i] + cur_ret))
                    else:
                        ret.add(str(char_set[i]))
                    cur_sum -= 1
    print(ret)



def prem_with_out_dups_2(s:str):
    def helper(cur_s:str, ret:set):
        if len(cur_s) == 1:
            return cur_s
        for i,c in enumerate(cur_s):
            c_ret = c + helper(cur_s.replace(c,''), ret)
            if len(c_ret) == len(s):
                ret.add(c_ret)
    ret = set()
    helper(s, ret)
    print(ret)


def prem_without_dups_3(s:str):
    def helper(given_s:set,cur_ret:str, all_ret:set):
        if len(given_s) == 0:
            all_ret.add(str(cur_ret))
            return

        for c in given_s:
            helper(given_s - {c}, cur_ret + c, all_ret)

    ret = set()
    helper(set(s), '',ret)
    print(ret)

if __name__ == '__main__':
    prem_without_dups_3('abs')






#
# def plus(a:int, b:int) -> int:
#     return a+b

#
# if __name__ == '__main__':
#     prem_without_dup("abs")
#     print(interveaveing([1,4,5,3,5,1,2]))
    # print(anagrams(('hey my name is K please eman give ym yeh si').split(' ')))
    # arrr= [15,16,19,20,25,1,3,4,5,7,10,14]
    # print(rotated(arrr, 0, len(arrr), 5))