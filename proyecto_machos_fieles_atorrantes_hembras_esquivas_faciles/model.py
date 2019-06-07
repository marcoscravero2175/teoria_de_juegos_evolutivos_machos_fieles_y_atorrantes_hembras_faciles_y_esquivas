from framework_mesa import Model
from framework_mesa.space import MultiGrid
from framework_mesa.datacollection import DataCollector

from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.agentes import Machos, Hembras
from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.schedule import RandomActivationByBreed

from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.resolucionDeEncuentros import ResolucionDeEncuentrosEntreMachosYHembras


import random

class Ambiente(Model):
	
	height = 20
	width = 20
	
	cantidadDeMachosFieles = 1
	cantidadDeMachosGalanteadores = 1
	cantidadDeHembrasEsquivas = 1
	cantidadDeHembrasFaciles = 1
	tiempoDeCortejoTotal = 2
	tiempoDeCrianzaTotal = 5
	edadDeMaduracionSexual = 16
	edadDeDefuncion = 90
	
	description = 'Un modelo descripto por Richard DawkinsA model for simulating wolf and sheep (predator-prey) ecosystem modelling.'
	
	def __init__(self, 
		alto = 20,
		ancho = 20,
		distanciaMaximaVecinos = 1, 
		cantidadDeMachosFieles = 1,
		cantidadDeMachosGalanteadores = 1,
		cantidadDeHembrasEsquivas = 1,
		cantidadDeHembrasFaciles = 1,
		tiempoDeCortejoTotal = 2,
		tiempoDeCrianzaTotal = 5,
		edadDeMaduracionSexual = 16,
		edadDeDefuncion = 90
		):
		super().__init__()
		self.alto = alto
		self.ancho = ancho

		self.k = 0
		
		self.distanciaMaximaVecinos = distanciaMaximaVecinos
		self.cantidadDeMachosFieles = cantidadDeMachosFieles
		self.cantidadDeMachosGalanteadores = cantidadDeMachosGalanteadores
		self.cantidadDeHembrasEsquivas = cantidadDeHembrasEsquivas
		self.cantidadDeHembrasFaciles = cantidadDeHembrasFaciles
		self.tiempoDeCortejoTotal = tiempoDeCortejoTotal
		self.tiempoDeCrianzaTotal = tiempoDeCrianzaTotal
		self.edadDeMaduracionSexual = edadDeMaduracionSexual
		self.edadDeDefuncion = edadDeDefuncion        

		self.eliminoIndividiosAlternativosMachos = True
		self.eliminoIndividiosAlternativosHembras = True

		self.schedule = RandomActivationByBreed(self)
		self.grid = MultiGrid(20, 20, torus=True)
		
		self.grid = MultiGrid(self.alto, self.ancho, torus=False)
		self.datacollector = DataCollector(
			{"Total": lambda m: m.schedule.cantidadDeAnimales0(),
			"Machos": lambda m: m.schedule.cantidadDeAnimales1(Machos),
			"Hembras": lambda m: m.schedule.cantidadDeAnimales1(Hembras),
			"Machos fieles": lambda m: m.schedule.cantidadDeAnimales2(Machos, "fiel"),
			"Machos galanteadores": lambda m: m.schedule.cantidadDeAnimales2(Machos, "galanteador"),
			"Hembras faciles": lambda m: m.schedule.cantidadDeAnimales2(Hembras, "facil"),
			"Hembras esquivas": lambda m: m.schedule.cantidadDeAnimales2(Hembras, "esquiva")})
		
		i = 0
		while i < self.cantidadDeMachosFieles:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "fiel"
			macho1 = Machos(id, estrategia, self.edadDeMaduracionSexual, self.edadDeDefuncion, self)
			self.grid.place_agent(macho1, (x, y))
			self.schedule.add(macho1)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeMachosGalanteadores:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "galanteador"
			macho2 = Machos(id, estrategia, self.edadDeMaduracionSexual, self.edadDeDefuncion, self)
			self.grid.place_agent(macho2, (x, y))
			self.schedule.add(macho2)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeHembrasEsquivas:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "esquiva"
			hembra1 = Hembras(id, estrategia, self.edadDeMaduracionSexual, self.edadDeDefuncion, self)
			self.grid.place_agent(hembra1, (x, y))
			self.schedule.add(hembra1)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeHembrasFaciles:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "facil"
			hembra2 = Hembras(id, estrategia, self.edadDeMaduracionSexual, self.edadDeDefuncion, self)
			self.grid.place_agent(hembra2, (x, y))
			self.schedule.add(hembra2)
			
			i = i + 1
			
		self.datacollector.collect(self)     
		self.running = True
	
	
	def step(self):


		puntajeMinimo = None
		puntajeMaximo = None
		for agente in self.schedule.agents:
			agente.SetCombatioContraAlguienEnEstaEpoca(False)
		#poblacion = self.schedule.cantidadDeJugadores0()
		eliminoIndividiosAlternativos = True


		print("*** paso: " + str(self.k))

		self.schedule.step()
		self.datacollector.collect(self)
		next_move = None
		
		for agenteA in self.schedule.agents:
			p0= agenteA.pos[0]
			p1= agenteA.pos[1]
			#for agenteB in self.grid.get_neighbors((p0, p1), True, include_center=True):

			if (agenteA.GetCombatioContraAlguienEnEstaEpoca() == False):	
				
				if agenteA.EstaCriandoAUnHijo() and (not agenteA.EstaCortejandoAalguien()):
					agenteA.AsignarTiempoAlHijo()
					
					print("- El agente nro:" + str(agenteA.unique_id) + " esta criando un hijo:" + str(agenteA.criandoHijo))
					
				if agenteA.EstaCortejandoAalguien():
					agenteA.AsignarTiempoAlCortejo()
	
					print("- El agente nro:" + str(agenteA.unique_id) + " esta cortejando " + str(agenteA.cortejando))
					#print("- Hembras step:" + str(agenteA.cortejando))
					if not agenteA.EstaCortejandoAalguien():
						
						puntoActual = agenteA.pos
						neig  = self.grid.get_neighborhood(puntoActual, True, True)
						next_move = random.choice(neig)
						x = next_move[0]
						y = next_move[1]
						estrategia = agenteA.estrategia
						poblacion = self.schedule.cantidadDeAnimales0()



						if type(agenteA) is Machos:

							numeroDeCopiasMachos = 1
							if (poblacion >= 10):
								if(self.eliminoIndividiosAlternativosMachos == True):
									numeroDeCopiasMachos = 0
									self.eliminoIndividiosAlternativosMachos = False
								else:
									numeroDeCopiasMachos = 1
									self.eliminoIndividiosAlternativosMachos = True

							i = 0
							while i < numeroDeCopiasMachos:

								macho = Machos(self.next_id(), estrategia, self.edadDeMaduracionSexual, self.edadDeDefuncion, self)
								self.grid.place_agent(macho, next_move)
								self.schedule.add(macho)
								print("- El agente nro:" + str(agenteA.unique_id) +" creo un macho y lo puso en "+ str(macho.unique_id) + "("+ str(x) + "," + str(y) + ")")
								i = i + 1
						
						if type(agenteA) is Hembras:

							numeroDeCopiasHembras = 1
							if (poblacion >= 10):
								if(self.eliminoIndividiosAlternativosHembras == True):
									numeroDeCopiasHembras = 0
									self.eliminoIndividiosAlternativosHembras = False
								else:
									numeroDeCopiasHembras = 1
									self.eliminoIndividiosAlternativosHembras = True

							i = 0
							while i < numeroDeCopiasHembras:
							
								hembra = Hembras(self.next_id(), estrategia, self.edadDeMaduracionSexual, self.edadDeDefuncion, self)
								self.grid.place_agent(hembra, next_move)
								self.schedule.add(hembra)
								print("- El agente nro:" + str(agenteA.unique_id) +" creo una hembra y lo puso en "+ str(hembra.unique_id) + "("+ str(x) + "," + str(y) + ")")
								i = i + 1

						print("-2c")
	
	
				i = 0
				for agenteB in self.grid.get_neighbors((p0, p1), True, include_center=True, radius=self.distanciaMaximaVecinos):
				
					#get_neighbors((p0, p1), radius, include_center=True)
					#get_neighbors((p0, p1), moore, include_center=True, radius=20)
					
	
					if (not (agenteA.unique_id == agenteB.unique_id)) and (agenteB.GetCombatioContraAlguienEnEstaEpoca() == False):
	
						(agenteA, agenteB) = ResolucionDeEncuentrosEntreMachosYHembras(agenteA, agenteB, self.tiempoDeCortejoTotal, self.tiempoDeCrianzaTotal)
	
					i = i + 1
	
				
				if (not agenteA.EstaCortejandoAalguien()) and (not agenteA.EstaCriandoAUnHijo()):
				
					#puntoActual = agenteA.pos
					p0= agenteA.pos[0]
					p1= agenteA.pos[1]                
					
					neig  = self.grid.get_neighborhood((p0, p1), True, True)
					next_move = random.choice(neig)
					
					self.grid.move_agent(agenteA, next_move)
					x = next_move[0]
					y = next_move[1]
					print("-Movido " + str(agenteA.unique_id) + " ("+ str(x) + "," + str(y) + ")")



		self.k = self.k + 1




	
	def run_model(self, step_count=200):
		a = 10
