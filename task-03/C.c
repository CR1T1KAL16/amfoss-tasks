#include <stdio.h>

int checkPrime(int n) {
    if (n<=1) 
        return 0; 
    for (int i = 2; i * i <= n; i++) {
        if (n%i==0) 
            return 0; 
    }
    return 1;
}

void primeNumbers(int n) {
    for (int i = 2; i <= n; i++) {
        if (checkPrime(i)) 
            printf("%d ", i);
    }
}

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    primeNumbers(n);
    return 0;
}
