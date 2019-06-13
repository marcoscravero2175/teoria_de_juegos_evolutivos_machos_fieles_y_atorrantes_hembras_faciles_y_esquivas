# Teoria de los Juegos Evolutivos. Machos fieles y atorrantes, hembras faciles y esquivas.


Los animales necesitan recursos, como agua y alimento, para vivir. En un ambiente favorable un individuo puede tener más hijos que en un ambiente desfavorable. Por ejemplo, supongamos, que en un ambiente favorable un individuo tiene en promedio 5 hijos y en un ambiente desfavorable tiene 2 hijos, podríamos asignarle al recurso un valor de 3 puntos. La diferencia entre la cantidad de hijos que tiene el individuo en un ambiente favorable menos la diferencia de hijos que el individuo tiene en un ambiente desfavorable es el valor del recurso ambiente favorable. Los individuos van sumando puntos con cada recurso que consiguen, cada recurso aporta una pequeña fracción del total de puntos. Cuando llega a una determinada edad, el individuo se reproduce asexualmente creando copias de sí mismo de acuerdo a la cantidad de puntos obtenidos y luego muere.

Las plantas no se dejan comer, producen sabores desagradables, los animales tampoco se dejan comer, las gacelas evolucionan para correr más rápido, haciéndoles hacen cada vez la vida más difícil a los leones. En este modelo no vamos a considerar  la carrera armamentística asimetría entre presas y depredadores, ni tampoco la evolución de la vista de los pájaros para ver a insectos que se camuflaba y mimetizaban cada vez mejor con el ambiente. Vamos a suponer que en cada posición del tablero,  el ambiente donde se desarrolla la simulación, hay recursos que los animales necesitan para vivir.

Un recurso se puede compartir. Si bien hay situaciones en las cuales a los individuos no les conviene compartir un recurso, por ejemplo si un ambiente favorable tiene para el animal 10 puntos, y un ambiente menos favorable tiene 8 puntos, a nadie le convendría compartir y tener  5 putos cuando puede irse a un ambiente desfavorable y tener 8 puntos. En este modelo supondremos que los recursos son divisibles y que a los animales les conviene compartir. 

Un conflicto se produce cuando dos individuos quieren el mismo recurso. Los conflictos se pueden resolver en forma pacífica, esto es, compartiendo el recurso, o puede escalar el conflicto, se produce una pelea que termina con uno de los dos contrincantes gravemente lesionado.   Las lesiones producidas en un combate entre dos animales son costosas, también es un costo, aunque menor, el tiempo perdido amenazando al contrincante, gruñendo o mostrándole los dientes.

En una guerra de desgaste solo el ganador obtiene el recurso pero ambos contrincantes pagan el mismo coste. Por ejemplo, si el coste está dado por el tiempo que duro la pelea, ambos perdieron el mismo tiempo. Si el coste está dado por lesiones recibidas, supongamos que un contrincante está dispuesto a pelear hasta que tenga el ojo en compota y el rival hasta las costillas rota. Empieza la pela, un contrincante tira un puño y le rompe el tabique nasal, como los contrincantes son físicamente iguales, el otro tira en puño y le rompe el tabique nasal al otro. Así hasta que llegan a los ojo en compota, momento en que uno de los contrincantes se retira y el otro gana. En este caso gana el animal que estaba dispuesto a pelear hasta tener una costilla rota y ambos animales pagan el costo de romperse el tabique nasal. 

En el juego de halcones y palomas el ganador obtiene recurso, pero a diferencia de la guerra de desgaste solo el perdedor paga el coste, el ganador no resulta lesionado. Si bien las peleas entre animales se parecen más a una guerra de desgaste asimétrica  que a un juego de halcones y palomas, para seguir el modelo de Maynad Smith  implemente el juego de halcones y palomas, solo el perdedor paga el costo y el ganador obtiene el recurso sin resultar lesionado.

Sabemos que el altruismo puede evolucionar si un individuo puede reconocer a individuos altruistas y ayudar solo a los que reconoció como altruista, si un individuo altruista se tira a un rio para salvar 10 individuos el altruistas podría morir, pero el gen para altruismo podría evolucionar si salvo a 10 individuos. De igual manera la cooperación puede evolucionar si hay reconocimiento individual de los miembros de la población. En un dilema del prisionero repetido, la estrategia que empieza cooperando y después coopera si el contrincante coopero con migo en el pasado y desertar en caso contrario. Estos los casos, altruismo y cooperación, los modelos suponen reconocimiento individual y memoria, coopero si Juan copero con migo en el pasado, lo ayudo a Juan que se está ahogando si pertenece al conjunto de los que ayudan a personas que se ahogan. En el modelo que  implemente no hay reconocimiento, ni memoria, el individuo son anónimos, no saben, antes de comenzar la pelea si el oponente es violento o pacifico, y tampoco queda recuerdo en la memoria de combate con el individuo.

