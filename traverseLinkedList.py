from LinkedList import Node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def traverseLinkedList(head1):
	while head1 != None:
		print (head1.val)
		head1 = head1.next
traverseLinkedList(head)