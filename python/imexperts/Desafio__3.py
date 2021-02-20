import math 
import traitlets
lucroMaxAcoes = (diasValores)
	
	lucroMax = 0
	menorPreco  = diasValores[0]
	for i = 1 i < diasValores.length i++:
		menorPreco = math.min(diasValores[i], menorPreco)
		lucroMax = math.max(lucroMax, diasValores[i] - menorPreco)

	return lucroMax

print(lucroMaxAcoes([7,1,5,3,6,4]))
print(lucroMaxAcoes([7,6,4,3,1]))
