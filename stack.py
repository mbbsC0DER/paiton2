class stack():
    def __init__(s , cap):
        s.cap = cap 
        s.top = -1
        s.a = []
    
    def push(s,x):
        if s.top == s.cap - 1 :
            print ("Stack overflow !")
            return False
        s.top += 1 
        s.a.append(x)
        print ("Element pushed .")
    
    def is_empty(s):
        return len(s.a) == 0
        
    def pop(s):
        if s.is_empty():
            print ("Stack is empty nothing to pop .")
            return False
        else:
            popped = s.a.pop(s.top)
            s.top -= 1
            print ("Element popped .")
            return popped
        
    def peek(s):
        if s.is_empty() :
            print ("Stack is empty .")
            return False
        return s.a[s.top]
    
    def display(s):
        if s.is_empty() < 0 :
            print ("stack is empty ")
            return False
        print ("Current stack : " , s.a)

t = stack(5)
t.push(10)
t.push(20)
t.display()
t.pop()
print (t.peek())
t.display()
t.pop()
t.display()
t.pop()
t.display()
    

     