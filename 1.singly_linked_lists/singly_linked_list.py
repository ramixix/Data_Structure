
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class Linkedlist:
    def __init__(self):
        self.head = None

#   -------------------------------------------------------------------------------------------
    def is_list_empty(self):
        return self.head == None

#   -------------------------------------------------------------------------------------------

    def add_node_to_front(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

#   -------------------------------------------------------------------------------------------

    def remove_node_from_front(self):
        if(self.is_list_empty()):
            print("List is empty!!!")
        else:
            temp = self.head
            self.head = temp.next_node
            del temp

#   -------------------------------------------------------------------------------------------

    def add_node_to_back(self, value):
        if(self.is_list_empty()):
            new_node = Node(value)
            self.head = new_node
            return
    
        temp = self.head
        while(temp.next_node != None):
            temp= temp.next_node
        new_node = Node(value)
        temp.next_node = new_node

#   -------------------------------------------------------------------------------------------

    def remove_node_from_back(self):
        if(self.is_list_empty()):
            print("List is empty!!!")
            
        else:
            if(self.head.next_node == None):
                del self.head
                self.head = None
            else:
                temp = self.head
                while((temp.next_node).next_node != None):
                    temp = temp.next_node
                del temp.next_node
                temp.next_node = None

#   -------------------------------------------------------------------------------------------

    def print_list(self):

        if(self.is_list_empty()):
            print("List is empty!!!")
        else:
            temp = self.head
            while(temp.next_node != None):
                print(f"{temp.value} -> ", end="")
                temp = temp.next_node
            print(f"{temp.value}")                

#   -------------------------------------------------------------------------------------------

    def add_item_by_order(self, value):
        new_node = Node(value)

        if(self.is_list_empty()):
            self.head = new_node
        
        else:
            temp = self.head
            
            if(value < temp.value):
                new_node.next_node = temp
                self.head = new_node
                return
        
            while(temp.next_node != None and value >= (temp.next_node).value):
                temp = temp.next_node
            
            new_node.next_node = temp.next_node
            temp.next_node = new_node

#   -------------------------------------------------------------------------------------------

    def remove_specific_node(self, value):
        if(self.is_list_empty()):
            print("List is empty!!!")
        
        else:
            if(self.head.value == value):
                temp = self.head
                self.head = self.head.next_node
                del temp
                return

            temp = self.head
            temp2 = self.head.next_node

            while(temp2 != None):
                if(temp2.value == value):
                    temp.next_node = temp2.next_node
                    break 
                temp = temp.next_node
                temp2 = temp2.next_node
            
            if(temp2 == None):
                print(f"There is not item with a value of {value}")
                return

            del temp2
            
#   -------------------------------------------------------------------------------------------

    def merge_two_list(self, list2):
        merged_list = Linkedlist()
        list1_tmp_head = self.head
        list2_tmp_head = list2.head

        while(list1_tmp_head != None or list2_tmp_head != None):
            if(list1_tmp_head != None and list2_tmp_head != None):
                while(list1_tmp_head != None and list2_tmp_head != None):
                    if(list1_tmp_head.value < list2_tmp_head.value):
                        merged_list.add_node_to_back(list1_tmp_head.value)
                        list1_tmp_head = list1_tmp_head.next_node
                    else:
                        merged_list.add_node_to_back(list2_tmp_head.value)
                        list2_tmp_head = list2_tmp_head.next_node

            if(list1_tmp_head == None):
                while(list2_tmp_head != None):
                    merged_list.add_node_to_back(list2_tmp_head.value)
                    list2_tmp_head = list2_tmp_head.next_node

            if(list2_tmp_head == None):
                while(list1_tmp_head != None):
                    merged_list.add_node_to_back(list1_tmp_head.value)
                    list1_tmp_head = list1_tmp_head.next_node
                    
        return merged_list

    def merge_two_list_by_order(self, list2):
        merged_list = Linkedlist()
        list1_tmp_head = self.head
        list2_tmp_head = list2.head

        while(list1_tmp_head != None):
            merged_list.add_item_by_order(list1_tmp_head.value)
            list1_tmp_head = list1_tmp_head.next_node
                
        
        while(list2_tmp_head != None):
            merged_list.add_item_by_order(list2_tmp_head.value)
            list2_tmp_head = list2_tmp_head.next_node
        merged_list.print_list()
        return merged_list
        #     if(self.head == None):
        #         merged_list.add_node_to_front()

#   -------------------------------------------------------------------------------------------
#   -------------------------------------------------------------------------------------------

list1 = Linkedlist()
list2 = Linkedlist()

list1.add_node_to_front(6)
list1.add_node_to_back(7)
list1.add_node_to_front(3)
list1.add_node_to_front(1)
list1.add_node_to_front(57)
list1.add_node_to_front(723)
list1.add_node_to_front(74)
list1.add_node_to_back(3)
list1.add_node_to_back(0)
list1.add_node_to_back(5)
list1.add_node_to_front(5)
list1.add_node_to_back(65)
list1.add_node_to_front(1)
list1.add_node_to_back(57)
list1.add_node_to_back(65)




list2.add_node_to_front(0)
list2.add_node_to_front(5)
list2.add_node_to_front(65)



list1.print_list()
list2.print_list()
list3 = list1.merge_two_list(list2)
list4 = list1.merge_two_list_by_order(list2)
list3.print_list()
# list4.print_list()
