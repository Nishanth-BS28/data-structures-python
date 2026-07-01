# Data Structures in Python

Core data structures implemented from scratch in Python — no built-in shortcuts.

## Implementations

### Stack (stack.py)
- LIFO — Last In First Out
- push() — add to top O(1)
- pop() — remove from top O(1)

### Queue (queue.py)
- FIFO — First In First Out
- enqueue() — add to back O(1)
- dequeue() — remove from front O(1)

### Linked List (linked_list.py)
- append() — add to end O(n)
- prepend() — add to start O(1)
- display() — print all nodes O(n)
- delete() — remove a node O(n)

### Binary Search Tree (bst.py)
- insert() — add a value O(log n)
- search() — find a value O(log n)
- inorder() — print sorted order O(n)
- find_min() — find minimum value O(log n)

### Hash Table (hash_table.py)
- insert() — add key-value pair O(1)
- get() — retrieve value by key O(1)
- Collision handling via chaining

## Time Complexity Summary
| Structure | Access | Search | Insert |
|-----------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) |
| BST | O(log n) | O(log n) | O(log n) |
| Hash Table | O(1) | O(1) | O(1) |

## Built With
- Python 3
