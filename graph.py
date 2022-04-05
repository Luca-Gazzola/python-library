from collections import deque

class Graph(object):
    # Static Public methods
    @staticmethod
    def bfs_traverse(graph: 'list[list[int]]', start: int, end: int, is_adjacency_list: bool = True) -> 'list[int]':
        """Finds the shortest path via Breadth-First Search through the graph from start to end given that the path exists.

        Args:
            graph (list[list[int]]): Graph in the form of an adjacency list or matrix.
            start (int): Starting graph node.
            end (int): Ending graph node.

        Returns:
            list[int]: Returns shortest path found, otherwise returns None if no path exists.
        """
        return Graph.__bfs_list_traverse__(graph, start, end) if is_adjacency_list else Graph.__bfs_matrix_traverse__(graph, start, end)
    
    @staticmethod
    def dfs_traverse(graph: 'list[list[int]]', start: int, end: int, is_adjacency_list: bool = True) -> 'list[int]':
        """Finds the shortest path via Depth-First Search through the graph from start to end given that the path exists.

        Args:
            graph (list[list[int]]): Graph in the form of an adjacency list or matrix.
            start (int): Starting graph node.
            end (int): Ending graph node.

        Returns:
            list[int]: Returns shortest path found, otherwise returns None if no path exists.
        """
        return Graph.__dfs_list_traverse__(graph, end, start, [start])
    
    @staticmethod
    def dijkstra(graph: 'list[list[int]]', start: int, end: int) -> 'list[int]':
        """Finds the shortest path via Dijkstra's Algorithm. This assumes that the graph passed in is in the form of an
        adjacency matrix that contains weights.

        Args:
            graph (list[list[int]]): An adjacency matrix with weights on each edge.
            start (int): Starting graph node.
            end (int): Ending graph node.

        Returns:
            list[int]: Returns shortest path found, otherwise returns None if no path exists.
        """
        pass
    
    @staticmethod
    def dijkstra_pq(graph: 'list[list[int]]', start: int, end: int) -> 'list[int]':
        """Finds the shortest path via Dijkstra's Algorithm implemented with a min-priority queue. This assumes that the
        graph passed in is in the form of an adjacency matrix that contains weights.

        Args:
            graph (list[list[int]]): An adjacency matrix with weights on each edge.
            start (int): Starting graph node.
            end (int): Ending graph node.

        Returns:
            list[int]: Returns shortest path found, otherwise returns None if no path exists.
        """
        pass
    
    @staticmethod
    def adjacency_list_to_matrix(list: 'list[list[int]]', weights: 'list[list[int]]' = None) -> 'list[list[int]]':
        """Converts an adjacency list and respective weights (if provided) to an adjacency matrix.

        Args:
            list (list[list[int]]): Adjacency list to convert.
            weights (list[list[int]], optional): Weights list to apply custom weights per edge. Defaults to None.

        Returns:
            list[list[int]]: Returns full adjacency matrix derived from the adjacency matrix, where each edge is
            represented by its weight (provided by the weights list).
        """
        result = []
        if weights is None:
            for neighbors in list:
                result.append([1 if edge in neighbors else 0 for edge in range(len(list))])
        else:
            for neighbors, weight in zip(list, weights):
                row = [0 for _ in range(len(list))]
                for adj, w in zip(neighbors, weight):
                    row[adj] = w
                result.append(row)
        
        return result          
    
    @staticmethod
    def adjacency_matrix_to_list(matrix: 'list[list[int]]')-> 'tuple[list[list[int]], list[list[int]]]':
        """Converts an adjacency matrix to an adjacency list and its associated weights list.

        Args:
            matrix (list[list[int]]): Matrix to convert.

        Returns:
            tuple[list[list[int]], list[list[int]]]: Returns the resulting edges and weights as a tuple ->
            (adjacency_list, weights)
        """
        result_edges = []
        result_weights = []
        for node in range(len(matrix)):
            neighbors = []
            weights = []
            for adjacent, weight in enumerate(matrix[node]):
                if weight > 0:
                    neighbors.append(adjacent)
                    weights.append(weight)
            result_edges.append(neighbors)
            result_weights.append(weights)

        return (result_edges, result_weights)

    # Static Private methods
    @staticmethod
    def __bfs_list_traverse__(graph: 'list[list[int]]', start: int, end: int) -> 'list[int]':
        # Prepare backtrace and deque
        visited = { start: None }
        queue = deque([start])
        while queue:
            # Grab next node
            node = queue.popleft()
            
            # If we find the end, return out and backtrace results
            if node == end:
                path = []
                while node is not None:
                    path.append(node)
                    node = visited[node]
                return path[::-1]
            
            # Continue trying to find the end
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited[neighbor] = node
                    queue.append(neighbor)
        
        # If no path found, return nothing
        return None
    
    @staticmethod
    def __bfs_matrix_traverse__(graph: 'list[list[int]]', start: int, end: int) -> 'list[int]':
        # Prepare backtrace and deque
        visited = { start: None }
        queue = deque([start])
        while queue:
            # Grab next node
            node = queue.popleft()
            
            # If we find the end, return out and backtrace results
            if node == end:
                path = []
                while node is not None:
                    path.append(node)
                    node = visited[node]
                return path[::-1]
            
            # Continue trying to find the end
            for neighbor, edge in enumerate(graph[node]):
                if edge == 1 and neighbor not in visited:
                    visited[neighbor] = node
                    queue.append(neighbor)
        
        # If no path found, return nothing
        return None
    
    @staticmethod
    def __dfs_list_traverse__(graph: 'list[list[int]]', end: int, node: int, path: 'list[int]') -> 'list[int]':
        # If we're at the end, return out
        if node == end:
            return list(path)
        
        # Keep recursing until we reach destination
        found_paths = []
        for neighbor in graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                found_paths.append(Graph.__dfs_list_traverse__(graph, end, neighbor, path))
                path.remove(neighbor)
        
        # Return minimum length path found
        if found_paths:
            return min(found_paths)
        return []
    
    @staticmethod
    def __dfs_matrix_traverse__(graph: 'list[list[int]]', end: int, node: int, path: 'list[int]') -> 'list[int]':
        pass
        