Algunos modelos se abstraen de la vecindad, la distancia mínima en cual dos individuos se consideran vecinos. Considerar que todos los agentes que hay en el ambiente son vecinos entre sí puede dar resultados muy diferentes a lo que sucede en la realidad. Por ejemplo, anteriormente vimos que la estrategia del dilema del prisionero repetido, cooperar si el individuo coopero con migo en el pasado” necesita que los agentes se puedan reconocer individualmente. El éxito de la estrategia depende de lo que está haciendo la mayoría de la población, si la mayoría de la población está cooperando, desertar no es buena idea. Recíprocamente, si la mayoría de la población está desertando, cuando aparezca alguien de coopere todos se van a aprovechar del ingenuo que empieza cooperando.  Pero una diferencia importante entre las dos estrategias es que cooperar si el otro coopero en el pasado tiene muy buen desempeño cuando se enfrenta con copias de sí mismo. Si los descendientes de cooperar heredan la estrategia y  nacen uno cerca uno del otro, cuando se encuentran tienen muy buen desempeño y les va mucho mejor que a los descendientes de siempre desertar que se encuentran copias de siempre desertar. Esta propiedad de la estrategia hace que crezca mucho más rápido que siempre desertar y en pocos pasos cooperar si anteriormente coopero se hace mayoría en la población y cuando alcance la mayoría en la población se convierte en la mejor estrategia que puede adoptar un individuo en la población. En la simulación se puede configurar la vecindad. Una vecindad de todo el ambiente da igual resultado que modelos matemáticos en los que se abstraen de la vecindad.

Modelos más complejos agregan el castigo. Algunos animales juegan en el dilema del prisionero repetido la estrategia compartir con quien haya compartido, pero se castigan, se vengan de quienes los han traicionado. El castigo es costoso y no da beneficio directo al agente que fue traicionado. Encima que lo traicionan, el agente pierde tiempo y energía en castigar a quien lo traiciono, esto es un beneficio evolutivo para la población y hace más fácil que aparezca la cooperación. Por ejemplo, las víctimas de un delito piden justicia y hacen marchas para que a los responsables.

La cantidad de hijos que un padre tiene depende de los recursos y las lesiones sufridas. Los individuos viven una determinada edad se reproducen y luego mueren, por ejemplo pueden vivir 6 pasos de simulación  dejar 2 hijos. Los hijos son iguales que sus padres, son clones de sus padres ya que en el modelo la reproducción es asexual, heredan la misma forma de resolución de conflictos.  Si los padres resolvían los conflictos compartiendo, los hijos van a compartir, si los padres resolvían las disputas peleando los hijos van a resolver las disputas peleando. El final del juego habrá más individuos que compartan y más individuos violentos.

La explosión demográfica es un problema en la simulación, pero en la naturaleza, generalmente, las poblaciones no crecen hasta quedarse sin recurso. Si en la simulación fijamos que los individuos más aptos tengan más de 2 hijos el crecimiento es exponencial y en pocas generaciones se produce una sobrepoblación. En cambio si hago que los individuos más aptos tengan un solo hijo, y los menos aptos no tengan ningún hijo,  en cada generación se va reduciendo la población. Los biólogos propusieron varias explicaciones de porque son muy raras las explosiones demográficas en la naturaleza. Una explicación, por el bien de la especie,  es selección de grupo, los individuos se reúnen, hacen un censo y se decide, inconscientemente, cuantos descendientes se tendrá en la próxima generación. 

Hay otra explicación con más evidencia empírica. Tener un hijo tiene un coste y solo se obtiene una ganancia si el hijo  llega sano y salvo a la edad adulta y le dé nietos. En la población hay individuos que están genéticamente programados para tener 20 hijos, hay individuos que están programados para temes 10 y los hay que tiene solo 5 hijos independientemente de su aptitud. Si un individuos pone 20 huevos y no puede alimentarlos, mueren todos sus hijos y entonces deja menos descendía que alguien que solo puso 5 huevos, pudo alimentar a los 5 y todos llegaron sanos y salvo a la edad adulta. Esto da como resultado una regulación dinámica de la cantidad de hijos óptimos.  Por cuestiones de simplicidad para la simulación se implementó una política centralizada, como la explicación del censo, se cuanta la cantidad total de individuos de la población y en base a esto se decide cuantos hijos se tendrán en la próxima generación.

