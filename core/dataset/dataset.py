
from JsonAnalysisEngine.internal.factory import Factory


class DatasetBase(object):
    pass


class KeysDataset(DatasetBase, list):
    pass


class ValuesDataset(DatasetBase, list):
    pass


class Dataset(object):

    def __init__(self):
        self.keys_dataset = KeysDataset()
        self.values_dataset = ValuesDataset()

Factory.register('Dataset', cls=Dataset())
