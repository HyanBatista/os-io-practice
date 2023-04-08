from dataclasses import dataclass


@dataclass
class Block:
    size: int


@dataclass
class Disk:
    blocks: list[Block]

    @property
    def size(self):
        return sum([block.size for block in self.blocks])
