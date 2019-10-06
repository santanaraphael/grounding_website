import math
import matplotlib.pyplot as plt
from grid_designer.application.graph_drawer import draw_graph


def calc_max_values_50(trip_time, ground_ro, gravel_ro, gravel_depth):
    max_current = 0.116 / math.sqrt(trip_time)
    correction_factor = 1 - (0.09 * (1 - ground_ro / gravel_ro
                                     ) / (2 * gravel_depth + 0.09))

    max_touch_voltage = (1000 + 1.5 * correction_factor * gravel_ro) * max_current
    max_step_voltage = (1000 + 6 * correction_factor * gravel_ro) * max_current

    return max_touch_voltage, max_step_voltage


def calc_max_values_70(trip_time, ground_ro, gravel_ro, gravel_depth):
    max_current = 0.157 / math.sqrt(trip_time)
    correction_factor = 1 - (0.09 * (1 - ground_ro / gravel_ro
                                     ) / (2 * gravel_depth + 0.09))

    max_touch_voltage = (1000 + 1.5 * correction_factor * gravel_ro) * max_current
    max_step_voltage = (1000 + 6 * correction_factor * gravel_ro) * max_current

    return max_touch_voltage, max_step_voltage


def evaluate_conductor_diameter(fault_current, kf, trip_time):
    conductor_section_kcmil = fault_current * kf * math.sqrt(trip_time)
    conductor_section_mm = conductor_section_kcmil / 1.974
    diameter = (2 * math.sqrt(conductor_section_mm / math.pi)) / 1000
    if diameter < 0.01:
        diameter = 0.01
    return diameter


def evaluate_grid_resistance(width, height, depth, spacement, ground_ro):
    horizontal_conductors = (height / spacement) + 1
    vertical_conductors = (width / spacement) + 1
    total_length = horizontal_conductors * width + vertical_conductors * height
    area = width * height
    equivalent_resistance = ground_ro * (
        (1 / total_length) + (1 / math.sqrt(20 * area)) * (
            1 + (1 / (1 + depth * math.sqrt(20 / area)))))
    return equivalent_resistance


def evaluate_ground_potential_rise(maximum_current, grid_resistance):
    return maximum_current * grid_resistance


def evaluate_voltages(**kwargs):

    width = kwargs.get('width')
    height = kwargs.get('height')
    spacement = kwargs.get('spacement')
    depth = kwargs.get('depth')

    diameter = kwargs.get('diameter')
    ig = kwargs.get('ig')

    ro = kwargs.get('ro')

    ground_rods = kwargs.get('ground_rods')
    rods_length = kwargs.get('rods_length')
    rods_number = kwargs.get('rods_number')

    horizontal_conductors = (height / spacement) + 1
    vertical_conductors = (width / spacement) + 1
    total_length = horizontal_conductors * width + vertical_conductors * height

    individual_rod_length = 0
    if not ground_rods:
        lm = total_length + rods_length
    else:
        individual_rod_length = (rods_length / rods_number)
        lm = total_length + rods_length * (
            1.55 + (1.22 * (individual_rod_length / math.sqrt(math.pow(height, 2) + math.pow(width, 2))))
        )

    area = width * height
    perimeter = 2 * width + 2 * height

    na = (2 * total_length) / perimeter
    nb = math.sqrt(perimeter / (4 * math.sqrt(area)))
    n_eq = na * nb

    if ground_rods:
        kii = 1
    else:
        kii = (1 / math.pow(2 * n_eq, (2 / n_eq)))

    ki = 0.644 + 0.148 * n_eq
    kh = math.sqrt(1 + depth)

    km = (1 / (2 * math.pi)) * (math.log((
        math.pow(spacement, 2) / (16 * depth * diameter)
    ) + (math.pow(spacement + 2 * depth, 2) / (
        8 * spacement * diameter
    )) - (depth / (4 * diameter))) + (kii / kh) * math.log(
        8 / (math.pi * (2 * n_eq - 1))
    ))

    mesh_voltage = (ro * km * ki * ig) / lm

    ls = 0.75 * total_length + 0.85 * rods_length

    ks = (1 / math.pi) * (
        (1 / (2 * depth)) + (1 / (spacement + depth)) + (1 / spacement) * (1 - math.pow(0.5, n_eq - 2))
    )

    step_voltage = (ro * ks * ki * ig) / ls

    return mesh_voltage, step_voltage


