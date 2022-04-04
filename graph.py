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
    def adjacency_list_to_matrix(graph: 'list[list[int]]') -> 'list[list[int]]':
        pass
    
    @staticmethod
    def adjacency_matrix_to_list(graph: 'list[list[int]]')-> 'list[list[int]]':
        pass

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
        

if __name__ == '__main__':
    adj_list = [[1,4], [0,2], [1,3], [4,2], [3,0]]
    adj_mat = [
        [0,1,0,0,1],
        [1,0,1,0,0],
        [0,1,0,1,0],
        [0,0,1,0,1],
        [1,0,0,1,0],
    ]
    bfs_list = Graph.bfs_traverse(adj_list, 0, 2)
    print(bfs_list)
    bfs_mat = Graph.bfs_traverse(adj_mat, 0, 2, False)
    print(bfs_mat)
    dfs_list = Graph.dfs_traverse(adj_list, 0, 2)
    print(dfs_list)
    dfs_list = Graph.dfs_traverse(adj_mat, 0, 2, False)
    
    adj_list2 = [[1,3,4], [0], [3,5], [1,0,2], [], [6], []]
    bfs_list2 = Graph.bfs_traverse(adj_list2, 0, 6)
    print(bfs_list2)
