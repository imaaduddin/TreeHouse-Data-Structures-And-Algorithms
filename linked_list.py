class Node:
  # An object for sotring a single node of a linked list
  # Models two attributes - data and the link to the next node in the list 
  data = None
  next_node = None

  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return "<Node data: %s>" % self.data 


class LinkedList:
  # Singly linked list 

  def __init__(self):
    self.head = None
  
  def is_empty(self):
    return self.head == None
  
  def size(self):
    # Returns the number of nodes in the list, takes O(n) time
    current = self.head
    count = 0

    while current != None:
      count = count + 1
      current = current.next_node
    return count

    def add(self, data):
      # Adds new Node containing data at head of the list 
      # Takes O(1) time
      new_node = Node(data)
      new_node.next_node = self.head
      self.head = new_node
      
      