if __name__ == '__main__':
    adj_list = [[1,4], [0,2], [1,3], [2,4], [0,3]]
    adj_mat = [
        [0,1,0,0,1],
        [1,0,1,0,0],
        [0,1,0,1,0],
        [0,0,1,0,1],
        [1,0,0,1,0],
    ]
    
    adj_list2 = [[1,3,4], [0], [3,5], [1,0,2], [], [6], []]
    
    weighted_adj_mat = [
        [0,  4,  0,  0,  0,  0,  0,  8,  0],
        [4,  0,  8,  0,  0,  0,  0, 11,  0],
        [0,  8,  0,  7,  0,  4,  0,  0,  2],
        [0,  0,  7,  0,  9, 14,  0,  0,  0],
        [0,  0,  0,  9,  0, 10,  0,  0,  0],
        [0,  0,  4, 14, 10,  0,  2,  0,  0],
        [0,  0,  0,  0,  0,  2,  0,  1,  6],
        [8, 11,  0,  0,  0,  0,  1,  0,  7],
        [0,  0,  2,  0,  0,  0,  6,  7,  0],
    ]
    weighted_adj_list, weighted_adj_list_weights = Graph.adjacency_matrix_to_list(weighted_adj_mat)
    
    print("Checking basic graph forms/conversions")
    print(Graph.adjacency_matrix_to_list(adj_mat)[0])
    print(Graph.adjacency_list_to_matrix(adj_list))
    print()
    
    print("Checking weighted variants of graph representations")
    print(weighted_adj_mat)
    print(weighted_adj_list)
    print(Graph.adjacency_list_to_matrix(weighted_adj_list, weighted_adj_list_weights))
    print()
    
    print("Checking BFS Traversals with both graph forms")
    bfs_list = Graph.bfs_traverse(adj_list, 0, 2)
    print(bfs_list)
    bfs_mat = Graph.bfs_traverse(adj_mat, 0, 2, False)
    print(bfs_mat)
    bfs_list2 = Graph.bfs_traverse(adj_list2, 0, 6)
    print(bfs_list2)
    print()
    
    print("Checking DFS Traversals with both graph forms")
    dfs_list = Graph.dfs_traverse(adj_list, 0, 2)
    print(dfs_list)
    dfs_mat = Graph.dfs_traverse(adj_mat, 0, 2, False)
    print(dfs_mat)
