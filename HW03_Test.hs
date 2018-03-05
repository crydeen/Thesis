module HW03_Test
where

import Control.Exception()

import HW03

main :: IO()
main = do
  putStrLn "\n3a sumSqNeg1 test 1:"
  putStrLn ("sumSqNeg1 [-1,3,4,-1,-1,3]\n"
    ++ show sumSqNeg1 [-1,3,4,-1,-1,3])
