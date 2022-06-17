#class stocks with three methods
class stock:
  '''attributes of stocks'''
  def __init__ (self,ifrise,ifdrop,ifflat):
    self.ifrise = ifrise
    self.ifdrop = ifdrop
    self.ifflat = ifflat
  
  def stock_movement_ifrise(self):
    print(f"When the value of a stock is up {self.ifrise}")
  

  def stock_movement_ifdrop(self):
    print(f"When the value of a stock is down {self.ifdrop}")
    

  def stock_movement_ifflat(self):
    print(f"When the value of a stock is flat {self.ifflat}")
    