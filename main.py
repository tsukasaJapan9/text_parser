from typing import NamedTuple


class Track(NamedTuple):
    artist: str
    song: str


def run():
    tracks = []
    with open("data.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line[3:].replace("\n", "").split("/")
            tracks.append(Track(line[1][1:], line[0][:-1]))

    with open("result.txt", "w") as f:
        f.write("artist\tsong\n")
        for track in tracks:
            f.write(f"{track.artist}\t{track.song}\n")


if __name__ == '__main__':
    run()
