class bi_tree:
    def __init__(s , value):
        s.value = value
        s.left = None
        s.right = None
    def left_node (s , num):
        if s.left is None:
            s.left = bi_tree(num)
        else :
            new = bi_tree(num)
            new.left = s.left 
            s.left = new
    def right_node (s , num):
        if s.right is None:
            s.right = bi_tree(num)
        else :
            new = bi_tree(num)
            new.right = s.right
            s.right = new
    def display (s , lvl = 0):
        print (" " * lvl * 3 + str(s.value))
        if s.left :
            s.left.display(lvl +1 )
        if s.right :
            s.right.display(lvl + 1 )

def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print (node.value , end = " ")
    print_inorder(node.right)

def print_preorder(node):
    if node is None:
        return
    print(node.value , end = " ")
    print_preorder(node.left)
    print_preorder(node.right)

def print_postorder(node):
    if node is None :
        return
    print_postorder(node.left)
    print_postorder(node.right)
    print(node.value , end = " ")

root = bi_tree(1)
root.left_node(2)  
root.right_node(3)
root.left.left_node(4)
root.left.right_node(5)
root.right.right_node(6)
root.display()
print("The indorder for this root is : " , end=" ")
print_inorder(root)
print("\nThe preorder for this root is : " , end=" ")
print_preorder(root)
print("\nThe postorder for this root is : " , end=" ")
print_postorder(root)