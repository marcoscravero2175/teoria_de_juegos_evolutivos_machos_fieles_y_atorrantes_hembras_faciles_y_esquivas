from framework_mesa.visualization.ModularVisualization import ModularServer
from framework_mesa.visualization.modules import CanvasGrid, ChartModule
from framework_mesa.visualization.UserParam import UserSettableParameter

from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.agentes import Machos, Hembras
from proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles.model import Ambiente

import random


from framework_mesa.visualization.ModularVisualization import VisualizationElement
import numpy as np


from framework_mesa.visualization.ModularVisualization import ModularServer
from framework_mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from framework_mesa.visualization.UserParam import UserSettableParameter

from framework_mesa.visualization.TextVisualization import (
	TextData, TextGrid, TextVisualization
)





class HistogramModule(VisualizationElement):
	#package_includes = ["<script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.4/Chart.min.js'></script>"]
	#package_includes  = ["dist/Chart.bundle.min.js"]
	#local_includes = ["clases/HistogramModule1.js"]
	local_includes = ["framework_mesa/visualization/templates/js/HistogramModule1.js"]
	
	def __init__(self, bins, canvas_height, canvas_width):
		self.canvas_height = canvas_height
		self.canvas_width = canvas_width
		self.bins = bins
		new_element = "new HistogramModule({}, {}, {})"
		new_element = new_element.format(bins,
		                                 canvas_width,
		                                 canvas_height)
		self.js_code = "elements.push(" + new_element + ");"
	
	def render(self, model):
		#wealth_vals = [agent.wealth for agent in model.schedule.agents]
		#hist = np.histogram(wealth_vals, bins=self.bins)[0]
		#return [int(x) for x in hist]    
		porcentajeDeMachosFiles = model.schedule.porcentajeDeAnimales2(Machos, "fiel")
		
		porcentajeDeMachosGalanteadores = model.schedule.porcentajeDeAnimales2(Machos, "galanteador")
		
		porcentajeDeHembrasFaciles = model.schedule.porcentajeDeAnimales2(Hembras, "facil")
		
		porcentajeDeHembrasEsquivas = model.schedule.porcentajeDeAnimales2(Hembras, "esquiva")
		
		return [porcentajeDeMachosFiles, porcentajeDeMachosGalanteadores, porcentajeDeHembrasFaciles, porcentajeDeHembrasEsquivas]
		



def personalizacionDelAmbiente(agent):
	if agent is None:
		return
	
	portrayal = {}
	
	if type(agent) is Machos:
	
		if agent.estrategia == "fiel":
			portrayal["Shape"] = "proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles/resources/machoFiel3.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Animal"] = "macho"
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Tiempo que falta de cortejo"] = round(agent.cortejando, 1)
			portrayal["Tiempo que faltante en crianza de hijos"] = round(agent.criandoHijo, 1)
			portrayal["Layer"] = 1
			portrayal["text_color"] = "Blue"
		
		if agent.estrategia == "galanteador":
			portrayal["Shape"] = "proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles/resources/machoGalanteador3.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Animal"] = "macho"
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Tiempo que falta de cortejo"] = round(agent.cortejando, 1)
			portrayal["Tiempo que faltante en crianza de hijos"] = round(agent.criandoHijo, 1)
			portrayal["Layer"] = 1
			portrayal["text_color"] = "White"
	    
	if type(agent) is Hembras:
	
		if agent.estrategia == "esquiva":
			portrayal["Shape"] = "proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles/resources/hembraEsquiva3.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Animal"] = "hembra"
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Tiempo que falta de cortejo"] = round(agent.cortejando, 1)
			portrayal["Tiempo que faltante en crianza de hijos"] = round(agent.criandoHijo, 1)
			portrayal["Layer"] = 1
			portrayal["text_color"] = "Green"
		
		if agent.estrategia == "facil":
			portrayal["Shape"] = "proyecto_machos_fieles_atorrantes_hembras_esquivas_faciles/resources/hembraFacil3.png"
			# https://icons8.com/web-app/36821/German-Shepherd
			portrayal["Animal"] = "hembra"
			portrayal["Estrategia"] = agent.estrategia
			portrayal["Edad"] = round(agent.edad, 1)
			portrayal["Tiempo que falta de cortejo"] = round(agent.cortejando, 1)
			portrayal["Tiempo que faltante en crianza de hijos"] = round(agent.criandoHijo, 1)
			portrayal["Layer"] = 1
			portrayal["text_color"] = "White"
	    
	return portrayal

canvas_element = CanvasGrid(personalizacionDelAmbiente, 20, 20, 500, 500)
#canvas_element = CanvasGrid(wolf_sheep_portrayal, 20, 20, 500, 500)
chart_element = ChartModule([{"Label": "Total", "Color": "#E6E6E6"},
				{"Label": "Machos", "Color": "#A9D0F5"},
				{"Label": "Hembras", "Color": "#F5A9BC"},
				{"Label": "Machos fieles", "Color": "#5882FA"},
				{"Label": "Machos galanteadores", "Color": "#0000FF"},
				{"Label": "Hembras esquivas", "Color": "#FA58AC"},
				{"Label": "Hembras faciles", "Color": "#FF0040"}])

model_params = {
		"distanciaMaximaVecinos": UserSettableParameter('slider', 'Distancia dentro de la cual se consideran que son vecinos', 30, 1, 20),
		"cantidadDeMachosFieles": UserSettableParameter('slider', 'Cantidad inicial de machos con estrategia fiel', 1, 0, 10),
		"cantidadDeMachosGalanteadores": UserSettableParameter('slider', 'Cantidad inicial de machos con estragetia galanteador', 0, 0, 10),
		"cantidadDeHembrasFaciles": UserSettableParameter('slider', 'Cantidad inicial de hembras con estrategia facil', 0, 0, 10),
		"cantidadDeHembrasEsquivas": UserSettableParameter('slider', 'Cantidad inicial de hembras con estrategia esquiva', 1, 0, 10),
		"tiempoDeCortejoTotal": UserSettableParameter('slider', 'Tiempo de cortejo de un macho fiel', 3, 0, 20),
		"tiempoDeCrianzaTotal": UserSettableParameter('slider', 'Tiempo total que se tiene que asignar a la criaza de un niño', 8, 0, 20),
		"edadDeMaduracionSexual": UserSettableParameter('slider', 'Edad de maduracion sexual', 0, 0, 50),
		"edadDeDefuncion": UserSettableParameter('slider', 'Edad en que mueren', 12, 0, 50)
		}

histogram = HistogramModule(list(range(10)), 200, 500)
#histogram = HistogramModule(list(range(10)), 200, 500)

server = ModularServer(Ambiente, [canvas_element, chart_element, histogram], "Machos galanteadores y fieles. Hembras faciles y esquivas", model_params)

#server.port = 8257
server.port = int(os.environ.get("PORT", 5000))

server.launch()
