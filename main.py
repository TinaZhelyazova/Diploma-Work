import os
from midi_generator import *
from tabs_reading import Tabs


def main():
    filename = input("Enter file location: ")
    tempo = input("Enter tempo of song: ")
    if tempo == "":
        tempo = 120
    else:
        tempo = int(tempo)

    t = Tabs(filename)
    t.preprocess()
    t.convertNotes()

    outputTrack = Track(int(tempo))
    outputTrack.midiGenerator(t.a)  # t=tabs; a= matrix of tabs notes
    command = "output.mid"
    os.system(command)


if __name__ == '__main__':
    main()
