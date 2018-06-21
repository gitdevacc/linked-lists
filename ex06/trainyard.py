import LinkedLists
def trainyard(train1,train2):
    assert isinstance(train1, LinkedLists.SinglyList)
    assert isinstance(train2, LinkedLists.SinglyList)
    train1.merge(train2)
    train1.sort_asc()
    train1.remove(train1.head,train1.head.c)
    train1.remove(train1.head,train1.head.c)