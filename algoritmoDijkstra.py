import networkx as nx
import matplotlib.pyplot as plt
def agregar_arista(G, u, v, w=1, dirigido=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not dirigido:
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)
def grafico():
    if __name__ == '__main__':
        # Instantiate the DiGraph
        G = nx.DiGraph()

        # Add node/edge pairs
        
        agregar_arista(G, "PLAZA", "OLIVE", 35.04,False)
        agregar_arista(G, "PLAZA", "HOSTAL LOS GERANIOS", 36.29,False)
        agregar_arista(G, "PLAZA", "KAP CAPACITACION Y SOLUCIONES TECNICAS", 32.25,False)
        agregar_arista(G, "PLAZA", "TERRENOS EN VENTA", 61.72, False)
        agregar_arista(G, "OLIVE", "HOSTAL LOS GERANIOS", 19.05, False)
        agregar_arista(G, "OLIVE", "KAP CAPACITACION Y SOLUCIONES TECNICAS", 69.58, False)
        agregar_arista(G, "OLIVE", "TERRENOS EN VENTA", 53.82, False)
        agregar_arista(G, "HOSTAL LOS GERANIOS", "KAP CAPACITACION Y SOLUCIONES TECNICAS", 141.04, False)
        agregar_arista(G, "KAP CAPACITACION Y SOLUCIONES TECNICAS", "TERRENOS EN VENTA", 38.89, False)
        

        # Draw the networks
        #imprimiendo el grafo
        pos = nx.layout.circular_layout(G)
        nx.draw_networkx(G, pos)
        #poniendo el nombre a los lados
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        #graficando el grafo
        plt.title("Ciudad Jardin")
        plt.show()
def graficoCamino(nombrePuntoIncio,nombrePuntoFinal,lado1,lado2=0,nombrePuntoMedio=None):
    if __name__ == '__main__':
        # Instantiate the DiGraph
        if(nombrePuntoMedio==None):
            G = nx.DiGraph()

            # Add node/edge pairs
            
            agregar_arista(G, nombrePuntoIncio, nombrePuntoFinal, lado1,False)
            # Draw the networks
            #imprimiendo el grafo
            pos = nx.layout.circular_layout(G)
            nx.draw_networkx(G, pos)
            #poniendo el nombre a los lados
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            #graficando el grafo
            plt.title("Ciudad Jardin")
            plt.show()
        if(nombrePuntoMedio!=None):
            G = nx.DiGraph()
            agregar_arista(G, nombrePuntoIncio, nombrePuntoMedio, lado1,False)
            agregar_arista(G, nombrePuntoMedio, nombrePuntoFinal, lado2,False)
            pos = nx.layout.circular_layout(G)
            nx.draw_networkx(G, pos)
            #poniendo el nombre a los lados
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            #graficando el grafo
            plt.title("Ciudad Jardin")
            plt.show()
class punto():
    def __init__(self):
        self.__nombre=None
        self.__lado=[]
        self.__opcion=0

    def getLado(self):

        return self.__lado
    
    def getNombre(self):

        return self.__nombre
    def agregarLado(self,lado):

        self.__lado.append(lado)

    def setNombre(self,nombre):

        self.__nombre=nombre

    def getOpcion(self):

        return self.__opcion
    
    def setOpcion(self,opcion):

        self.__opcion=opcion
    def mostrar(self):
      
        for i in range(len(self.__lado)):
            
                print(self.__lado[i])
    
 
    def obtenerLado(self,posicion):
        return self.__lado[posicion]

