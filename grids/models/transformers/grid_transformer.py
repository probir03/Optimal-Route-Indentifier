'''Transformer class for Grid COllection'''

class GridTransformer():
    """Transforming Grid data for Response"""

    @staticmethod
    def transform(data):
        '''transform method for data transformation'''
        if isinstance(data, list):
            for item in data:
                item['id'] = item.pop('_id')
                item.pop('is_deleted')
                item['updatedAt'] = item.pop('updated_at', None)
                item['createdAt'] = item.pop('created_at', None)
        
        else:
            data['id'] = data.pop('_id')
            data.pop('is_deleted')
            data['updatedAt'] = data.pop('updated_at', None)
            data['createdAt'] = data.pop('created_at', None)
        return data