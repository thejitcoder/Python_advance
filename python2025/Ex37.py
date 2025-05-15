class ex34:
 def show(self):
  aq = 5
  ap = 20
  atta = aq*ap
  rq = 10
  rp = 35
  rice = rq*rp
  total = atta+rice
  print("total is", total)
  balance= 500-total
  print("balance is ", balance)
ob = ex34()
ob.show()