La primera simulación que haremos será de un modelo donde todos los individuos son exactamente iguales, luego aparece un gen mutado, agregamos individuos con una solo diferencia la estrategia para resolver conflicto, compartir o pelear. Después agregaremos una diferencia arbitraria, por ejemplo el color de cabello o si tiene barba o no tiene barba, que no influyen en la fuerza física, ni en la capacidad de lucha e introduciremos estrategias condicionales, como pelear si mi oponente tiene el cabello más oscuro que el mío y compartir en caso contrario. Por ultimo veremos qué pasa cuando los individuos se diferencian en atributo que influye en la fuerza o en  la capacidad de lucha, que pasa con individuos que luchan si mi contrincante es más fuerte y huyen si es alguien más débil.

## Compartir o pelear en población donde todos los individuos son iguales

En el primer modelo que implementamos suponemos que todos los individuos son exactamente iguales, no se diferencian en nada, hasta que surge un conflicto. Unos resuelven los conflictos compartiendo y otros peleando.    No sabe qué estrategia va a usar el oponente hasta que empiece el combate. No puede haber estrategia del tipo altruista, si mi oponente es de los que comparten yo voy a compartir, porque no hay forma de saber qué hará el oponente. Tampoco puede haber estrategia de tipo colaborativa, si mi oponente compartió en el pasado voy a compartir, no hay discriminación individual, no sé si  tuve un conflicto anterior con el mismo oponente, ni se cómo se comportó en disputas anteriores. 

Todos los individuos ante un conflicto comparten o pelean. Las estrategias son hereditarias. Los individuos que comparten tuvieron un padre que compartía y los individuos que pelean tuvieron un padre que peleaba. Una de las estrategias es compartir. Se comparte si el otro también quiere compartir,  si el otro no quiere compartir, quiere pelear por el recurso, el que quiere compartir le cede el recurso al violento. La otra estrategia pelear, pelea hasta conseguir el recurso y hasta quedar gravemente lesionado.  Si elijo pelear y el otro elije pelear se da una pelea y dado que somos iguales físicamente se tiene el 50% de probabilidades de ganar y 50% de probabilidades de terminar gravemente lesionado.  

Supongamos una población donde todos los individuos son clones, exactamente igual, todos tienen la misma fuerza física y la forma de resolver conflictos es compartiendo. Si en esta población cuando surge un conflicto por un recurso, como todos los individuos comparten entonces todos obtienen la mitad del valor de los recursos.  Ahora supongamos que se produce una  mutación, los individuos mutantes siguen siendo físicamente iguales, pero se diferencian de los demás en una sola cosa, cuando surge un conflicto por un recurso los individuos no comparten sino que pelean. En la simulación se agrega un individuo que resuelva los conflictos peleando. ¿Qué sucede en la población? 

Si el valor del recurso es menor que el coste de las lesiones producida por la pela al cabo de un par de generaciones todos los individuos pelearan. Si todos los individuos de la población pelean, como son individuos  físicamente iguales la probabilidad de ganar es del 50% y la probabilidad de perder es del 50%, por lo tanto en promedio obtienen 50% V-C.

Si en esta población todos pelean, como son todos iguales, la mitad de las peleas las gana uno y la otra mitad de las peleas la gana el otro, por lo tanto todos se quedan con la mitad del valor del recurso, igual al caso donde todos comparten. 

Veremos si al final de los juegos hay más individuos que resuelven sus conflictos a los golpes o deciden compartir.  Qué pasa si en una población donde todos comparten se agrega un violento? Puede invadir la población? Que pasa con una población donde todos son violentos y se agrega uno que comparte? 

Todo depende del valor del recurso y del coste de la lesión. Si el valor del recurso es superior al costo de lesión una población violenta no puede ser invadido por alguien que comparta y si en la población inicial todos están compartiendo y se agrega un violento, el violento invade la población y toda la población se vuelve violenta al final de juego.
Por ejemplo, si todos los individuos eligieron pelear y el costo de lesión es superior al valor del recurso a mí me conviene elegir compartir, porque si bien mi ganancia neta va a ser 0, voy a ceder con todos, no voy a ganar nunca, si elijaría pelear la mitad de las veces ganaría y la otra mitad de las veces perdería, la mitad de las veces obtendría el recurso y la otra mitad de las veces quedaría lesionado, y dado que la lesión es mayor que el beneficio del recuso, obtendría en promedio un resultado menor que cero.

