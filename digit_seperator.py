num=input('enter the number: ')

seperated_digit_num=''
count=0

for i in num:
    if i.isnumeric():
        continue

    else:
        print('only numbers!')
        break
else:




 if len(num)<4:
    print(num)
 else:
    num=list(num)
    num.reverse()


    for i in num:
        count+=1
        seperated_digit_num+=i
        if count%3==0 and count!=len(num): 
            seperated_digit_num+=','

    seperated_digit_num=list(seperated_digit_num)
    seperated_digit_num.reverse()
    for i in seperated_digit_num:
        print(i,end='')           


            