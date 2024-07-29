# Print fibonacci series upto given digit
#1,2,3,4,5,6
#0,1,1,2,3,5,8

n = int(input("Enter the number to which you want series : "))
def fibonacci_number(num):
     if num == 1:
         return 0
     elif num == 2:
         return 1
     else:
         return(fibonacci_number(num-1)+fibonacci_number(num-2))

def fibonacci_series(n):
     series = []
     for i in range(1, (n+1)):
        # print(fibonacci_number(i))
         series.append(fibonacci_number(i))
     print(series)

fibonacci_series(n)
