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
    def remove(self, list_head, val):
        if isinstance(val, Node):
            val1=val
            if val1.c==list_head.c:
                del val
                return val1.n  
            self.remove(list_head, val1.c)
        else:
            if list_head.c==val:
                val1=list_head
                del list_head  
                return val1.n
            for element in self:
                if element.n==val:
                    temp=element.n
                    element.n=temp.n 
                    del temp
        return list_head
a=Node('Green')
b=Node('Eggs')
c=Node('And')
d=Node('Spam')
linkedlist=SinglyList()
linkedlist.add_head(a)
linkedlist.add_tail(a,b)
linkedlist.add_tail(a,c)
linkedlist.add_tail(a,d)
linkedlist.print_list(linkedlist.remove(a, b))
