from collections import defaultdict
from framework_mesa.time import RandomActivation
from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.agentes import Machos, Hembras

class RandomActivationByBreed(RandomActivation):
	model = None
	
	def __init__(self, model):
		super().__init__(model)
		self.agents_by_breed = defaultdict(dict)
		self.model = model
	
	def add(self, agent):
	
		self._agents[agent.unique_id] = agent
		agent_class = type(agent)
		self.agents_by_breed[agent_class][agent.unique_id] = agent
	
	def remove(self, agent):
	
		del self._agents[agent.unique_id]
		
		agent_class = type(agent)
		del self.agents_by_breed[agent_class][agent.unique_id]
	
	def cantidadDeAnimales0(self):
		n = len(self.agents_by_breed[Machos]) + len(self.agents_by_breed[Hembras])
		return n
	
	def cantidadDeAnimales1(self, claseDeAnimal):
		todos = len(self.agents_by_breed[Machos]) + len(self.agents_by_breed[Hembras])
		n = len(self.agents_by_breed[claseDeAnimal])
		return n
	
	def porcentajeDeAnimales2(self, claseDeAnimal, estrategia):
		todos = len(self.agents_by_breed[Machos])+len(self.agents_by_breed[Hembras])
		n = 0
		for i in self.agents_by_breed[claseDeAnimal]:
			agente3 = self.agents_by_breed[claseDeAnimal][i]
			if agente3.estrategia == estrategia:
				n = n + 1
		if not n == 0:
			n = round(n/todos, 2)
		else:
			n = 0
		
		return n
	
	def cantidadDeAnimales2(self, claseDeAnimal, estrategia):
		todos = len(self.agents_by_breed[Machos])+len(self.agents_by_breed[Hembras])
		n = 0
		for i in self.agents_by_breed[claseDeAnimal]:
			agente3 = self.agents_by_breed[claseDeAnimal][i]
			if agente3.estrategia == estrategia:
				n = n + 1
	
		return n
