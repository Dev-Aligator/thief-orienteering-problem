import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageTk, Image
import os
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

def get_proper_fig_size(n_cities):
    if n_cities < 60:
        return (5, 5)
    if n_cities < 110:
        return (20, 20)
    if n_cities < 300:
        return (30, 30)
    return (40, 40)

def construct_map(thop_input_file_path, output_file, thief_route_solution=None, show_solution=True):
    data = load_cities_data(thop_input_file_path)
    x, y = data[:, 1], data[:, 2]
    # Define the path
    if show_solution:
        thief_route_solution.insert(0, 1)
        thief_route_solution.append(len(x))

    # Plotting code
    plt.figure(figsize=get_proper_fig_size(len(x)))
    
    if show_solution:
        # Draw the lines connecting the points in the specified path
        path_coords = [(x[i-1], y[i-1]) for i in thief_route_solution]
        path_x, path_y = zip(*path_coords)
        plt.plot(path_x, path_y, color='black')
    highlight_nodes = [city for city in thief_route_solution] if show_solution else list(range(1, len(x) + 1))
    # Plot the points and annotations
    plt.scatter(x, y, alpha=0)
    for i, (xi, yi) in enumerate(zip(x, y)):
        if i in (0, len(x)-1):
            plt.annotate(str(i + 1), (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center',
                        bbox=dict(boxstyle="round,pad=0.3", edgecolor="red", facecolor="red"))
        else:
            alpha = 1 if i+1 in highlight_nodes else 0.2
            color = get_random_color()
            city_box = plt.annotate(str(i + 1), (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center',
                        bbox=dict(boxstyle="round,pad=0.3", edgecolor=color, facecolor=color, alpha=alpha))
            sub_bbox = dict(boxstyle="round,pad=0.1", edgecolor="white", facecolor="white", alpha=alpha)
            city_node = plt.annotate(str(i + 1), (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center', bbox=sub_bbox)
            city_box.set_alpha(alpha)
            city_node.set_alpha(alpha)
    # Hide x-axis and y-axis values
    plt.xticks([])
    plt.yticks([])
    plt.box(False)
    plt.savefig(output_file, dpi=300)
    image = (Image.open(output_file))
    resized_image= image.resize((1500, 1000), Image.LANCZOS)
    new_image= ImageTk.PhotoImage(resized_image)
    
    if len(x) > 100:
        os.system('feh ' + output_file + ' &')
    return new_image

def main():
    thop_input_file_path = "./acoplusplus_thop/instances/eil51-thop/eil51_01_bsc_05_03.thop"
    thief_route_solution = [32, 11, 38, 9, 50, 16, 2, 29, 21, 20, 35, 36, 3, 28, 31, 8, 26, 48, 23, 7, 24, 14, 25, 13, 41, 19, 42, 44, 15, 37, 17, 18, 4, 47, 12, 46]
    output_file = "thop_visualiser/output/eil51_01_bsc_05_03.png"
    construct_map(thop_input_file_path, thief_route_solution, output_file)
