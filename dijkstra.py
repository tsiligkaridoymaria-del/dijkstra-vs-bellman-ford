import random
import heapq
import math

VERTICES = ["s", "A", "B", "t"]
P_CONNECTION = 0.7
Q_NEGATIVE_DIRECTION = 0.3
NUM_GRAPHS = 1000


def generate_random_graph():
    graph = {v: [] for v in VERTICES}

    for i in range(len(VERTICES)):
        for j in range(i + 1, len(VERTICES)):
            u = VERTICES[i]
            v = VERTICES[j]

            if random.random() < P_CONNECTION:
                if random.random() < Q_NEGATIVE_DIRECTION:
                    graph[u].append((v, -1))
                    graph[v].append((u, +1))
                else:
                    graph[u].append((v, +1))
                    graph[v].append((u, -1))

    return graph


def has_negative_edges(graph):

    for u in graph:

        for v, weight in graph[u]:

            if weight < 0:

                return True

    return False


def dijkstra(graph, source):

    distances = {v: math.inf for v in graph}
    distances[source] = 0

    visited = set()
    priority_queue = [(0, source)]

    while priority_queue:

        current_distance, u = heapq.heappop(priority_queue)

        if u in visited:

            continue

        visited.add(u)

        for v, weight in graph[u]:

            if v in visited:

                continue

            new_distance = current_distance + weight

            if new_distance < distances[v]:

                distances[v] = new_distance
                heapq.heappush(priority_queue, (new_distance, v))

    return distances


def bellman_ford(graph, source):

    distances = {v: math.inf for v in graph}
    distances[source] = 0

    edges = []

    for u in graph:

        for v, weight in graph[u]:

            edges.append((u, v, weight))

    for _ in range(len(graph) - 1):

        changed = False

        for u, v, weight in edges:

            if distances[u] != math.inf and distances[u] + weight < distances[v]:

                distances[v] = distances[u] + weight
                changed = True

        if not changed:

            break

    has_negative_cycle = False

    for u, v, weight in edges:

        if distances[u] != math.inf and distances[u] + weight < distances[v]:

            has_negative_cycle = True
            break

    return distances, has_negative_cycle


def print_graph(graph):

    for u in graph:

        for v, weight in graph[u]:

            print(f"{u} -> {v} with weight {weight}")


def compare_results(dijkstra_distances, bellman_ford_distances):

    for v in dijkstra_distances:

        if dijkstra_distances[v] != bellman_ford_distances[v]:

            return False

    return True


def main():

    graphs_with_negative_edges = 0
    graphs_with_negative_cycle = 0
    dijkstra_correct = 0
    dijkstra_wrong = 0

    for _ in range(NUM_GRAPHS):

        graph = generate_random_graph()

        if has_negative_edges(graph):

            graphs_with_negative_edges += 1

        dijkstra_distances = dijkstra(graph, "s")
        bellman_ford_distances, negative_cycle = bellman_ford(graph, "s")

        if negative_cycle:

            graphs_with_negative_cycle += 1
            dijkstra_wrong += 1

        else:

            if compare_results(dijkstra_distances, bellman_ford_distances):

                dijkstra_correct += 1

            else:

                dijkstra_wrong += 1

    print("Results")
    print("----------------------")
    print(f"Number of graphs: {NUM_GRAPHS}")
    print(f"Graphs with negative edges: {graphs_with_negative_edges}")
    print(f"Graphs with negative cycle: {graphs_with_negative_cycle}")
    print(f"Cases where Dijkstra was correct: {dijkstra_correct}")
    print(f"Cases where Dijkstra was wrong: {dijkstra_wrong}")


if __name__ == "__main__":
    main()