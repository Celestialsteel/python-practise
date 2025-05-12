class LinkedlistNode:
    def __init__(next,data):
        data = data
        next = None
        prev = None
        head = None

    def insert_at_end(self,data):
        new_node = LinkedlistNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while (current_node.next):
                current_node = current_node.next
            current_node.next = new_node    

    def insert_at_start(data):
        new_node = LinkedlistNode(data)
        if head is None:
            head = new_node
            return
        else:
            new_node.next = head
            head = new_node 

    def insert_at_index(self,index, data):
       if index == 0:
          self.insert_at_start(data)
          return 
        
       position = 0
       current_node = self.head
       while current_node is not None and position+1 != index:
                position += 1
                current_node = current_node.next
       
       if current_node is not None:
            new_node = LinkedlistNode(data)
            new_node.next = current_node.next
            current_node.next = new_node 
       else:
               print("Index out of range")

    def delete_at_index(self,index):
         if self.head is None:
             return

         position = 0 
         current_node = self.head
         if index == 0:
              self.remove_node()
              return   
                  
         while current_node is not None and position < index -1 :
             position += 1
             current_node = current_node.next

         if current_node is None or current_node.next is None:
             print("Index out of range")
             return
         else:
             current_node.next = current_node.next.next

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False 

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        