En resumen, si valor del recurso es mayor que el costo de perder una pelea y tengo una población pacifica con solo agregar un individuo violento, que en vez de compartir prefiera pelear, al final del juego todos los individuos van a ser violentos. Si el valor del recurso es menor que el costo de lesiones al final del juego voy a tener en la población un porcentaje de sujetos que prefieren compartir y un porcentaje de violentos, mientras mayor sea el costo por perder una pelea mayor va a ser el porcentaje de la población que va a preferir ser pacífica y compartir recursos en conflicto. Una conclusión interesante es que por más grande que sea el coste de lesión siempre habrá un pequeño porcentaje que le rendirá ser violento. 



## Estrategias condicionales usando diferencias arbitrarias entre los individuos

En la vida real no somos clones, no somos todos iguales, hay diferencias arbitrarias, como el color de pelo, que no influyen en el resultado de una pelea y hay diferencias entre los individuos, como fuerza física o tamaño que si influye en resultado de un combate. Primero vamos a considerar diferencias en atributos no influyen en el resultado de un combate, como tener barba verde,  cabello oscuro, piel clara. Luego vamos a considerar diferencias que si influyen en el resultado de una pelea, como ser más grande y más fuerte.

Supongamos que hay individuos que tienen cabello claro y hay individuos con cabello oscuro, además suponemos que cada individuo sabe su color de cabello y puede ver el color de cabello de su oponente, pero no puede saber si su oponente va a estar dispuesto a compartir el recurso o va a pelear. 

En un punto anterior se explicó el altruismo, un individuo se arroja al rio y muere pero logra salvar a 10 individuos altruistas, con individuos que pueden reconocer a individuos altruistas y tienen una estrategia condicional del tipo “si el que se está ahogando es un individuo altruista tirarse al rio e intentar salvarlo. En este caso no podemos tener una estrategia del tipo “comparto solo con los individuos que comparten” porque no hay indicios de si es pacífico o violento, antes de que empiece la pelea no sé sabe cómo se comportara el oponente. 

En un punto anterior también se explicó que puede surgir la cooperación en un dilema del prisionero repetido, cuando hay reconocimiento individual, memoria de encuentros anteriores y una estrategia condicional del tipo “compartir si en oportunidades anteriores el individuo compartió y desertar en caso contrario”. En el juego que estamos considerando no hay reconocimiento individual, ni memoria de conflictos pasados. Esto se puede deber a que no tengan memoria, o a que sea muy raro que dos individuos se vuelvan a encontrar en el futuro, como pueden ser un conflicto entre dos desconocidos en una gran ciudad.

Los animales pueden usar diferencias arbitrarias para resolver conflictos. Además de las estrategias simples,   siempre compartir, siempre pelear, vamos a   agregar una tercera estrategia, una estrategia condicional,  “pelear solo si mi contrincante tiene el cabello más oscuro que mi color de cabello y compartir en caso contrario”. Que sucederá en este caso? qué estrategia me conviene a mí adoptar para ganar más puntos? Si vas a roma has le de los romanos, si todos están usando la estrategia condicional me conviene hacer lo que todos hacen?

Sabemos que si el recurso vale más que el costo de una lesión conviene pelear y que si el costo de una lesión es mayor de que valor del recurso lo que conviene hacer depende de lo que está haciendo la población,  va a haber un porcentaje de la población que comparta y otro que pelee, el porcentaje depende del valor del recurso y del costo de lesión, a mayor costo de lesión menor cantidad de individuos van pelear. Ahora veremos qué pasa cuando agregamos una estrategia condicional que depende de una diferencia arbitraria que hay entre los individuos.

Se puede ver en la simulación que si todos los individuos están usando la estrategia condicional “si mi oponente tiene el cabello más oscuro que el mío entonces pelear, en caso contrario compartir” y el valor del recurso es menor que el costo de una lesión, ninguna otra estrategia puede invadir esa población.



## Diferencias entre individuos en aspectos que influyen en el resultado de una pelea

