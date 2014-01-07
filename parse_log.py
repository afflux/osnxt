import sys
from matplotlib import pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    points = []
    turns = []
    with open(sys.argv[1]) as log_file:
        for index, reading in enumerate(log_file):
            if reading.startswith('turning'):
                turns.append(len(points))
                continue
            distance = int(reading.split('=')[1])
            if distance == 255:
                continue
            points.append(distance)
    line, = ax.plot(points)
    plt.ylabel('Readings')
    ax.set_ylim(0, 250)
    for turn in turns:
        print('adding annotation at %d' % turn)
        ax.annotate('turn', xy=(turn, 60), xytext=(turn, 200), arrowprops=dict(facecolor='black', shrink=0.15))
    plt.show()



if __name__ == '__main__':
    main()