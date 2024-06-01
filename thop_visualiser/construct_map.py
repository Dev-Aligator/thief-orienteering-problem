import numpy as np
from matplotlib import pyplot as plt

def get_random_color():
    return list(np.random.choice(range(256), size=3) / 256)

def load_cities_data(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start_parsing = False
        for line in lines:
            if "NODE_COORD_SECTION" in line.strip():
                start_parsing = True
                continue
            if start_parsing:
                if "ITEMS SECTION" in line.strip():
                    break
                parts = line.strip().split()
                index = int(parts[0])
                x = float(parts[1])
                y = float(parts[2])
                coordinates.append((index, x, y))
    return np.array(coordinates)

def construct_map(thop_input_file_path, thief_route_solution, output_file):
    data = load_cities_data(thop_input_file_path)
    x, y = data[:, 1], data[:, 2]

    # Define the path
    thief_route_solution = [32, 11, 38, 9, 50, 16, 2, 29, 21, 20, 35, 36, 3, 28, 31, 8, 26, 48, 23, 7, 24, 14, 25, 13, 41, 19, 42, 44, 15, 37, 17, 18, 4, 47, 12, 46]
    thief_route_solution.insert(0, 1)
    thief_route_solution.append(len(x))

    # Plotting code
    plt.figure()

    # Draw the lines connecting the points in the specified path
    path_coords = [(x[i-1], y[i-1]) for i in thief_route_solution]
    path_x, path_y = zip(*path_coords)
    plt.plot(path_x, path_y, color='black')

    # Plot the points and annotations
    plt.scatter(x, y, alpha=0)
    for i, (xi, yi) in enumerate(zip(x, y)):
        if i in (0, len(x)-1):
            plt.annotate(str(i + 1), (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center',
                        bbox=dict(boxstyle="round,pad=0.3", edgecolor="red", facecolor="red"))
        else:
            color = get_random_color()
            plt.annotate(str(i + 1), (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center',
                        bbox=dict(boxstyle="round,pad=0.3", edgecolor=color, facecolor=color))
            sub_bbox = dict(boxstyle="round,pad=0.1", edgecolor="white", facecolor="white")
            plt.annotate(str(i + 1), (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center', bbox=sub_bbox)

    # Hide x-axis and y-axis values
    plt.xticks([])
    plt.yticks([])
    plt.box(False)

    plt.savefig(output_file, bbox_inches='tight', pad_inches=0.2, dpi=300)

if __name__ == '__main__':
    thop_input_file_path = "./acoplusplus_thop/instances/eil51-thop/eil51_01_bsc_05_03.thop"
    thief_route_solution = [32, 11, 38, 9, 50, 16, 2, 29, 21, 20, 35, 36, 3, 28, 31, 8, 26, 48, 23, 7, 24, 14, 25, 13, 41, 19, 42, 44, 15, 37, 17, 18, 4, 47, 12, 46]
    output_file = "thop_visualiser/output/eil51_01_bsc_05_03.png"
    construct_map(thop_input_file_path, thief_route_solution, output_file)
