class Casa:

	def __init__(self, preco):
		self._preco = preco

	@property
	def preco(self):
		return self._preco
	
	@preco.setter
	def preco(self, novo_preco):
		if novo_preco > 0 and isinstance(novo_preco, float):
			self._preco = novo_preco
            
            

	@preco.deleter
	def preco(self):
		del self._preco


casa = Casa(123.000)
casa.preco = 10.000
del casa.preco
print(casa.preco)