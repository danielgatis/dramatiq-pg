ISOLATION_LEVEL_AUTOCOMMIT: int


def quote_ident(ident: str, scope) -> str:
    ...


class Notify(object):
    payload: str

    def __init__(self, pid: int, channel: str, payload: str):
        ...