Ahora consideremos una población donde los individuos son distintos, pero en aspectos que influyen en el resultado de una pelea, por ejemplo la fuerza y el tamaño. En la población hay individuos grandes y fuertes e individuos pequeños y débiles. Al igual que en los casos anteriores, los individuos no saben cómo reaccionara el oponente, si estará dispuesto a compartir o tendrá ganas de pelear. Solo se que el animal es más grande, o más chico, no sé si está dispuesto a atacarme o podemos compartir el recurso. 
Un ejemplo de asimetría puede ser el tamaño, hay individuos grandes e individuos chicos, otro ejemplo puede ser el sexo, hay individuos que son machos y otros que son hembras. Para simplificar asumamos que la asimetría puede tener solo dos valores, por ejemplo grande o chico, no hay individuos más o menos grandes, ni individuos que pesen 62 kg y otros que pesen 6 5kg, solo podemos clasificar a los individuos en grandes o chicos. En una pelea entre dos individuos grandes existe la misma probabilidad de que gane uno o de que gane el otro, igualmente una pelea entre individuos chicos tenemos el 50% de probabilidad de que gane uno o de que gane el otro. Pero cuando se enfrenta un individuo grande contra un individuo chico la probabilidad de que gane el más grande es un parámetro del modelo. Si queremos que el más grande siempre gane ponemos un porcentaje de 100. Si en peleas entre grandes y chicos el 80% de las veces gana el más grande ajustamos el parámetro del modelo a 80.

En una población asimétrica del tipo que estamos considerando pueden existir cuatro estrategias. Las dos estrategias que teníamos en la población simétrica, Siempre pelear, siempre  compartir, y dos estrategias condicionales, una de sentido común, pelear si mi oponente es de menor tamaño y compartir y caso contrario, y una estrategia condicional paradójica, pelear si mi oponente es más grande y compartir en caso contrario.

No hace falta ser muy inteligente para darte cuenta que sos un individuo grande y los costes de lesión son mayores que el valor del recurso la mejor estrategia es “pelear con los que son más chicos que vos y compartir el recurso en caso contrario”. En una población donde todos golpean a los más débiles no puede ser invadida por ninguna de las otras dos estrategias, siempre pelear, ni por siempre compartir.

Que pasa en una población donde todos los individuos pelean si su oponente es más grande y comparten en caso contrario? Puede ser invadido por las estrategias alternativas, siempre pelear, siempre compartir, o pelear solo si mi oponente es menor? Si el costo de lesión es superior al valor del recurso y todos siguen la estrategia paradójica, un individuo que siga la estrategia de sentido común, “pelear solo si el oponente es menor y compartir en caso contrario” no podrá invadir, está en peor situación que alguien que siga una estrategia paradójica, se pelearía con todos, y con un costo de lesión de más de 8 veces el valor del recurso, una probabilidad de ganar del 80% no compensa. 

Si los machos son más fuertes y grandes que las hembras, el 80% de las peleas entre machos y hembras las gana un macho, una estrategia condicional paradójica del tipo si sos hembra y tu contrincante es un macho atacar,  y si sos macho y tu contendiente es una hembra huir podría ser una estrategia evolutivamente estable. Cualquiera que hiciera algo distinto estaría en desventaja, las estrategias siempre huir, siempre pelear, están en desventaja contra la estrategia condicional paradójica que estaría usando la mayoría de la población. Aunque no es fácil decir cómo podría llegar una población a que todos sus miembros adopten una estrategia condicional paradójica, no hay etapas intermedias que sean evolutivamente estables.



## Juegos con estrategias evolutivas inestables

Como vimos anteriormente, con tema de la sobrepoblación, tener 5 hijos no siempre es evolutivamente mejor que tener 2 hijos. Tener un hijo tiene un costo y se obtiene recompensa cuando el descendiente llega sano y salvo a la edad adulta y  puede dar nietos. Una carrera armamentística produjo diferencias entre los sexos.  El ovulo es más grande y aporta nutrientes, los espermatozoides son mucho más chicos y tienen movilidad. Hay dimorfismo sexual, los machos son más grandes porque compiten por las hembras, las crías se desarrollan dentro del cuerpo de la madre.

En la reproducción sexual los costos de tener un hijo lo puede pagar uno solo de los progenitores o se pueden compartir entre los dos.  No están sobre este planeta las especies donde los machos se marcharon, dejando sola a las hembras, y como venganza las hembras también se marchaban dejando morir a la cría. Pero las hembras tienen una carta en su mano, pueden seleccionar machos con buenos genes o machos que realicen aportes, como construir un nido, antes de copular. 