def evaluate_case(case_info):
    name = case_info['name']
    trip_time = case_info['trip_time']
    ground_ro = case_info['ground_resistivity']
    gravel_ro = case_info['gravel_resistivity']
    gravel_depth = case_info['gravel_depth']
    width = case_info['grid_width']
    height = case_info['grid_height']
    depth = case_info['grid_depth']
    spacement = case_info['spacement']
    if_ground_rods = case_info['if_ground_rods']
    rods_length = case_info['rods_length']
    rods_number = case_info['rods_number']

    max_grid_current = case_info['max_grid_current']
    fault_current = case_info['fault_current']
    conductor_kf = case_info['conductor_kf']
    increment_step = case_info['increment_step']

    ground_potential_rise_array = []
    touch_array = []
    step_array = []
    spacement_array = []

    [max_touch, max_step] = calc_max_values_70(trip_time, ground_ro, gravel_ro, gravel_depth)
    conductor_diameter = evaluate_conductor_diameter(fault_current, conductor_kf, trip_time)

    not_finished = True
    success = False

    while not_finished:
        grid_resistance = evaluate_grid_resistance(width, height, depth, spacement, ground_ro)
        gpr = evaluate_ground_potential_rise(max_grid_current, grid_resistance)
        print(if_ground_rods, width, height, spacement, conductor_diameter, depth,
              ground_ro, max_grid_current, rods_length, rods_number)

        kwargs = {
            'width': width,
            'height': height,
            'spacement': spacement,
            'depth': depth,
            'diameter': conductor_diameter,
            'ro': ground_ro,
            'ig': max_grid_current,
            'ground_rods': if_ground_rods,
            'rods_length': rods_length,
            'rods_number': rods_number
        }

        [mesh_voltage, step_voltage] = evaluate_voltages(**kwargs)

        ground_potential_rise_array.append(gpr)
        step_array.append(step_voltage)
        touch_array.append(mesh_voltage)
        spacement_array.append(spacement)

        if gpr < max_touch:
            print('gpr {} < max touch {}'.format(gpr, max_touch))
            not_finished = False
            success = True
        elif (mesh_voltage < max_touch) and (step_voltage < max_step):
            print('mesh {} < max touch {} and step {} < max step {}'.format(mesh_voltage, max_touch, step_voltage,
                                                                            max_step))
            not_finished = False
            success = True
        else:
            print(
                'gpr {}, mesh {}, step {}, max touch {}, max step {}'.format(gpr, mesh_voltage, step_voltage, max_touch,
                                                                             max_step))
            print('Decreasing the spacement from {} to {}'.format(spacement, spacement - increment_step))

            if spacement <= increment_step:
                not_finished = False
                print("Couldn't find a solution")
            else:
                spacement = spacement - increment_step

    max_touch_vector = []
    max_step_vector = []
    for data in step_array:
        max_step_vector.append(max_step)
    for data in touch_array:
        max_touch_vector.append(max_touch)

    touch_potential_data = {
        "title": "Touch Potential Data",
        "lines": [
            [spacement_array, touch_array, 'b', 'Touch Potential'],
            [spacement_array, max_touch_vector, 'g', 'Max Touch Potential']
        ],
        "labels": [
            'Touch Potential (V)', 'Spacement (m)'
        ]
    }

    step_potential_data = {
        "title": "Step Potential Data",
        "lines": [
            [spacement_array, step_array, 'b', 'Step Potential'],
            [spacement_array, max_step_vector, 'g', 'Max Step Potential']
        ],
        "labels": [
            'Step Potential (V)', 'Spacement (m)'
        ]
    }

    ground_potential_rise_data = {
        "title": "GPR Data",
        "lines": [
            [spacement_array, ground_potential_rise_array, 'b', 'Ground Potential Rise'],
            [spacement_array, max_touch_vector, 'g', 'Max Touch Potential']
        ],
        "labels": [
            'GPR (V)', 'Spacement (m)'
        ]
    }

    horizontal_conductors = (height / spacement) + 1
    vertical_conductors = (width / spacement) + 1
    total_length = horizontal_conductors * width + vertical_conductors * height

    data = [ground_potential_rise_data, touch_potential_data, step_potential_data]
    plt.figure()
    draw_graph(data)
    fig = plt.gcf()
    fig.set_size_inches(15, 30)
    dir_ = '/home/raphael/Projects/grounding/grid_designer'
    path = '/static/imgs/{}.png'.format(name)
    fig.savefig(dir_ + path, dpi=100, bbox_inches='tight')

    return success, path, conductor_diameter, total_length + rods_length, spacement, data, grid_resistance
