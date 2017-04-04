

class JsonObject(dict):

    def __getattr__(self, att_key):
        if att_key in self.keys():
            return self[att_key]
        else:
            raise KeyError(att_key)

    def __repr__(self):
        return "<JsonObject [%s]>" % str(super(JsonObject, self).__repr__())
