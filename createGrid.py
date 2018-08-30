import math
import json
from pprint import pprint


class Grid:
    def __init__(self, data_json):
        for data in data_json:
            setattr(self, data, data_json['{}'.format(data)])
            # self.data = data_json['{}'.format(data)]

    def show_data(self):
        return vars(self)

    def calc_max_values(self):
        max_current = 0.116/math.sqrt(self.TRIP_TIME)
        correction_factor = 1 - (0.09*(1-self.GROUND_RESISTIVITY/self.GRAVEL_RESISTIVITY
                                       )/(2*self.GRAVEL_DEPTH+0.09))

        max_touch_voltage = (1000+1.5*correction_factor*self.GROUND_RESISTIVITY)*max_current
        max_step_voltage = (6000+1.5*correction_factor*self.GROUND_RESISTIVITY)*max_current

        return max_touch_voltage, max_step_voltage

    def size_conductor(self):
        # Onderdonk Equation
        conductor_section = self.FAULT_CURRENT/(226.53*math.sqrt((1/self.TRIP_TIME)*math.log10(
            ((self.MAXIMUM_TEMPERATURE-self.ROOM_TEMPERATURE)/(234+self.ROOM_TEMPERATURE))+1
        )))
        return conductor_section

if __name__ == '__main__':
    with open("input_data.json") as file:
        input_data = json.load(file)
    grid1 = Grid(input_data)
    pprint(grid1.calc_max_values())
    print(grid1.size_conductor())
