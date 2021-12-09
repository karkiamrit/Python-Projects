n=eval(input("Enter your number between 1 to 99999: "))
units = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
tens = {2:"Twenty",3:"Thirty",4:"Fourty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
if n<=9:
    print(units[n])

elif n>=10 and n<=19:
    print(units[n])

elif n>=20 and n<=99:
    print(tens[n//10] +" " + units[n%10])

elif n>=100 and n<=999:
    if n%100<=19:
        print(units[n//100]+' '+"hundred" +" "+units[n-((n//100)*100)])
    else:
        print(units[n//100]+' '+"hundred" +" "+tens[(n-((n//100)*100))//10]+" "+units[(n%100)%10])

elif n>=1000 and n<=99999:
    if n//1000<=19:
        if ((n-(n//1000)*1000)%100)<=19:
            if(n%1000==0):
                print(units[n//1000]+' '+"Thousand"+" "+units[(n-(n//1000)*1000)//100]+" "+units[(n-(n//1000)*1000)%100])
            else:
                print(units[n//1000]+' '+"Thousand"+" "+units[(n-(n//1000)*1000)//100]+" Hundred "+units[(n-(n//1000)*1000)%100])
        else:
            print(units[(n//1000)]+" "+"Thousand"+" "+units[((n-(n//1000)*1000)//100)]+" Hundred "+tens[((n-((n//1000)*1000))%100)//10]+' '+units[((n-(n//1000)*1000)%100)%10])
    else:
        if  ((n-(n//1000)*1000)%100)<=19:
            if(n%1000==0):
                print(tens[(n//1000)//10]+" "+units[(n//1000)%10]+' '+'Thousand')
            else:
                print(tens[(n//1000)//10]+" "+units[(n//1000)%10]+' '+'Thousand'+units[(n-(n//1000)*1000)//100]+" Hundred "+units[(n-(n//1000)*1000)%100])
        else:
            print(tens[(n//1000)//10]+" "+units[(n//1000)%10]+' '+'Thousand'+" "+units[((n-(n//1000)*1000)//100)]+" Hundred "+tens[((n-((n//1000)*1000))%100)//10]+' '+units[((n-(n//1000)*1000)%100)%10])
