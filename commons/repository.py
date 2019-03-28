from models import *
import datetime

def filterByAttribute(modelName, filterKeys):
    return modelName.objects.get(**filterKeys)

def filter_attribute(modelName, filterKeys):
    return modelName.objects.filter(**filterKeys)

def update(modelName, filterKeys, updateWith):
    updateWith.update({'updated_at':datetime.datetime.now()})
    return modelName.objects.filter(**filterKeys).update(**updateWith) 

def fetchAll(modelName):
    return modelName.objects.all()

def store(modelName, values):
    return modelName.objects.create(**values)

def delete(modelName, filterKeys):
    return modelName.objects.filter(**filterKeys).delete()