import System
main=do
 args<-getArgs
 let a=1:2:drop 2(concat.zipWith replicate a.cycle$[1,2])
 putStrLn$concatMap(\b->' ':show b)$take(read(args!!0)::Int)a
