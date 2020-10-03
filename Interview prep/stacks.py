class Stack():
    def __init__(self):
        self.stack = []
        self.size = 0

    def pop(self):
        ret = self.stack.pop()
        self.size -= 1
        return ret

    def push(self, obj):
        self.stack.append(obj)
        self.size += 1

    def peek(self):
        if self.stack != []:
            return self.stack[-1]
        else: return None

    def sort_stack(self):
        temp_stack = Stack()
        while(self.peek() != None):
            temp = temp_stack.peek()
            cur = self.pop()
            if temp == None:
                temp_stack.push(cur)
            elif temp > cur:
                ret = temp_stack.pop()
                temp_stack.push(cur)
                temp_stack.push(ret)
            else:
                temp_stack.push(cur)
        self.stack = temp_stack

class Queue:

    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def push(self, obj):
        self.stack_a.push(obj)

    def pop(self):
        pass

        # if self.stack_b.is_empty():
        #     while(self.stack_a not empty):
        #         self.stack_b.push(self.stack_a.pop())




class set_of_stacks():
    class Stack():
        def __init__(self):
            self.stack = []
            self.size = 0

        def pop(self):
            self.stack.pop()
            self.size -= 1

        def push(self, obj):
            self.stack.append(obj)
            self.size += 1

        def peek(self):
            return self.peek()

    def __init__(self, n):
        self.num_of_stacks = 0
        self.list_of_stacks = [set_of_stacks.Stack()]
        self.threshold = n

    def push(self, obj):
        if self.list_of_stacks[self.num_of_stacks].size < self.threshold:
            self.list_of_stacks[self.num_of_stacks].push(obj)
        else:
            self.list_of_stacks.append(set_of_stacks.Stack())
            self.num_of_stacks += 1
            self.push(obj)
    def pop(self):
            if self.list_of_stacks[self.num_of_stacks].size == 0:
                self.list_of_stacks.remove(self.list_of_stacks[self.num_of_stacks])
                self.num_of_stacks -= 1
            self.list_of_stacks[self.num_of_stacks].pop()
    def pop_at(self,index):
        stack_to_pop = index // self.threshold
        index_to_pop = index % self.threshold
        temp = set_of_stacks.Stack()
        for i in range(index_to_pop-1):
            temp.push(self.list_of_stacks[stack_to_pop].pop())
        self.list_of_stacks[stack_to_pop].pop()
        for i in range(index_to_pop):
            self.list_of_stacks[stack_to_pop].push(temp.pop())


if __name__ == '__main__':
    pass
    # set = Stack()
    # set.push(5)
    # set.push(4)
    # set.push(3)
    # set.push(4)
    # set.push(1)
    # # # set.pop()
    # # # set.pop()
    # # # set.pop_at(3)
    # set.sort_stack()
    # print(set.stack)