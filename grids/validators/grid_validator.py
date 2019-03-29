from grids.helpers.graph import Graph

class GridValidator(object):
    '''Validator class for grids'''
    
    def __init__(self):
        '''initializing requierd object'''
        self.graph_obj = Graph()
    
    def validate(self, nodes, edges):
        '''valide for a valid grid

        Args:
            edges: List of dictionary
        
        Return:
            Boolean
        '''
        edge_nodes = []
        for item in edges:
            self.graph_obj.add_edge(item.get('start'), item.get('end'), item.get('distance'), item.get('speed'))
            edge_nodes.append(item.get('start'))
            edge_nodes.append(item.get('end'))
       
        if list(set(edge_nodes) - set(nodes)) != [] or list(set(nodes) - set(edge_nodes)) != []:
            return False
        return self.graph_obj.check_all_conected_nodes()