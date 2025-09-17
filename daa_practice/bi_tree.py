class binary_tree:
    def __init__(s , value):
        s.value = value
        s.left = 0
        s.right = 0
    def insert_left(s , num):
        s.left = binary_tree(num)
    def insert_right(s , num):
        s.right = binary_tree(num)
    def display(s , lvl = 0) :
        if s.right :
            s.right.display(lvl + 1 )
            print (" " * lvl + str(s.value))
        if s.left :
            s.left.display(lvl + 1)

root = binary_tree(1)
root.insert_left(2)
root.insert_right(3)
root.left.insert_left(4)
root.left.insert_right(5)
root.right.insert_left(6)
root.right.insert_right(7)
root.display()