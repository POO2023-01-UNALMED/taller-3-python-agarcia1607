class Tv():
  canal=1
  volumen=1
  precio=500
  numTV=0
  def __init__(self,marca,estado):
    from televisores.control import Control
    from televisores.marca import Marca
    self.Marca=marca
    self.estado=estado
    Marca.numTv+=1
  def get_marca(self):
    return self.marca
  def get_contol(self):
    return self.control
  def get_precio(self):
    return self.precio
  def get_volumen(self):
    return self.volumen
  def get_canal(self):
    return self.canal
  def set_marca(self,marca):
    self.marca=marca
  def set_control(self,control):
    self.control=control
  def set_precio(self,precio):
    self.precio=precio
  def set_volumen(self,volumen):
    self.volumen=volumen
  def set_canal(self,canal):
    self.canal=canal
  def turnOn(self):
    if self.estado==False:
      self.estado=True
  def turnOff(self):
    if self.estado==True:
      self.estado=False
  def get_estado(self):
    return self.estado
  def canalUp(self,estado):
    if estado==True and self.canal in range(1,119):
      self.canal+=1
  def canalDown(self,estado):
    if estado==True and self.canal in range(1,119):
      self.canal-=1
  def volumenUp(self,estado):
    if estado==True and self.volumen in range(0,6):
      self.volumen+=1
  def volumenDown(self,estado):
    if estado==True and self.volumen in range(0,6):
      self.volumen-=1