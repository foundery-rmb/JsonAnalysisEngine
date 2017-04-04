
from JsonAnalysisEngine.internal.factory import Factory

import collections

class DatasetBase(collections.Counter):
    pass


class KeysContainer(DatasetBase):
    pass


class ValuesContainer(DatasetBase):
    pass


class Dataset(object):

    def __init__(self):
        self.keys_container = get_container(KeysContainer)
        self.values_container = get_container(ValuesContainer)


def MakeContainer(container_class, *args, **kwargs):
    """
    factory entry point for containers
    """

    if container_class == KeysContainer:
        container = Factory.classes.get('KeysContainer')
        if not container:
            Factory.register('KeysContainer', cls=KeysContainer(*args, **kwargs))
        return Factory.KeysContainer
    elif container_class == ValuesContainer:
        container = Factory.classes.get('ValuesContainer')
        if not container:
            Factory.register('ValuesContainer', cls=ValuesContainer(*args, **kwargs))
        return Factory.ValuesContainer

Factory.register('Dataset', cls=Dataset())
