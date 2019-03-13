# Python3 print all sets of numbers that sum up to n. 
def printSetOfNumber(arr, index, bil, i): 
    #Jika Negative
    if (i < 0): 
        return; 
    #Jika Set Number ketemu print bilangan
    if (i == 0): 
        for i in range(index): 
            print(arr[i], end = " "); 
        print(""); 
        return; 
# Cek bilangan sebelumnya yang ditaruh di arr[]
    prev = 1 if(index == 0) else arr[index - 1]; 
    for k in range(prev, bil + 1): 
        arr[index] = k; 
        printSetOfNumber(arr, index + 1, bil, i - k);

def setOfNumber(n): 
# arr untuk menyimpan sets bialngan, size array max sebanyan N elemen
    arr = [0] * n; 
    printSetOfNumber(arr, 0, n, n); 
# Driver code 
n = 5; 
setOfNumber(n); 