listaCaminos=[]
listaPuntos=[]
listaNumeros=[]
listaNombre=[]
listaNombre1=[]
listaNombre2=[]
listaNombre3=[]
listaLadoGrafico=[]
listaGrafico=[]
def dijkstra(valor1,valor2):
    bandera=True
    contador=0
    contador2=0
    ladoPunto1_2=punto1.obtenerLado(0)
    ladoPunto1_3=punto1.obtenerLado(1)
    ladoPunto1_4=punto1.obtenerLado(2)
    ladoPunto1_5=punto1.obtenerLado(3)
    ladoPunto2_3=punto2.obtenerLado(1)
    ladoPunto2_4=punto2.obtenerLado(2)
    ladoPunto2_5=punto2.obtenerLado(3)
    ladoPunto3_4=punto3.obtenerLado(2)
    ladoPunto4_5=punto4.obtenerLado(3)
    
    
    if(valor1==1 and valor2==2 or valor1==2 and valor2==1):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
  
        if valor1==int(punto1.getOpcion()):
          
            nombrePartida=punto1.getNombre()
            nombreLlegada=punto2.getNombre()
        else:
            bandera=False
            nombrePartida=punto2.getNombre()
            nombreLlegada=punto1.getNombre()
        contador=ladoPunto1_3+ladoPunto2_3
        
        listaNumeros.append(1)
        listaNombre.append(punto3.getNombre())       
        listaPuntos.append(listaNombre)
        contador2=ladoPunto1_4+ladoPunto4_5+ladoPunto2_5
        listaNumeros.append(2)
        listaNombre1.append(punto4.getNombre())
        listaNombre1.append(punto5.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto1_4+ladoPunto2_4
        listaNumeros.append(3)
        listaNombre2.append(punto4.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto1_4+ladoPunto3_4+ladoPunto2_3
        listaNumeros.append(4)
        listaNombre3.append(punto4.getNombre())
        listaNombre3.append(punto3.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto1_2)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto1_2}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)
    if(valor1==1 and valor2==3 or valor1==3 and valor2==1):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        if valor1==int(punto1.getOpcion()):
            
            nombrePartida=punto1.getNombre()
            nombreLlegada=punto3.getNombre()
        else:
            bandera=False
            nombrePartida=punto3.getNombre()
            nombreLlegada=punto1.getNombre()
        contador=ladoPunto1_2+ladoPunto2_3
        listaNumeros.append(1)
        listaNombre.append(punto2.getNombre())
        listaPuntos.append(listaNombre)
        contador2=ladoPunto1_4+ladoPunto4_5+ladoPunto2_5+ladoPunto2_3
        listaNumeros.append(2)
        listaNombre1.append(punto4.getNombre())
        listaNombre1.append(punto5.getNombre())
        listaNombre1.append(punto2.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto1_4+ladoPunto2_4+ladoPunto2_3
        listaNumeros.append(3)
        listaNombre2.append(punto4.getNombre())
        listaNombre2.append(punto2.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto1_4+ladoPunto3_4
        listaNumeros.append(4)
        listaNombre3.append(punto4.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto1_3)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto1_3}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)

    if(valor1==1 and valor2==4 or valor1==4 and valor2==1):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        if valor1==int(punto1.getOpcion()):
            
            nombrePartida=punto1.getNombre()
            nombreLlegada=punto4.getNombre()
        else:
            bandera=False
            nombrePartida=punto4.getNombre()
            nombreLlegada=punto1.getNombre()
        contador=ladoPunto1_2+ladoPunto2_4
        listaNumeros.append(1)
        listaNombre.append(punto2.getNombre())
        listaPuntos.append(listaNombre)
        contador2=ladoPunto1_2+ladoPunto2_5+ladoPunto4_5
        listaNumeros.append(2)
        listaNombre1.append(punto2.getNombre())
        listaNombre1.append(punto5.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto1_3+ladoPunto3_4
        listaNumeros.append(3)
        listaNombre2.append(punto3.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto1_5+ladoPunto4_5
        listaNumeros.append(4)
        listaNombre3.append(punto5.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto1_4)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto1_4}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)

        
    if(valor1==1 and valor2==5 or valor1==5 and valor2==1):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        if valor1==int(punto1.getOpcion()):
            
            nombrePartida=punto1.getNombre()
            nombreLlegada=punto5.getNombre()
        else:
            bandera=False
            nombrePartida=punto5.getNombre()
            nombreLlegada=punto1.getNombre()
        contador=ladoPunto1_4+ladoPunto4_5
        listaNumeros.append(1)
        listaNombre.append(punto4.getNombre())
        listaPuntos.append(listaNombre)
        contador2=ladoPunto1_2+ladoPunto2_5
        listaNumeros.append(2)
        listaNombre1.append(punto2.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto1_3+ladoPunto3_4+ladoPunto4_5
        listaNumeros.append(3)
        listaNombre2.append(punto3.getNombre())
        listaNombre2.append(punto4.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto1_2+ladoPunto2_5
        listaNumeros.append(4)
        listaNombre3.append(punto2.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto1_5)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto1_5}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)
    if(valor1==2 and valor2==3 or valor1==3 and valor2==2):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        if valor1==int(punto2.getOpcion()):
            
            nombrePartida=punto2.getNombre()
            nombreLlegada=punto3.getNombre()
        else:
            bandera=False
            nombrePartida=punto3.getNombre()
            nombreLlegada=punto2.getNombre()
        
        contador=ladoPunto1_2+ladoPunto1_3
        listaNumeros.append(1)
        listaNombre.append(punto1.getNombre())
        listaPuntos.append(listaNombre)
        contador2=ladoPunto2_4+ladoPunto1_4+ladoPunto1_3
        listaNumeros.append(2)
        listaNombre1.append(punto4.getNombre())
        listaNombre1.append(punto1.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto2_4+ladoPunto3_4
        listaNumeros.append(3)
        listaNombre2.append(punto4.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto2_5+ladoPunto4_5+ladoPunto3_4
        listaNumeros.append(4)
        listaNombre3.append(punto5.getNombre())
        listaNombre3.append(punto4.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto2_3)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto2_3}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera) 
        
        
    if(valor1==2 and valor2==4 or valor1==4 and valor2==2):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        listaGrafico.clear()
        listaLadoGrafico.clear()
        if valor1==int(punto2.getOpcion()):
            
            nombrePartida=punto2.getNombre()
            nombreLlegada=punto4.getNombre()
        else:
            bandera=False
            nombrePartida=punto4.getNombre()
            nombreLlegada=punto2.getNombre()
        
        contador=ladoPunto1_2+ladoPunto1_4
        listaNumeros.append(1)
        listaNombre.append(punto1.getNombre())
        listaPuntos.append(listaNombre)
        if(bandera==True):
            listaLadoGrafico.append(ladoPunto1_2)
            listaLadoGrafico.append(ladoPunto1_4)
            listaGrafico.append(listaLadoGrafico)
        else:
            listaLadoGrafico.append(ladoPunto1_4)
            listaLadoGrafico.append(ladoPunto1_2)
            listaGrafico.append(listaLadoGrafico)
        contador2=ladoPunto2_3+ladoPunto3_4
        listaNumeros.append(2)
        listaNombre1.append(punto3.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto2_5+ladoPunto4_5
        listaNumeros.append(3)
        listaNombre2.append(punto5.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto2_3+ladoPunto1_3+ladoPunto1_4
        listaNumeros.append(4)
        listaNombre3.append(punto3.getNombre())
        listaNombre3.append(punto1.getNombre())
        listaPuntos.append(listaNombre3)
        
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto2_4)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto2_4}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)
        
    if(valor1==2 and valor2==5 or valor1==5 and valor2==2):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        if valor1==int(punto2.getOpcion()):
            
            nombrePartida=punto2.getNombre()
            nombreLlegada=punto5.getNombre()
        else:
            bandera=False
            nombrePartida=punto5.getNombre()
            nombreLlegada=punto2.getNombre()
        contador=ladoPunto1_2+ladoPunto1_5
        listaNumeros.append(1)
        listaNombre.append(punto1.getNombre())
        listaPuntos.append(listaNombre)
        contador2=ladoPunto2_4+ladoPunto4_5
        listaNumeros.append(2)
        listaNombre1.append(punto4.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto2_3+ladoPunto1_3+ladoPunto1_5
        listaNumeros.append(3)
        listaNombre2.append(punto3.getNombre())
        listaNombre2.append(punto1.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto2_3+ladoPunto3_4+ladoPunto4_5
        listaNumeros.append(4)
        listaNombre3.append(punto3.getNombre())
        listaNombre3.append(punto4.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto2_5)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto2_5}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)        
    if(valor1==3 and valor2==4 or valor1==4 and valor2==3):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        listaGrafico.clear()
        listaLadoGrafico.clear()
        if valor1==int(punto3.getOpcion()):
            
            nombrePartida=punto3.getNombre()
            nombreLlegada=punto4.getNombre()
        else:
            bandera=False
            nombrePartida=punto4.getNombre()
            nombreLlegada=punto3.getNombre()
 
        contador=ladoPunto1_3+ladoPunto1_4
        listaNumeros.append(1)
        listaNombre.append(punto1.getNombre())
        listaPuntos.append(listaNombre)
        if(bandera==True):
            listaLadoGrafico.append(ladoPunto1_3)
            listaLadoGrafico.append(ladoPunto1_4)
            listaGrafico.append(listaLadoGrafico)
        else:
            listaLadoGrafico.append(ladoPunto1_4)
            listaLadoGrafico.append(ladoPunto1_3)
            listaGrafico.append(listaLadoGrafico)

        contador2=ladoPunto2_3+ladoPunto1_2+ladoPunto1_4
        listaNumeros.append(2)
        listaNombre1.append(punto2.getNombre())
        listaNombre1.append(punto1.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto2_3+ladoPunto2_5+ladoPunto4_5
        listaNumeros.append(3)
        listaNombre2.append(punto2.getNombre())
        listaNombre2.append(punto5.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto1_3+ladoPunto1_5+ladoPunto4_5
        listaNumeros.append(4)
        listaNombre3.append(punto1.getNombre())
        listaNombre3.append(punto5.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto3_4)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto3_4}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")

        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)
    if(valor1==4 and valor2==5 or valor1==5 and valor2==4):
        listaCaminos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaNombre1.clear()
        listaNombre2.clear()
        listaNombre3.clear()
        listaGrafico.clear()
        listaLadoGrafico.clear()
        if valor1==int(punto4.getOpcion()):
            
            nombrePartida=punto4.getNombre()
            nombreLlegada=punto5.getNombre()
        else:
            bandera=False
            nombrePartida=punto5.getNombre()
            nombreLlegada=punto4.getNombre()
        contador=ladoPunto1_4+ladoPunto1_5
        listaNumeros.append(1)
        listaNombre.append(punto1.getNombre())
        listaPuntos.append(listaNombre)
        
        contador2=ladoPunto2_4+ladoPunto2_5
        listaNumeros.append(2)
        listaNombre1.append(punto2.getNombre())
        listaPuntos.append(listaNombre1)
        contador3=ladoPunto1_4+ladoPunto1_3+ladoPunto2_3+ladoPunto2_5
        listaNumeros.append(3)
        listaNombre2.append(punto1.getNombre())
        listaNombre2.append(punto3.getNombre())
        listaNombre2.append(punto2.getNombre())
        listaPuntos.append(listaNombre2)
        contador4=ladoPunto3_4+ladoPunto2_3+ladoPunto2_5
        listaNumeros.append(4)
        listaNombre3.append(punto4.getNombre())
        listaNombre3.append(punto2.getNombre())
        listaPuntos.append(listaNombre3)
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        listaCaminos.append(ladoPunto4_5)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        print(f"camino 1: {ladoPunto4_5}")
        print(f"camino 2: {camino1}")
        print(f"camino 3: {camino2}")
        print(f"camino 4: {camino3}")
        print(f"camino 5: {camino4}")
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)
    if(valor1==3 and valor2==5 or valor1==5 and valor2==3):
        listaCaminos.clear()
        listaPuntos.clear()
        listaNumeros.clear()
        listaNombre.clear()
        listaGrafico.clear()
        listaLadoGrafico.clear()
        if valor1==int(punto3.getOpcion()):
            
            nombrePartida=punto3.getNombre()
            nombreLlegada=punto5.getNombre()
        else:
            bandera=False
            nombrePartida=punto5.getNombre()
            nombreLlegada=punto3.getNombre()
        contador=ladoPunto2_3+ladoPunto2_5
        listaNumeros.append(0)
        listaNombre.append(punto2.getNombre())
        
        listaPuntos.append(listaNombre)
        
        if(bandera==True):
            listaLadoGrafico.append(ladoPunto2_3)
            listaLadoGrafico.append(ladoPunto2_5)
            listaGrafico.append(listaLadoGrafico)
        else:
            listaLadoGrafico.append(ladoPunto2_5)
            listaLadoGrafico.append(ladoPunto2_3)
            listaGrafico.append(listaLadoGrafico)
        
        contador2=ladoPunto1_3+ladoPunto1_5
        contador3=ladoPunto2_3+ladoPunto1_4+ladoPunto4_5
        contador4=ladoPunto3_4+ladoPunto4_5
        contador5=ladoPunto2_3+ladoPunto1_2+ladoPunto1_5
        camino1=round(contador,2)
        camino2=round(contador2,2)
        camino3=round(contador3,2)
        camino4=round(contador4,2)
        camino5=round(contador5,2)
        listaCaminos.append(camino1)
        listaCaminos.append(camino2)
        listaCaminos.append(camino3)
        listaCaminos.append(camino4)
        listaCaminos.append(camino5)
        print(f"camino 1: {camino1}")
        print(f"camino 2: {camino2}")
        print(f"camino 3: {camino3}")
        print(f"camino 4: {camino4}")
        print(f"camino 5: {camino5}")
        
        menor(listaCaminos,nombrePartida,nombreLlegada,bandera)
