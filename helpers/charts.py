import matplotlib.pyplot as plt
import numpy as np


def draw_horizontal_bar_chart(descrpition, data):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(descrpition))

    ax.barh(y_pos, data, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(descrpition)
    ax.invert_yaxis()
    ax.set_xlabel('Used CPU time')
    ax.set_title('P||C max for {} CPUs'.format(len(descrpition)))
    plt.tight_layout()
    plt.savefig("results/graph.png")

    plt.show()
