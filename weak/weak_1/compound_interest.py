principal = int(input())
interest = int(input())
time = int(input())
rate=interest/100
def compInt(principal,interest,time):
    return principal*(1+rate)**time

print(f"copound interest is:{compInt(principal,interest,time)}")