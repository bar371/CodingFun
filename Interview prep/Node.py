class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def set_left_child(self, value):
        left_child = Node(value)
        self.left_child = left_child

    def set_right_child(self,value):
        right_child=Node(value)
        self.right_child= right_child

    def Node_say_hey(self):
        return 'hey'

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value)
        if self.right_child:
            self.right_child.in_order()
    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value)

    def __repr__(self):
        return 'my value is ' + str(self.value) + ' my right child is: ' + str(self.right_child.value)  + ' my left child is: ' + str(self.left_child.value)

    def DFS(self, root):
        if root == None:return
        visit(root)
        root.visited = True
        for node in root.ad_list:
            if node.visited == False:
                self.DFS(node)

    def BFS(self, root):
        if root == None: return
        new_queue = quit()
        new_queue.enqeue(root)

        while( not new_queue.is_empty()):
            cur = new_queue.deqeue()
            visit(cur)
            cur.visited = True
            for node in cur.ad_list:
                if cur.visited == False:
                    new_queue.enqeue(node)




class Tree:
    def __init__(self, root):
        self.root = root

    # def delete_node(self, value):
    #     pass

if __name__ == '__main__':
    pass
    # node_1 = Node(5, Node(2,Node(1) ,Node(4)), Node(10))
    # node_1.post_order()
    # tree = Tre/e(node_1)
    # a = no/de_1.Node_say_hey()
    # print(a)
    # node_1.set_left_child(4)
    # node_1.set_right_child(3)
    # print(node_1)