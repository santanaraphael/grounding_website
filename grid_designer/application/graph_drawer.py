import matplotlib.pyplot as plt


def draw_line(array1, array2, formatting, legend):
    plt.plot(array1, array2, label=legend)


def draw_graph(graphs):

    for index, graph_data in enumerate(graphs):
        plt.subplot(len(graphs), 1, index + 1)
        plt.title(graph_data['title'])
        for line in graph_data['lines']:
            draw_line(line[0], line[1], line[2], line[3])

        plt.legend()
        plt.ylabel(graph_data['labels'][0])
        plt.xlabel(graph_data['labels'][1])
