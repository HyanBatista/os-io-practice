import random

from entities import BlockAcess


def main():
    print("Seleção do intervalo mínimo de blocos.")
    min_block = int(input("Bloco mínimo: "))
    max_block = int(input("Bloco máximo: "))
    disk_accesses = int(input("Quantidade de acessos ao disco: "))

    block_accesses: list[BlockAcess] = []

    for block in [random.randint(min_block, max_block) for _ in range(disk_accesses)]:
        block_accesses.append(BlockAcess(block, random.randint(0, 1)))

    print("\nBlocos requisitados:")
    for access in block_accesses:
        access_type = "Leitura" if access.access_type == 0 else "Escrita"
        print(f"Block #{access.block} \t {access_type}")


if __name__ == "__main__":
    main()
