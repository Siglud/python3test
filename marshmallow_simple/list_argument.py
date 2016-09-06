from marshmallow import Schema, fields


class ListArgument(Schema):
    uid = fields.Integer(required=True)
    time = fields.Integer(required=True)

    def handle_error(self, error, data):
        raise Exception("A Error occurs! {}".format(error))


class ListDict(Schema):
    class __ContentDict(Schema):
        mid = fields.Integer(required=True)
        date = fields.Integer(required=True)

    history = fields.Nested(__ContentDict, many=True)


if __name__ == "__main__":
    l = ListArgument(many=True)
    res = l.load([dict(uid=1, time=2), dict(uid=3, time=2)])
    print(res.errors)
    print(res.data)

    ld = ListDict()
    res = ld.load(dict(history=[dict(mid=1, date=2), dict(mid=3, date=4)]))
    print(res.errors)
    print(res.data)
