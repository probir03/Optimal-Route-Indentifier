'''helper file, which contains helper method for the grid app'''

from grids.helpers.graph import Graph

def find_optimal_route(edges, start, end):
    '''find the optimal route between two node

    Args:
        edges: list (connect edges list)
        start: string (starting node)
        end: string (end node)
    
    Return:
        List
    '''
    graph_obj = Graph()

    for item in edges:
        graph_obj.add_edge(item.get('start'), item.get('end'), item.get('distance'), item.get('speed'))
    
    return graph_obj.find_optimal_path(start, end)