#***************************************************************************************
#***************************funcion para determinar el menor valor************************************************************ 
def menor(lista,nombrePartida,nombreLlegada,bandera):
    contador=0
    cont=0
    medio=0
    menor=0
    Incio=0
    tamañoLista=len(lista)-1
 

    while cont<len(lista):
        if cont<tamañoLista:
            if(cont==0 and cont+1==tamañoLista):
                if(lista[cont]<lista[cont+1]):
                    print(f"el camino mas optimo para llegar del punto {nombrePartida} al lugar {nombreLlegada} con {lista[cont]} M")
                    print(f"pasando directamenta de {nombrePartida} a {nombreLlegada}")
                    graficoCamino(nombrePartida,nombreLlegada,menor) 
                    break
                elif(lista[cont+1]<lista[cont]):
                     print(f"el camino mas optimo para llegar del punto {nombrePartida} al lugar {nombreLlegada} con {lista[cont+1]} M")
                     print(f"pasando directamenta de {nombrePartida} a {nombreLlegada}")
                     graficoCamino(nombrePartida,nombreLlegada,menor) 
                     break
            elif(cont==0):
                Incio=lista[cont]
       
        if (cont>0 and cont<tamañoLista):
            
            if(cont>0 and cont>1 and cont<tamañoLista):
                    
                if(medio<lista[cont] and medio<lista[cont+1] and medio<lista[cont-1] and medio<Incio):
                            medio=medio
            elif(lista[cont]<lista[cont+1] and lista[cont]<Incio and lista[cont]<lista[cont-1]):
                    medio=lista[cont]
                    

            else: 
                   
                    if(lista[cont+1]<lista[cont] and lista[cont+1]<Incio and lista[cont+1]<lista[cont-1]):
                        medio=lista[cont+1]

                    elif(lista[cont-1]==Incio):
                         medio=Incio
                   
                    elif(lista[cont-1]<Incio):
                        medio=lista[cont-1]
                    else:
                        medio=Incio
             
        if(cont==tamañoLista and lista[cont]<lista[cont-1] and lista[cont]<medio):
            menor=lista[cont]
            
            print(f"el camino mas optimo para llegar del punto {nombrePartida} al lugar {nombreLlegada} es {menor} M")
        elif(cont==tamañoLista):
            if(lista[cont-1]==medio):
                menor=medio
                print(f"el camino mas optimo para llegar del punto {nombrePartida} al lugar {nombreLlegada} es {menor} M")

                
            elif(lista[cont-1]<medio):
                menor=lista[cont-1]
                print(f"el camino mas optimo para llegar del punto {nombrePartida} al lugar {nombreLlegada} es {menor} M")

            else:
                menor=medio
                print(f"el camino mas optimo para llegar del punto {nombrePartida} al lugar {nombreLlegada} es {menor} M")

        
          
        cont=cont+1
        #**mostrando por que punto o lugar esta pasando el camino****************************************************************************************************
        #*********************************************************************************************************************************
        if(cont==tamañoLista+1):
            
            while contador<len(lista):
                if(contador<len(lista) and contador<len(listaNumeros)):
                    
                    if(listaNumeros[contador]==0 and menor==lista[contador] ):
          
                           
                        print(f"pasando por {listaPuntos[contador][contador]}")
                        
                        graficoCamino(nombrePartida,nombreLlegada,listaGrafico[contador][contador],listaGrafico[contador][contador+1],listaPuntos[contador][contador])
                    elif(listaNumeros[contador]==1 and contador<len(listaNumeros) and menor==lista[1]):
          
                           
                        print(f"pasando por {listaPuntos[contador][contador]}")
                        graficoCamino(nombrePartida,nombreLlegada,listaGrafico[contador][contador],listaGrafico[contador][contador+1],listaPuntos[contador][contador])

                        break
                    elif(contador<len(lista) and contador<len(listaNumeros) and menor==lista[contador]):

                        print(f"pasando directamenta de {nombrePartida} a {nombreLlegada}")

                        graficoCamino(nombrePartida,nombreLlegada,menor) 
                    elif(len(listaPuntos[contador])>1 and len(listaPuntos[contador])==2 and bandera==True and menor==lista[contador]):
                            print(f"pasando por {listaPuntos[contador][contador]} Y {listaPuntos[contador][contador+1]}")
                    elif(len(listaPuntos[contador])>1 and len(listaPuntos[contador])==2 and bandera==False and menor==lista[contador]):
                            print(f"pasando por {listaPuntos[contador][contador+1]} Y {listaPuntos[contador][contador]}")
                        

                contador=contador+1
      
