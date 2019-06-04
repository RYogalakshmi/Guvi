r=int(input())
if( r%100!=0 and r%4==0 or r%400==0):
    print("yes")
else:
    print("no")
