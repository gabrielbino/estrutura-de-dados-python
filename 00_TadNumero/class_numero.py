class Numero:

  def __init__(self):
    self.__valor = 0

  @property
  def valor(self):
    return self.__valor
  
  @valor.setter
  def valor(self, valor):
    if isinstance(valor, float) or isinstance(valor, int):
      if valor < 0:
        valor = 0
        self.msg("valor menor que zero -> corrigido para zero")
      elif valor > 40 and valor < 60:
        if valor < 50:
          valor = 40
          self.msg("valor no intervalo não suportado -> corrigido para 40")
        else:
          valor = 60
          self.msg("valor no intervalo não suportado -> corrigido para 60")
      elif valor > 100:
        self.msg("valor no intervalo não suportado -> corrigido para 100")
      self.__valor = valor
      print("Novo valor atribuído.")
    else:
      self.msg("tipo de dado incompatível; valor inalterado")

  def msg(self, texto):
    print("\n\n !!! ATENÇÃO: " + texto + " !!!\n\n" )