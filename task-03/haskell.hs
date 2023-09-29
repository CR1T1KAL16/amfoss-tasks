factors::Int->[Int]
factors n = [x | x<-[1..n], (mod n x)==0]

isprime :: Int->Bool
isprime n = (factors n) == [1,n]

uptoN :: Int->[Int]
uptoN n = [x | x<-[1..n], isprime x]

main = do
   let n=10
   print (uptoN n)