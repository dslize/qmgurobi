\ Model diet
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.82 peanutbutter + 0.07 milk + 0.31 apple + 0.29 bread
Subject To
 R0: 627 peanutbutter + 42 milk + 50 apple + 188 bread >= 2000
 R1: 49.9 peanutbutter + 0.3 milk + 0.4 apple + bread <= 20
 R2: 0.3333333333333333 peanutbutter + 0.3333333333333333 milk
   - 0.6666666666666667 apple + 0.3333333333333333 bread <= 0
Bounds
End