Una hembra puede exigir que el macho le construya un nido antes de copular. La estrategia que se adopte un individuo depende de lo que está haciendo el resto de la población. Un hornero construye un nido porque todas las hembras exigen lo mismo para copular.
Como puede elegir una hembra machos con buenos genes. Como puede saber si no le están mintiendo, si solamente aparenta que es el macho más fuerte, pero en realidad los músculos son falsos? Los pavo real macho tienen colas llamativas que les dificulta caminar son atractivos para las hembras, porque son atractivas para las hembras o porque pueden mostrar que aun con una dificultad llegaron a la edad adulta. La explicación que hoy en día se acepta es que las señales son honestas porque son costosas, el principio de la desventaja. 

En la primer parte se consideraron dos tipos distintos de individuos, individuos grandes y chicos. Ambos individuos tenían las mismas estrategias disponibles. Los individuos grandes podían compartir o pelear, y los individuos chicos también podían compartir y pelear. Ahora consideremos dos tipos de individuos, pero cada individuo tiene distintas estrategias.  
Supongamos que los tipos de individuos son machos y hembras. Las estrategias de los machos son fieles o atorrantes y las hembras pueden ser fáciles y esquivas. Supongamos que la ventaja evolutiva por tener una  cría le da 15 puntos a cada uno de los padres, supongamos que el coste para tener una criar una cría con éxito es de 20 puntos, este coste se puede repartir entre los padres o lo pude pagar solo la hembra dependiendo del tipo de estrategia, supongamos que en un cortejo se pierden 3 puntos.

-En un encuentro de macho atorrante con una hembra fácil, le da al macho 15 puntos y a la hembra -5 puntos.
-Un encuentro entre un macho fiel y una hembra esquiva, el macho gana 2 puntos, esto es 15 de la cría -10 de la crianza compartida, -3 del cortejo. La hembra también obtiene el mismo puntaje.
-Un encuentro entre un macho atorrante y una hembra esquiva cada uno obtiene 0 puntos, no tienen ninguna cría, no hay cortejo, ni hay costo de crianza.
-Un encuentro entre un macho fiel y una hembra fácil, el macho consigue 5 puntos y la hembra también consigue 5 puntos.

Si se analiza el juego parecería que hay un equilibrio estable. En la primera edición del Gen Egoísta, Richard Dawkins pensaba que este juego tenía un equilibro  Analizando en profundidad el juego se puede ver que en realidad el equilibrio es inestable, el juego oscila, una vez que se alcanza el equilibrio, si se produce una pequeña modificación en los porcentajes, lejos de autorregularse y volver al equilibrio, el desequilibrio se potencia hasta alcanzar un equilibrio distinto.

Supongamos una población donde todas las hembras son fáciles y todos los machos fieles, si se introduce un macho atorrante este, a diferencia del macho fiel, no paga el coste de la crianza, por lo tanto va a obtener mejores puntajes que un macho fiel y el número de machos atorrantes aumenta.

A medida que los machos atorrantes aumentan, las hembras fáciles empiezan a tener menos ventaja que las hembras esquivas. Cuando la mayoría de los machos son atorrantes, las hembras esquivas obtienen mejor resultado que las hembras fáciles y por lo tanto su número aumenta.

Cuando se llega a unan situación donde todas las hembras son esquivas y los machos atorrantes, un macho fiel puede invadir la población, obtiene mejor desempeño que un macho atorrante.

Si todas las hembras son esquivas y los machos son files, una hembra fácil puede invadir la población y sacar ventaja de que todos los machos son fieles. En este punto estamos en la misma situación que cuando se empezó el ciclo, una población donde las hembras son fáciles y los machos son fieles.

* **Richard Dawkins, El Gen Egoista./**
* **Richard Dawkins, El Relojero Ciego./**
* **Richard Dawkins, Escalando el Monte Improbable./**
* **Richard Dawkins, El Rio del Eden./**
* **Daniel Dennett, La Peligrosa Idea de Darwin./**
* **Daniel Dennett, La Evolucion de La Libertad./**
* **Steven Pinker, La Tabla Rasa./**
* **Steven Pinker, El Instinto del Lenguaje./**
* **John Maynard Smith, Evolucion y Teoria de los Juegos./**
* **John Maynard Smith, Animal Signals./**






 
