from dataclasses import dataclass


@dataclass
class BlockAcess:
    """Acesso ao bloco.

    Se o tipo de acesso for 0, então é leitura. Caso contrário, é escrita.
    """
    block: int
    access_type: int
