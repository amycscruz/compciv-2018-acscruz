def fob(n):
    for i in range(1,n+1):
        if i%15==0:
            print (str(i)+' FoozBuzz')
        if i%3==0:
            print (str(i)+' Fooz')
        if i%5==0:
            print (str(i)+' Buzz')
        else:
            print (i)
