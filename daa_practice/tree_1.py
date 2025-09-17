class test :
    def __init__(s , value):
        s.value = value 
        s.children = []
    def add_child(s , child_node):
        s.children.append(child_node)

    def display(s , lvl = 0):
        print (" " * lvl * 2  + s.value)
        for i in s.children :
            i.display(lvl + 1 )
        
    
root = test("root")
c1 = test("CHild 1 ")
c2 = test ("Chld 2 ")
root.add_child(c1)
root.add_child(c2)
c1.add_child(test("Child 1.1"))
c2.add_child(test("child 2.1"))
c2.add_child(test("child 2.2"))
root.display()
