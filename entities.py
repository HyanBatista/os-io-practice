from dataclasses import dataclass


@dataclass
class TrackAccess:
    """Acesso ao bloco.

    Se o tipo de acesso for 0, então é leitura. Caso contrário, é escrita.
    """
    track: int
    access_type: int
