fn is_prime(num: u64) -> bool {
    if num <= 1 {
        return false;
    }
    if num == 2 {
        return true;
    }
    if num % 2 == 0 {
        return false;
    }
    
    let mut i = 3;
    while i * i <= num {
        if num % i == 0 {
            return false;
        }
        i += 1; 
    }
    true
}

fn print_primes_up_to_n(n: u64) {
    for i in 2..=n {
        if is_prime(i) {
            println!("{}", i);
        }
    }
}

fn main() {
    let n = 10; 
    print_primes_up_to_n(n);
    }