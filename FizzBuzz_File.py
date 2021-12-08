def FizzBuzz(start, finish):
    mylist = []
    mylist = list(range(start, finish+1))
    idx = 0
    for x in range(start, finish+1):
        if x % 3 == 0:
            mylist[idx] = "fizz"
        if x % 5 == 0:
            mylist[idx] = "buzz"
        if x % 15 == 0:
            mylist[idx] = "fizzbuzz"
        idx+=1
    return(mylist)