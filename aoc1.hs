solve :: Integer -> Integer -> Integer -> Integer
solve num cmp acc = if num <= 0
                        then acc
                        else if rem == cmp
                            then solve quo cmp $ acc + rem
                            else solve quo rem acc
                    where rem = num `mod` 10
                          quo = num `div` 10
