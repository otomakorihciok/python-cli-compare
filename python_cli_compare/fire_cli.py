from typing import Optional


class CLI:
    def __init__(self, base: int = 10):
        self.base = base

    def to_num(self, num: int) -> int:
        return num * self.base
