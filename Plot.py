import matplotlib.pyplot as plt


def draw_line(array1, array2, formatting):
    plt.plot(array1, array2, formatting)


def draw_graph(graph_data):
    plt.title(graph_data['title'])
    for line in graph_data['lines']:
        draw_line(line[0], line[1], line[2])

MAX_TOUCH_VALUE = 100

touch_value = [300, 200, 120, 50]
squares = [10, 20, 30, 40]
max_value_vector = []
for data in touch_value:
    max_value_vector.append(MAX_TOUCH_VALUE)


touch_potential_data = {"title": "Touch Potential Data", "lines": [[squares, touch_value, 'b'],
                                                                   [squares, max_value_vector, 'g']]}
plt.figure()
draw_graph(touch_potential_data)
plt.show()

# plt.figure()
# plt.subplot(1, 3, 1)
# plt.plot(squares, array, 'b', squares, max_value_vector, 'g')
# plt.show()

