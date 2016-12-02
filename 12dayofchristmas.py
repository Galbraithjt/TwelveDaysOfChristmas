#TwelveDaysOfChristmas

#Truple For Storing Gifts
gifts=('Partridge in a Pear Tree','Turtle Doves','French Hens',
        'Calling Birds','Golden Rings','Geese-a-Laying','Swans-a-Swimming',
        'Maids-a-Milking','Ladies Dancing','Lords-a-Leaping','Pipers Piping',
        'Drummers Drumming')

#For loop to print
for i in range(len(gifts)):
    #If statement to print day grammatically correct i.e. 1st 2nd 3rd 
    if i==0:
        print("On the {}st day of Chrismas my true love gave to me".format(i+1))
    elif i==1:
        print("On the {}nd day of Chrismas my true love gave to me".format(i+1))
    elif i==2:
        print("On the {}rd day of Chrismas my true love gave to me".format(i+1))
    else:
        print("On the {}th day of Chrismas my true love gave to me".format(i+1))
    #For loop to display gifts.
    for j in range(i,-1,-1):
        print (j+1, gifts[j])
    # Line break between verses.
    print ("\n")
