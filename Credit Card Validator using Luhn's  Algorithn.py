card_no ='5610591081018250'
odd_sum = 0
even_sum = 0
#convert to list to make iterations
number = list(card_no)   
double_list = []

#enumerate to obtain index list
for (idx,val) in enumerate(number):  
    if idx%2 !=0 :  #this is odd indexed number
        odd_sum += int(val) #1.Find the sum of odd index values of the credit card number.

    else:  #this is even indexed number 2.Find the doubles of number of even indexed  number
        double_list.append(int(val)*2)  #enclose the val with bracket or else * will be the priority and will get double value



#converting the list into a string
double_string = ""
for x in double_list:
    double_string += str(x)  #3. Calculate the sum of doubles of number of even indexed number

#converting the string back to list
double_list = list(double_string)

for x in double_list:
    even_sum += int(x)   #4.Calculate the sum of even indexed numbers
  
net_sum = odd_sum + even_sum   #5.Find the sum of odd and even numbers .If add up to multiples of 10 then the card is valid.
if net_sum %10 == 0:
    print("Valid card!")
else:
    print("Invalid card")



