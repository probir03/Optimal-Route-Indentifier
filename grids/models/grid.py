'''
    Model file for Grid collection
'''
from pymodm import MongoModel, EmbeddedMongoModel, fields, connect
from pymodm.errors import ValidationError

from grids.models.managers.grid_manager import GridManager


# different fields available are :
'''
    'CharField', 'IntegerField', 'BigIntegerField', 'ObjectIdField',
    'BinaryField', 'BooleanField', 'DateTimeField', 'Decimal128Field',
    'EmailField', 'FileField', 'ImageField', 'FloatField',
    'GenericIPAddressField', 'URLField', 'UUIDField',
    'RegularExpressionField', 'JavaScriptField', 'TimestampField',
    'DictField', 'OrderedDictField', 'ListField', 'PointField',
    'LineStringField', 'PolygonField', 'MultiPointField',
    'MultiLineStringField', 'MultiPolygonField', 'GeometryCollectionField',
    'EmbeddedDocumentField', 'EmbeddedDocumentListField', 'ReferenceField'
'''

def is_distinct_grid_name(string):
    """
    custom validator function to check duplicate grid name while inserting new grid.
    """
    if Grid.objects.search_by_name(string):
        raise ValidationError('Grid with same name already exists !!')

class Edge(EmbeddedMongoModel):
    '''EmbeddedMongoModel of edges'''
    start = fields.CharField()
    end = fields.CharField()
    distance = fields.IntegerField()
    speed = fields.IntegerField()

    class Meta:
        '''Meta class for defining meta info of model'''
        final = True
        ignore_unknown_fields = True


class Grid(MongoModel):
    '''MongoModel class for Grid'''

    _id = fields.CharField(primary_key=True)
    name = fields.CharField(validators=[is_distinct_grid_name])
    nodes = fields.ListField()
    edges = fields.EmbeddedDocumentListField(Edge)
    is_deleted = fields.BooleanField(default=False)
    updated_at = fields.CharField()
    created_at = fields.CharField()

    objects = GridManager()

    class Meta:
        '''Meta class for defining meta info of model'''
        collection_name = "Grids"

