class Control():
  def __init__(self,tv):
    self.tv=tv
  def turnOn(self):
    Tv.turnOn()
  def turnOff(self):
    Tv.turnOff()
  def canalUp(self):
    Tv.canalUp()
  def canalDown(self):
    Tv.canalDown()
  def VolumenUp(self):
    Tv.VolumenUp()
  def volumenDown(self):
    Tv.volumenDown()
  def set_canal(self,canal):
    self.canal=canal
  def enlazar(self, televisor):
      self.tv = televisor
      televisor.control = self
  def set_tv(self,tv):
    self.tv=tv
  def get_tv(self,tv):
    return self.tv
    