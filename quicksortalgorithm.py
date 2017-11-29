def quickSort(ar):
   quickSortHelper(ar,0,len(ar)-1)

def quickSortHelper(ar,first,last):
   if first<last:

       splitpoint = partition(ar,first,last)

       quickSortHelper(ar,first,splitpoint-1)
       quickSortHelper(ar,splitpoint+1,last)


def partition(ar,first,last):
   pivotvalue = ar[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and ar[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while ar[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = ar[leftmark]
           ar[leftmark] = ar[rightmark]
           ar[rightmark] = temp

   temp = ar[first]
   ar[first] = ar[rightmark]
   ar[rightmark] = temp


   return rightmark

m = input()
ar = [int(i) for i in raw_input().strip().split()]

quickSort(ar)

print(ar)
