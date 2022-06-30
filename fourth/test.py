

#1.2857142857142858
#1.28571429
def float_to_ratio(number):
    accuracy=len(str(number))-2
    whole_part=int(str(number)[0])
    number=float(number)
    number=number-whole_part
    number=round(number,accuracy)
    numerator=0
    denominator=1
    while round(numerator/float(denominator),accuracy)!=number:
        #print(numerator)
        if numerator+1<=denominator:
            numerator+=1
        else:
            numerator=1
            denominator+=1
    numerator+=whole_part*denominator
    return (numerator,denominator)
    
float_to_ratio(0.33)