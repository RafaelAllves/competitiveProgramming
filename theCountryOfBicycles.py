# https://www.beecrowd.com.br/judge/pt/problems/view/1454

import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        
    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)
        self.arestas[vertice] = {}
        
    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.arestas[vertice1][vertice2] = peso
        self.arestas[vertice2][vertice1] = peso
        
    def dijkstra(self, origem):
        distancia = {vertice: float('infinity') for vertice in self.vertices}
        distancia[origem] = 0
        fila = [(-float('infinity'), origem)] # inicio com -infinito pois os pesos podem ser negativos

        while fila:
            atual_distancia, atual_vertice = heapq.heappop(fila)

            if atual_distancia > distancia[atual_vertice]:
                continue

            for vizinho, peso in self.arestas[atual_vertice].items():

                # distancia_atualizada = atual_distancia + peso # algoritmo de Dijkstra
                distancia_atualizada = max(atual_distancia, peso) # adptacao

                if distancia_atualizada < distancia[vizinho]:
                    distancia[vizinho] = distancia_atualizada
                    heapq.heappush(fila, (distancia_atualizada, vizinho))

        return distancia

def main():
    instancia = 1

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        print(f'Instancia {instancia}')
        instancia += 1

        grafo = Grafo()

        for i in range(n):
            grafo.adicionar_vertice(i+1)

        for _ in range(m):
            i, j, h = map(int, input().split())
            grafo.adicionar_aresta(i, j, h)

        k = int(input())

        for _ in range(k):
            origem, destino = map(int, input().split())
            if origem == destino:
                print(0)
            else:
                resultados_dijkstra = grafo.dijkstra(origem)

                print(resultados_dijkstra[destino])
        print()


if __name__ == "__main__":
    main()
