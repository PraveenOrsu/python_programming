interval_1=int(input("Enter the first interval : "))
interval_2=int(input("Enter the second interval  :"))
i=interval_1
while(i<=interval_2):
    is_prime=True
    for j in range(2,i):
        if(i%j==0):
            is_prime=False
    if(is_prime):
        print(i)

    i=i+1
