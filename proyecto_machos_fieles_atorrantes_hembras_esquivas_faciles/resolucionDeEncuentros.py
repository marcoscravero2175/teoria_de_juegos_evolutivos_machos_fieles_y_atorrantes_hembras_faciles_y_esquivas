from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.agentes import Machos, Hembras
def ResolucionDeEncuentrosEntreMachosYHembras(agente1, agente2, tiempoDeCortejoTotal, tiempoDeCrianzaTotal):

	print(agente1.EstaCortejandoAalguien())
	print(agente2.EstaCriandoAUnHijo())
	print(agente1.EsMaduroSexual())
	
	
	if (type(agente1) is Machos) and (not agente1.EstaCortejandoAalguien()) and \
		(type(agente2) is Hembras) and (not agente2.EstaCortejandoAalguien()) and \
		(not agente1.EstaCriandoAUnHijo()) and (not agente2.EstaCriandoAUnHijo()) and \
		agente1.EsMaduroSexual() and (agente2.EsMaduroSexual()) and \
		(agente1.estrategia == "fiel") and (agente2.estrategia == "esquiva"):
	
		xs = 21
		agente1.TieneQueCortejar(tiempoDeCortejoTotal)
		agente2.TieneQueCortejar(tiempoDeCortejoTotal)
		agente1.TieneQueCriarAUnHijo(round(tiempoDeCrianzaTotal/2, 1))
		agente2.TieneQueCriarAUnHijo(round(tiempoDeCrianzaTotal/2, 1))
		print("Se cambio")
		print("-vecinos: "+ str(agente2.unique_id)+" agente1.cortejando:"+ str(agente1.cortejando) + " agente2.cortejando:" + str(agente2.cortejando))

		agente1.SetCombatioContraAlguienEnEstaEpoca(True)
		agente2.SetCombatioContraAlguienEnEstaEpoca(True)

		
	elif (type(agente1) is Machos) and (not agente1.EstaCortejandoAalguien()) and \
		(type(agente2) is Hembras) and (not agente2.EstaCortejandoAalguien()) and \
		(not agente1.EstaCriandoAUnHijo()) and (not agente2.EstaCriandoAUnHijo()) and \
		agente1.EsMaduroSexual() and (agente2.EsMaduroSexual()) and \
		(agente1.estrategia == "fiel") and (agente2.estrategia == "facil"):
		xs = 21
		agente1.TieneQueCortejar(1)
		agente2.TieneQueCortejar(1)
		agente1.TieneQueCriarAUnHijo(round(tiempoDeCrianzaTotal/2, 1))
		agente2.TieneQueCriarAUnHijo(round(tiempoDeCrianzaTotal/2, 1))
		print("Se cambio")
		print("-vecinos: "+ str(agente2.unique_id)+" agente1.cortejando:"+ str(agente1.cortejando) + " agente2.cortejando:" + str(agente2.cortejando))

		agente1.SetCombatioContraAlguienEnEstaEpoca(True)
		agente2.SetCombatioContraAlguienEnEstaEpoca(True)
		
	elif (type(agente1) is Machos) and (not agente1.EstaCortejandoAalguien()) and \
		(type(agente2) is Hembras) and (not agente2.EstaCortejandoAalguien()) and \
		(not agente1.EstaCriandoAUnHijo()) and (not agente2.EstaCriandoAUnHijo()) and \
		(agente1.EsMaduroSexual()) and (agente2.EsMaduroSexual()) and \
		(agente1.estrategia == "galanteador") and (agente2.estrategia == "facil"):
		xs = 21
		agente1.TieneQueCortejar(1)
		agente2.TieneQueCortejar(1)
		agente1.TieneQueCriarAUnHijo(0)
		agente2.TieneQueCriarAUnHijo(tiempoDeCrianzaTotal) 
		
		agente1.SetCombatioContraAlguienEnEstaEpoca(True)
		agente2.SetCombatioContraAlguienEnEstaEpoca(True)

		print("Se cambio")
		print("-vecinos: "+ str(agente2.unique_id)+" agente1.cortejando:"+ str(agente1.cortejando) + " agente2.cortejando:" + str(agente2.cortejando))

	return (agente1, agente2)		
