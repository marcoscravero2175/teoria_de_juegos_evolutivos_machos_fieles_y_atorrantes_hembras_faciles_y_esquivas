from framework_mesa import Agent

from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.animales import Animales

import random

class Machos(Animales):

	def __init__(self, unique_id, estrategia, edadDeMaduracionSexual, edadDeDefuncion, model):
		super().__init__(unique_id, model)
		
		self.estrategia = estrategia
		self.edadDeMaduracionSexual = edadDeMaduracionSexual
		self.edadDeDefuncion = edadDeDefuncion  
		self.combatioContraAlguienEnEstaEpoca = False
	
	def step(self):
	
		self.edad = self.edad + 1
		
		if self.edad > self.edadDeDefuncion:
		
			self.model.grid._remove_agent(self.pos, self)
			self.model.schedule.remove(self)
	
	    
	def EsMaduroSexual(self):
		b = (self.edad > self.edadDeMaduracionSexual)
		return b
	
	def EstaCortejandoAalguien(self):
		b = (self.cortejando > 0)
		return b
	
	def EstaCriandoAUnHijo(self):
		b = (self.criandoHijo > 0)
		return b
	
	def TieneQueCriarAUnHijo(self, criandoHijo):
		self.criandoHijo = criandoHijo
	
	def TieneQueCortejar(self, cortejando):
		self.cortejando = cortejando
	
	def AsignarTiempoAlCortejo(self):
		self.cortejando = self.cortejando - 1
	
	def AsignarTiempoAlHijo(self):
		self.criandoHijo = self.criandoHijo - 1
	
	def SetCombatioContraAlguienEnEstaEpoca(self, combatioContraAlguienEnEstaEpoca):
	
		self.combatioContraAlguienEnEstaEpoca = combatioContraAlguienEnEstaEpoca
	
	def GetCombatioContraAlguienEnEstaEpoca(self):
	
		return self.combatioContraAlguienEnEstaEpoca
    
class Hembras(Animales):

	def __init__(self, unique_id, estrategia, edadDeMaduracionSexual, edadDeDefuncion, model):
		super().__init__(unique_id, model)
		
		self.estrategia = estrategia
		self.edadDeMaduracionSexual = edadDeMaduracionSexual
		self.edadDeDefuncion = edadDeDefuncion  
		self.combatioContraAlguienEnEstaEpoca = False
	
	def step(self):
	
		self.edad = self.edad + 1
		
		if self.edad > self.edadDeDefuncion:
			self.model.grid._remove_agent(self.pos, self)
			self.model.schedule.remove(self)
	
	    
	def EsMaduroSexual(self):
		b = (self.edad > self.edadDeMaduracionSexual)
		return b
	
	def EstaCortejandoAalguien(self):
		b = (self.cortejando > 0)
		return b
	
	def EstaCriandoAUnHijo(self):
		b = (self.criandoHijo > 0)
		return b
	
	def TieneQueCriarAUnHijo(self, criandoHijo):
		self.criandoHijo = criandoHijo
	
	def TieneQueCortejar(self, cortejando):
		self.cortejando = cortejando
	
	def AsignarTiempoAlCortejo(self):
		self.cortejando = self.cortejando - 1
	
	def AsignarTiempoAlHijo(self):
		self.criandoHijo = self.criandoHijo - 1
	     
	def SetCombatioContraAlguienEnEstaEpoca(self, combatioContraAlguienEnEstaEpoca):
	
		self.combatioContraAlguienEnEstaEpoca = combatioContraAlguienEnEstaEpoca
	
	def GetCombatioContraAlguienEnEstaEpoca(self):
	
		return self.combatioContraAlguienEnEstaEpoca
