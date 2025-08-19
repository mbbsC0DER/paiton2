class stack():
    def __init__(s ):
        # s.cap = cap 
        # s.top = -1
        s.a = []
    
    def push(s,x):
        # if s.top == s.cap - 1 :
        #     print ("Stack overflow !")
        #     return False
        # s.top += 1 
        s.a.append(x)
        print ("Element pushed .")
    
    def is_empty(s):
        return len(s.a) == 0
        
    def pop(s):
        if s.is_empty():
            print ("Stack is empty nothing to pop .")
            return False
        else:
            popped = s.a.pop()
            # s.top -= 1
            print ("Element popped .")
            return popped
        
    def peek(s):
        if s.is_empty() :
            print ("Stack is empty .")
            return False
        # return s.a[]
    
    def display(s):
        if s.is_empty() < 0 :
            print ("stack is empty ")
            return False
        print ("Current stack : " , s.a)

t = stack()
t.push(10)
t.push(20)
t.display()
print (t.pop())
# print (t.peek())
t.display()
t.pop()
t.display()
t.pop()
t.display()
    

     