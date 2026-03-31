# OBJECT ORIENTED
# 2 Istilah: CLASS & OBJECT
# CLASS: seperti cetakan, tempat membuat cupcakes, cookie cutter
# OBJECT: cupcakes, cookies yang kita buat yang ditaruh di cetakan/cookie cutter (CLASS)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# The code defines a Node class and a LinkedList class to create and manage a linked list data structure.
# The LinkedList class has methods to append new nodes and display the list.