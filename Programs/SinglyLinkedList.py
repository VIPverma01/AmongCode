class Node:
    def __init__(self, data=None, ptr=None):
        self.data = data
        self.next = ptr
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data, pos):
        if self.head:
            ptr = self.head
            if pos==0:
                self.addAtStart(data)
            else:
                index = 0
                while (ptr.next and index<pos):
                    index+=1
                    if index == pos:
                        break
                    ptr=ptr.next
                temp = Node(data)
                temp.next = ptr.next
                ptr.next = temp


    def addAtStart(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        
    def addAtEnd(self, data):
        temp = Node(data)
        if self.head:
            ptr = self.head
            while (ptr.next):
                ptr = ptr.next
            ptr.next = temp
        else:
            self.head = temp
    
    def remove(self, pos): 
  
        if self.head == None: 
            return 
        temp = self.head 
  
        if pos == 0: 
            self.head = temp.next
            temp = None
            return 

        for i in range(pos-1): 
            temp = temp.next
            if temp is None: 
                break

        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next

        temp.next = None  
        temp.next = next 

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    def clear(self):
        self.head = None

    def isEmpty(self):
        return self.head==None

    def display(self):
        if self.head:
            temp = self.head
            while (temp):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("Empty Linked List")
    
    def length(self):
        count=0
        if self.head:
            ptr = self.head
            while ptr:
                count+=1
                ptr = ptr.next
        return count

if __name__ =='__main__':
    # l = LinkedList(Node(10, Node(20, Node(30, Node(40, Node(50))))))
    l = LinkedList()
    print("Linked List is "+("Empty" if l.isEmpty() else "NotEmpty"))
    print("\nLength is:",l.length())

    print("\nAdding at end")
    l.addAtEnd(10)
    l.addAtEnd(20)
    l.display()
    
    print("\nLength is:",l.length())

    print("\nAdding at start")
    l.addAtStart(-1)
    l.addAtStart(-2)
    l.display()
    
    print("\nLinked List is "+("Empty" if l.isEmpty() else "NotEmpty"))

    print("\nAdding at desired position")
    l.add(-5,1)
    l.add(-6,2)
    l.display()

    print("\nRemoving elements at given position")
    l.remove(l.length()-1)
    l.remove(0)
    l.remove(2)
    
    l.display()
    
    print("\nReversing the linked list")
    l.reverse()
    l.display()
    