num=int(input("enter a number"))
# square pattren
for i in range(num):
    for j in range(num):
        print("# ",end='')
    print("")
# square second method    
for t in range(num):
    print("*"*num)    
           
 # pyramid patren
for i in range(num):
    for j in range(i+1):
        print("#",end=" ")
    print()
# pyramid second method
for y in range(num):
    print("*"*(y+1))
    
    
# reverse pyramid 
for i in range(num):
    for j in range(num-i):
        print("#",end=" ")
    print()   
# reverse pyramid secong method
for z in range(num):
    print("*"*(num-z))

#  triangle 
 
for r in range(num):
    print("*"*(2*r+1))       

# is prime number

def is_primenum(num):
    for pr in range(2,num):
        if num%pr==0:
            print("not prime")
            break
    else:
        print("prime")   
    
is_primenum(num)   
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

ro=[i+2 for i in points]
print(points)
print(ro)
A=[4,6,5,8,9,3,2,4,5,4,3,2,3,4]
totalpop=sum(pop)
print(totalpop)
A = [2, 1, 2,5,3] 
def solve(A):
     first=0
     second=0
     if len(A)<2:
         return -1
     else:
         for n in A:
             if n>first:
                 first=n
                 second=first
                 return second
          
t=solve(A)
print(t)

word = "rohini is a good girl"
word_list = list(word)
print(word_list)
n=word_list.index('n')
d=word_list.index('D')
print(d,n)
print(word_list[7:19])