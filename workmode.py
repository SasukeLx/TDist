# workmode: local / remote

class BaseMode:
    def exec(self, cmd: str) -> str:
        raise NotImplementedError

class LocalMode(BaseMode):
    def exec(self, cmd: str) -> str:
        return super().exec(cmd)

class RemoteMode(BaseMode):
    ip: str
    port: int

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def exec(self, cmd: str) -> str:
        return super().exec(cmd)

if __name__ == "__main__":
    pass