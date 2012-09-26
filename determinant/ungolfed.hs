import Data.List (transpose)

det :: Num a => [[a]] -> a
det [[a]]   = a
det m       = sum [(-1)^i*m!!i!!0*det(minor m (i+1) 1) | i <- [0..length m - 1]]

minor :: Num a => [[a]] -> Int -> Int -> [[a]]
minor m i j = transpose . remRow (j-1) . transpose $ remRow (i-1) m

remRow :: Num a => Int -> [[a]] -> [[a]]
remRow row m = ys ++ (tail zs)
    where (ys,zs) = splitAt row m

main = do
    putStrLn "aoeu"
