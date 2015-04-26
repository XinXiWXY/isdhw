def bsearch(data,target):
       if data!=[]:
             top =0
             bot=len(data)-1
       while(top <=bot):
               mid = ( top + bot )/2
               if (data[mid]==target):
                     return mid
               elif (data[mid]<target):
                        top=mid+1
                        bsearch (data,target )
               elif (data[mid]>target):
                        bot=mid-1
                        bsearch (data,target)
       if ( bot<top ):
           return None
       elif ( top <=bot):
           return target[index]
       
