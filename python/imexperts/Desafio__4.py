
get_Retencao = mapaElevacao
retencao = 0
esq = 0
dir = mapaElevacao.len [-1]
maxEsq = 0
maxDir = 0

while esq < dir:
    	if mapaElevacao[esq] < mapaElevacao[dir]
			mapaElevacao[esq] >= maxEsq or (maxEsq = mapaElevacao[esq]) or retencao += (maxEsq - mapaElevacao[esq])
			return ++esq
        else:
			mapaElevacao[dir] >= maxDir ? (maxDir = mapaElevacao[dir]) or retencao += (maxDir - mapaElevacao[dir])
			return --dir
		
	
return retencao


print(get_Retencao([0,1,0,2,1,0,1,3,2,1,2,1]))