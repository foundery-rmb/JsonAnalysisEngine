
import md5


class JsonObject(dict):
    
    parent = None

    def __init__(self, *args, **kwargs):
        super(JsonObject, self).__init__(*args, **kwargs)
        self['parent'] = None

    def __getattr__(self, att_key):
        if att_key in self.keys():
            return self[att_key]
        else:
            raise KeyError(att_key)

    def __repr__(self):
        return "<JsonObject [%s]>" % str(super(JsonObject, self).__repr__())

    def __hash__(self):
        hashed = md5.md5(str(self)).hexdigest()
        return hash(hashed)
