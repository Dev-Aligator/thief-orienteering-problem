import numpy as np

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

def load_items_in_cities_data(file_path, clean_flag=False, items_in_plan=None):
    items = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start_parsing = False
        for line in lines:
            if "ITEMS SECTION" in line.strip():
                start_parsing = True
                continue
            if start_parsing:
                if len(line.strip()) < 4:
                    break
                parts = line.strip().split()
                index = int(parts[0])
                profit = int(parts[1])
                weight = int(parts[2])
                city = int(parts[3])
                items.append((index, profit, weight, city))
    city_items = {}
    for item in items:
        if clean_flag and item[0] not in items_in_plan:
            continue
        index, profit, weight, city = item
        if city not in city_items:
            city_items[city] = []
        city_items[city].append({'index': index, 'profit': profit, 'weight': weight})
    return city_items

def get_proper_fig_size(n_cities):
    if n_cities < 60:
        return (5, 5)
    if n_cities < 110:
        return (20, 20)
    if n_cities < 300:
        return (30, 30)
    return (40, 40)

def rgbtohex(rgb_color):
    r, g, b = [int(256 * x) for x in rgb_color]
    return f'#{r:02x}{g:02x}{b:02x}'