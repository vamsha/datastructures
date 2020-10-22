class node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def insertAtFirst(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, data):
        new_node = node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def append(self, data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while(temp.next):
            temp=temp.next

        temp.next=new_node

    def insertAfterGivenKey(self, key, data):
        new_node = node(data)

        temp=self.head
        while(temp):
            # print(temp.data)
            if(temp.data == key):
                # print("inside if condition")
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next

    def insertBeforeGvenKey(self, key, data):
        new_node = node(data)

        first = self.head
        if first.data == key:
            new_node.next = first
            self.head = new_node
        else:
            second = self.head
            while(first):
                if(first.data == key):
                    new_node.next = second.next
                    second.next = new_node
                    break
                second = first
                first = first.next

    def deleteNode(self, key):
        temp = self.head

        if temp.data == key:
            self.head = temp.next
            temp = None
            return 
        else:
            prev = temp
            temp = temp.next
            while(temp):
                if(temp.data==key):
                    prev.next = temp.next
                    temp = None
                    break
                prev = temp
                temp = temp.next

    def deleteayPosition(self, key):
        if self.head == None:
            return
        temp = self.head
        if key==0:
            self.head = temp.next
            temp = None
            return

        for i in range(key-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None: 
            return 
        if temp.next is None: 
            return

        temp.next = temp.next.next

if __name__=='__main__':
    llist = Linkedlist()

    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third

    llist.insertAtFirst(15)

    llist.insertAfter(llist.head.next,50)

    llist.insertAfterGivenKey(2,200)

    llist.insertBeforeGvenKey(3,150)

    llist.append(1000)

    llist.deleteNode(1000)

    llist.deleteayPosition(1)

    llist.printlist()