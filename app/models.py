class Trigger:

    def __init__(self) -> None:
        self.status: bool = True

    def on(self) -> None:
        self.status = True

    def off(self) -> None:
        self.status = False

    def is_on(self) -> bool:
        return self.status

trigger = Trigger()
