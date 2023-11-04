# in python list is a Dynamic Array
# static array is not mutable array, which functions like a tuple

# При работе с обычным списком, когда происходит insert, то список сначала двигает все элементы
# на один от точки вставки нового элемента и потом вставляет, а если первоначально выделенное место
# для списка закончилось, то при инсерте, список скопируется в новые слоты, увеличенные колисчетвом вдвое,
# и только после этого вставит обновленный список с новым элементом. Связный список позволяет избежать этого
# и делать при вставке просто менять ссылку с одного элемента на другой, а новый элемент указывает на следующий.
# Вставки или удаление сначала списка - O(1), так как вставляется с начачала и модифицируются ссылки, а если в конце,
# то O(n), так как нужно проитерироваться по списку, чтобы дойти до конца.

# + for Linked List
# Dont need to preallocate space
# Insertion is easier

# operation, Array, Linked List
# indexing, O(1), O(n),
# insert, delete at start, O(n), O(1)
# insert, delete at end, O(1), O(n)
# Insert in the middle, O(n), O(n)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):  # insert at beginning
        node = Node(data, self.head)  # pointer to previous head node
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index not valid")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # need to stop at the previous element to change the link
                # changing to the one that goes after the one the we want to delete
                int.next = itr.next.next
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Index not valid")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head 
        while itr: 
            if count == index - 1: 
                node = Node(data, itr.next) # we are at the previous element so the next element will be the link
                itr.next = node
                break

            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):

        itr = self.head
        while itr: 
            if itr.data == data_after: 
                node = Node(data_to_insert, itr.next)
                itr.next = node

            itr = itr.next
            

ll = LinkedList()
ll.insert_values(["foo", "faa", "fee", "fuu"])
ll.print()
ll.insert_after_value("faa", "fyy")
ll.print()