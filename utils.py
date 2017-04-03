

class JsonObject(dict):

    def __getattribute__(self, att_key):
        if att_key in self:
            return self[att_key]
        elif att_key in dir(self):
            return super(JsonObject, self).__getitem__(att_key)
        else:
            raise KeyError("2")

    def __repr__(self):
        return "<JsonObject [%s]>" % str(super(JsonObject, self).__repr__())