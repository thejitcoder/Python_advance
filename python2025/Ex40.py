"""
write an example where there is a shop in your village and that shop is a grocery shop and you are purchasing 
aloo-5kg
and 1kg=20 rs
rice-10kg
and 1kg= 35 rs
now find the total, you have take 500 rs so what is the balance left. use class object method 
"""
class ex40:
 def show(self):
  price=20
  qty=5
  total=price*qty
  print  ("Aloo is", total)
  price=35
  qty=10
  total1=price*qty
  print  ("Rice is", total)
  total2=total+total1
  print("Total amount",total2)
  balance=500-total2
  print("Balance is", balance)
  
ob=ex40()
ob.show()