punto1=punto()
punto1.setNombre("PLAZA")
punto1.setOpcion(1)
punto1.agregarLado(35.04)
punto1.agregarLado(36.29)
punto1.agregarLado(32.25)
punto1.agregarLado(61.72)

punto2=punto()
punto2.setNombre("OLIVE")
punto2.setOpcion(2)
punto2.agregarLado(35.04)
punto2.agregarLado(19.05)
punto2.agregarLado(69.58)
punto2.agregarLado(53.82)

punto3=punto()
punto3.setNombre("HOSTAL LOS GERANIOS")
punto3.setOpcion(3)
punto3.agregarLado(36.29)
punto3.agregarLado(19.05)
punto3.agregarLado(141.04)

punto4=punto()
punto4.setNombre("KAP CAPACITACION Y SOLUCIONES TECNICAS")
punto4.setOpcion(4)
punto4.agregarLado(32.25)
punto4.agregarLado(69.58)
punto4.agregarLado(141.04)
punto4.agregarLado(38.89)
punto5=punto()
punto5.setNombre("TERRENOS EN VENTA")
punto5.setOpcion(5)
punto5.agregarLado(5.37)
punto5.agregarLado(119.65)
punto5.agregarLado(38.89)
respuesta="si"
while respuesta!="no" and respuesta!="NO" and respuesta!="No" and respuesta!="nO":
    print("estos son los lugares que hay")
    print(f"1.{punto1.getNombre()}")
    print(f"2.{punto2.getNombre()}")
    print(f"3.{punto3.getNombre()}")
    print(f"4.{punto4.getNombre()}")
    print(f"5.{punto5.getNombre()}")
    
    print("en que lugar estas")
    grafico()
    opcionInicial=int(input())
    if(opcionInicial>0 and opcionInicial<=5):
       
        print("a que lugar quieres llegar")
        opcionFinal=int(input())
        if(opcionFinal>0 and opcionFinal<=5):
            
            dijkstra(opcionInicial,opcionFinal)
            
            
            print("quieres continuar si/no")
            respuesta=input()
        else:
            print("vuelve a escribir")
    else:
        print("vuelve a escribir")
  


