class queue():
    def __init__(s):
        # s.cap = cap
        # s.top = 0
        s.a = []
    
    def enq(s , x):
        s.a.append(x)
        # s.top+= 1
        print ("Element is enqueued ")
    
    def is_empty(s):
        return len(s.a) == 0

    def deq(s):
        if s.is_empty():
            print ("Queue is empty !")
            return False
        # s.top -= 1 
        return s.a.pop(0)

    def display(s):
        if s.is_empty():
            print ("Queue is empty !")
        
        print ("Current queue is : " , s.a)

    def peek(s):
        if s.is_empty():
            print ("Queue is empty !")
        return s.a[0]


q = queue()
q.display()
q.enq(10)
q.enq(20)
q.enq(30)
print(q.peek())
q.display()
print (q.deq())
q.display()
print (q.peek())     
print (q.deq())
print (q.deq())
q.display()    
q.deq()

