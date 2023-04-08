import random

from entities import TrackAccess


UNIT_TIME = 1


def compute_partial_seek_time(source_track: int, target_track: int) -> int:
    return abs(source_track - target_track)


def main() -> None:
    print("Seleção do intervalo mínimo de trilhas.")
    min_track = int(input("Trilha mínima: "))
    max_track = int(input("Trilha máxima: "))
    disk_accesses = int(input("Quantidade de acessos ao disco: "))

    track_accesses: list[TrackAccess] = []

    for track in [random.randint(min_track, max_track) for _ in range(disk_accesses)]:
        track_accesses.append(TrackAccess(track, random.randint(0, 1)))

    print("\nTrilhas requisitadas:")
    for access in track_accesses:
        access_type = "Leitura" if access.access_type == 0 else "Escrita"
        print(f"Trilha #{access.track} \t {access_type}")

    print("\nOrdem de acesso às trilhas segundo o mq-deadline:")
    total_seek_time = 0
    read_accesses: list[TrackAccess] = sorted(
        [access for access in track_accesses if access.access_type == 0].copy(),
        key=lambda access: access.track,
    )
    write_accesses: list[TrackAccess] = sorted(
        [access for access in track_accesses if access.access_type == 1].copy(),
        key=lambda access: access.track,
    )

    head = 0
    for index in range(len(read_accesses)):
        partial = compute_partial_seek_time(head, read_accesses[index].track)
        total_seek_time += partial
        head = read_accesses[index].track
        print(f"Trilha #{head} \t Leitura \t Tempo de procura parcial: {partial} u.t.")

    for index in range(len(write_accesses)):
        partial = compute_partial_seek_time(head, write_accesses[index].track)
        total_seek_time += partial
        head = write_accesses[index].track
        print(f"Trilha #{head} \t Escrita \t Tempo de procura parcial: {partial} u.t.")
    print("Tempo total de procura:", total_seek_time, "u.t.")

    print("\nOrder de acesso às trilhas segundo o C-Scan:")
    access_sequence = sorted(
        [access for access in track_accesses].copy(),
        key=lambda access : access.track
    )

    head = max_track // 2
    previous_head = head
    partial = 0
    total_seek_time = 0
    while len(access_sequence) > 0:
        if head == access_sequence[0].track:
            access_type = "Leitura" if access_sequence[0].access_type == 0 else "Escrita"
            total_seek_time += partial
            print(
                f"Trilha #{head} \t {access_type} \t Tempo de procura parcial: {partial} u.t. \t Head Anterior: {previous_head}"
            )
            partial = 0
            access_sequence.pop(0)
            previous_head = head
        
        if len(access_sequence) > 0 and head >= max_track:
            head = 0
        
        partial += compute_partial_seek_time(head, head + 1)
        head += 1
    print("Tempo total de procura:", total_seek_time, "u.t.")


if __name__ == "__main__":
    main()
