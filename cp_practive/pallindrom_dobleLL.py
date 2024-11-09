class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self, data):
        new_node=Node(data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
        if self.tail is None:
            self.tail=new_node

    def is_palindrome(self):
        curr=self.head
        runner=self.tail
        while curr is not None and runner is not None:
            if curr.data!=runner.data:
                return False
            curr=curr.next
            runner = runner.prev
        return True
    
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.push(1)
doubly_linked_list.push(4)
doubly_linked_list.push(3)
doubly_linked_list.push(4)
doubly_linked_list.push(1)

print(doubly_linked_list.is_palindrome()) 