#recursive function to solve Tower of Hanoi
def towers(n,a,c,b):
    #if only 1 disk, then move it from A to C
    if n==1:
        print('Move disk %i from pole %s to %s'%(n,a,c))
    else: #if more than 1 disk
        #move first n-1 disk from A to B using C as intermediate pole
        towers(n-1,a,b,c)
        #move remaining 1 disk from A to C
        print('Move disk %i from pole %s to %s'%(n,a,c))
        #move n-1 disk from B to C using A as intermediate pole
        towers(n-1,b,c,a)
n=int(input('Enter number of disks: '))
#call the function
towers(n,'A','C','B')
