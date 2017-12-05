def trueReturn(data, msg, code=200):
    return {
        "status": True,
        "data": data,
        "msg": msg,
        "code": code
    }


def falseReturn(data, msg, code=200):
    return {
        "status": False,
        "data": data,
        "msg": msg,
        "code": code
    }

