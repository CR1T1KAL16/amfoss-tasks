package main

import (
    "fmt"
    "math"
)

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    sqrtN := int(math.Sqrt(float64(n)))
    for i := 2; i <= sqrtN; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func primeNumbers(n int) {
    for i := 2; i <= n; i++ {
        if isPrime(i) {
            fmt.Printf("%d ", i)
        }
    }
    fmt.Println()
}

func main() {
    var n int
    fmt.Print("Enter a positive integer: ")
    fmt.Scan(&n)
    primeNumbers(n)
}