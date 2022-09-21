## Array

1. Definition:

   - Contiguous area of memory

   - Equal-size elemets

   - Index by contiguous integers

2. Constant-time access
   - The target address of i: array_address + element_size * (i - first_index)
3. Common Operation
   - End: Add O(1), Remove O(1)
   - Middle: Add O(n), Remove O(n)
   - Begin: Add O(n), Remove O(n)

## Singly-Linked List

1. A singly-linked list contains a key and a next pointer.
2. List API
   - add to front: O(1)
   - return front: O(1)
   - remove front: O(1)
   - add to back: O(n) (if no tail pointer) O(1) (if tail pointer)
   - return back:  O(n) (if no tail pointer) O(1) (if tail pointer)
   - remove back: O(n)
   - Find key: O(n)
   - remove key: O(n)
   - Add before: O(n)
   - Add after: O(1)
   - is empty: O(1)

## Doubly-Linked Lists

1. A Doubly-Linked List contains a key, a next pointer, a prev pointer.
2. List API
   - add to front: O(1)
   - return front: O(1)
   - remove front: O(1)
   - add to back: O(n) (if no tail pointer) O(1) (if tail pointer)
   - return back:  O(n) (if no tail pointer) O(1) (if tail pointer)
   - remove back: O(1)
   - Find key: O(n)
   - remove key: O(n)
   - Add before: O(1)
   - Add after: O(1)
   - is empty: O(1)

## Stacks

1. Basic operations: like a tile of books
   - push: O(1)
   - Top: the most recently add key O(1)
   - Pop: removes and returns the most recently add key O(1)
   - Check empty O(1)
2. Use an array to implement stack
3. Use linked list to implement stack: push front
4. LIFO

## Queues

1. Operations
   - Enqueue: add keys to collection O(1)
   - Dequeue: removes and returns least recently-added key O(1)
   - Empty O(1)
   - FIFO
2. Implement by linked list with tail pointer
3. Implement by array with read index and write index

## Trees

1. A tree contains a key and a list of child trees
2. Root: top node in the tree, root node is level 1
3. Child and parent
4. Ancestor or descendant

5. Leaf: leaf height is 1

6. Traversal

   - In-order: left root right

   - Pre-order: root left right

   - Post-order: left right root

   - BFS: 

     Queue q

     q.enqueue(tree)

     while not q.empty():

     ​	node <- q.dequeue()

     ​	print(node)

     ​	if node.left:

     ​		q.enqueue(node.left)

     ​	if node.right:

     ​		q.enqueue(node.right)
