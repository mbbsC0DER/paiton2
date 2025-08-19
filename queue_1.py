class queue():
    def __init__(s):
        # s.cap = cap 
        s.a = []
    
    def enq(s , x):
        s.a.append(x)
        print ("Element is enqueued ")
    
    def is_empty(s):
        return len(s.a) == 0

    def deq(s):
        if s.is_empty():
            print ("Queue is empty !")
            return False
        return s.a.pop(0)

    def display(s):
        if s.is_empty():
            print ("Queue is empty !")
        
        print ("Current queue is : " , s.a)

q = queue()
q.display()
q.enq(10)
q.enq(20)
q.enq(30)
q.display()
print (q.deq())
q.display()     
print (q.deq())
print (q.deq())
q.display()    
q.deq()

