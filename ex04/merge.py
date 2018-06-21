class Node():
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
class SinglyList():
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
        current=list_head
        if isinstance(val, Node):
            val1=val.c 
            if current.c==val1:
                del current.c 
                node_head=current.n
                return node_head
            while current.n!=None:
                if current.n==val1:
                    temp=current.n
                    current.n=temp.n 
                else:
                    current=current.n
            return list_head
        else:
            if current.c==val:
                del current.c 
                current=current.n
            while current.n!=None:
                if current.n==val:
                    temp=current.n
                    current.n=temp.n 
                else:
                    current=current.n
        return list_head
    def has_cycle(self,list_head):
        current=list_head
        while current.n:
            current=current.n
            if current.c==list_head:
                return True
        return False
    def merge(self,train2):
        assert isinstance(train2, SinglyList)
        if self.has_cycle(self.head):
            raise Exception ("Circularly linked lists cannot be merged.")
        for element in train2:
            self.add_tail(self.head, element.c)
        return self 
a=Node('Green')
b=Node('Eggs')
linkedlist=SinglyList()
linkedlist.add_head(a)
linkedlist.add_tail(a,b)
linkedlists=SinglyList()
linkedlists.add_head(b)
linkedlists.add_tail(b,a)
linkedlist.merge(linkedlist)