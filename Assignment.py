# adding a new node
def addAtStart(self, data):
    newNode = Node(data);
    # Checks if the list is empty.
    if self.head.data is None:
        # If list is empty, both head and tail would point to new node.
        self.head = newNode;
        self.tail = newNode;
        newNode.next = self.head;
    else:
        # Store data into temporary node
        temp = self.head;
        # New node will point to temp as next node
        newNode.next = temp;
        # New node will be the head node
        self.head = newNode;
        # Since, it is circular linked list tail will point to head.
        self.tail.next = self.head;

        class CircularLinkedList:
            cl = CreateList();

            # Adding 1 to the list
            cl.addAtStart(1);
            cl.display();
            # Adding 2 to the list
            cl.addAtStart(2);
            cl.display();
            # Adding 3 to the list
            cl.addAtStart(3);
            cl.display();
            # Adding 4 to the list
            cl.addAtStart(4);
            cl.display()

#Deleting a particular node (referenced by the location)
#Delete all the nodes from the list which contain a particular data say a number 5

def deleteNode(self, key):
    # Store head node
    temp = self.head

    # If head node itself holds the key to be deleted
    if (temp is not None):
        if (temp.data == key):
            self.head = temp.next
            temp = None
            return

    # Search for the key to be deleted, keep track of the
    # previous node as we need to change 'prev.next'
    while (temp is not None):
        if temp.data == key:
            break
        prev = temp
        temp = temp.next

    # if key was not present in linked list
    if (temp == None):
        return

    # Unlink the node from linked list
    prev.next = temp.next

    temp = None

    # Utility function to print the linked LinkedList


def printList(self):
    temp = self.head
    while (temp):
        print(" %d" % (temp.data)),
        temp = temp.next


# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()

# Delete the complete linked list
def push(self, new_data):
    # Allocate the Node &
    # Put in the data
    new_node = Node(new_data)

    # Make next of new Node as head
    new_node.next = self.head

    # Move the head to point to new Node
    self.head = new_node


# Use push() to construct below
# list 1-> 12-> 1-> 4-> 1
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    print("Deleting linked list")
    llist.deleteList()

    print("Linked list deleted")

#Display the linked list
def display(self):
    # Node current will point to head
    current = self.head;

    if (self.head == None):
        print("List is empty");
        return;
    print("Nodes of singly linked list: ");
    while (current != None):
        # Prints each node by incrementing pointer
        print(current.data),
        current = current.next;


sList = SinglyLinkedList();

# Add nodes to the list
sList.addNode(1);
sList.addNode(2);
sList.addNode(3);
sList.addNode(4);

# Displays the nodes present in the list
sList.display();

#Display the inverted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create and Handle list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Head of list

    # Method to reverse the list
    def reverse(self, head):

        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head

        # Reverse the rest list
        rest = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest

    # Returns the linked list in display format
    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

    # Pushes new data to the head of the list
    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp


# Driver code
linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)

print("Given linked list")
print(linkedList)

linkedList.head = linkedList.reverse(linkedList.head)

print("Reversed linked list")
print(linkedList)

#Display the total memory space occupied by the linked list

# sample lists
list1 = [1, 2, 3, 4]
list2 = ["Data Structure", "Algorithms"]

# print the sizes of the sample lists
print("Size of list1: " + str(list1.__sizeof__()) + "bytes")
print("Size of list2: " + str(list2.__sizeof__()) + "bytes")


