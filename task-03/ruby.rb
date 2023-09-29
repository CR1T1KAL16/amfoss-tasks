def is_prime?(n)
  (2..Math.sqrt(n)).each do |i|
    return false if n % i == 0
  end
  return true
end

def find_primes(n)
  
  primes = []
  (2..n).each do |i|
    primes << i if is_prime?(i)
  end
  primes
end

n=gets.chomp.to_i
p find_primes(n) 