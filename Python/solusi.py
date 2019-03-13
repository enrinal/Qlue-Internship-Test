#Fungsi untuk cek prima atau tidak
def isPrima(n): 
    if n <= 1 : 
        return False
    # Check bilangan
    for i in range(2, n): 
        if n % i == 0: 
            return False
    return True

# Fungsi untuk print bilangan prima
def printPrime(n): 
    f = []
    for i in range(2,n):
        if isPrime(i):
            #Memasukan nilai kedalam list
            f.append(i)
    return f

# Driver code 
if __name__ == "__main__" : 
    n = 10
    # Pemanggilan Fungsi
    print(printPrime(n)) 

