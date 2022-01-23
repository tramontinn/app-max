class Cozinha:
    def __init__(self, horaAbertura, horaFechamento, nomeCozinha, pPrincipal):
        self.horaAbertura = horaAbertura
        self.horaFechamento = horaFechamento
        self.nomeCozinha = nomeCozinha
        self.pprincipal = pPrincipal
    
    def exibeInfoCozinha(self):
        print(self.horaAbertura, self.horaFechamento, self.nomeCozinha, self.pprincipal)


class Ingrediente:
    def __init__(self, ingrediente, dataValidade):
      self.ingrediente = ingrediente
      self.dataValidade = dataValidade


ingredientes1 = Ingrediente('Arroz','12 dias')
print(ingredientes1.ingrediente, ingredientes1.dataValidade)

cozinha1 = Cozinha('14:00','20:00','Cozinha Mineira','Feijoada')
cozinha1.exibeInfoCozinha()

cozinha2 = Cozinha('10:00','23:00','Cozinha Chinesa','Yakissoba')
cozinha2.exibeInfoCozinha()