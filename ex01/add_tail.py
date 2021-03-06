class Node(object):
    def __init__(self, content):
        if content is None: 
            raise ValueError('Node must have content')
        self.c= content
        self.n=None
    def __str__(self):
        return str(self.c)
    @property
    def content(self):
        return self.c
    @content.setter
    def content(self, val):
        self.c=val
    @property
    def next(self):
        return self.n 
    @next.setter
    def next(self, val):
        self.n=val
class SinglyList(object):
    def __init__(self):
        self.h=None
    def __iter__(self):
        current=self.head
        while current:
            yield current
            current=current.next
    @property
    def head(self):
        return self.h
    @head.setter
    def head(self, val):
        self.h=val
    def isEmpty(self):
        return self.head==None
    def add_head(self, node):
        if self.isEmpty():
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def add_tail(self, list_head, val):
        if isinstance(val, Node):
            current=list_head
            while current.n!=None:
                current=current.n
            current.n=val
        else:
            node=Node(val)
            self.add_tail(list_head, node) 
    def print_list(self, list_head):
        c=list_head
        while c.n!=None:
            print(c.c)
            c=c.n
        print(c.c)
    
a=Node('Green')
b=Node('Eggs')
c=Node('And')
d=Node('Spam')
linkedlist=SinglyList()
linkedlist.add_head(a)
linkedlist.add_tail(a,b)
linkedlist.add_tail(a,c)
linkedlist.add_tail(a,d)
linkedlist.print_list(a)

