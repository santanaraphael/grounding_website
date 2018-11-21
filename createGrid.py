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

    def size_conductor_legacy(self):
        # Onderdonk Equation
        conductor_section = self.FAULT_CURRENT/(226.53*math.sqrt((1/self.TRIP_TIME)*math.log10(
            ((self.MAXIMUM_TEMPERATURE-self.ROOM_TEMPERATURE)/(234+self.ROOM_TEMPERATURE))+1
        )))
        if conductor_section < 35:
            real_section = 35
        else:
            real_section = conductor_section

        diameter = (2*math.sqrt(real_section/math.pi))/1000 # Diameter should be returned in meters
        return diameter

    def size_conductor(self):

        conductor_section_kcmil = self.FAULT_CURRENT*self.KF*math.sqrt(self.TRIP_TIME)

        conductor_section_mm = conductor_section_kcmil/1.974

        diameter = (2*math.sqrt(conductor_section_mm/math.pi))/1000 # Diameter should be returned in meters
        return diameter

    def define_max_spacement(self):
        MAXIMUM_SPACEMENT = math.gcd(self.GRID_HEIGHT, self.GRID_WIDTH)
        return MAXIMUM_SPACEMENT

    def calc_potentials(self, spacement, diameter):
        horizontal_conductors = (self.GRID_HEIGHT/spacement)+1
        vertical_conductors = (self.GRID_WIDTH/spacement) + 1
        total_length = horizontal_conductors*self.GRID_WIDTH + vertical_conductors*self.GRID_HEIGHT

        # We should add the possibility of adding rods to the grounding grid, the total rod length should
        # then be counted on the total length
        grid_area = self.GRID_HEIGHT*self.GRID_WIDTH

        # Sverak Equation
        equivalent_resistance = self.GROUND_RESISTIVITY*(
            (1/total_length)+(1/math.sqrt(20*grid_area))*(
                1 + (1/(1+self.GRID_DEPTH*math.sqrt(20/grid_area)))
            )
        )
        eq_conductors = math.sqrt(horizontal_conductors*vertical_conductors)
        kii = 1/(math.pow(2*eq_conductors, (2/eq_conductors)))  # If there are rods, factor is 1
        kh = math.sqrt(1+self.GRID_DEPTH)
        ki = 0.656+0.172*eq_conductors
        km = (1/(2*math.pi))*math.log(
            (math.pow(spacement, 2)/16*diameter*self.GRID_DEPTH) + (math.pow(
                spacement + 2*self.GRID_DEPTH, 2)/8*spacement*diameter) - (self.GRID_DEPTH/(4*diameter)))+(
                kii/kh)*math.log(8/(math.pi*(2*eq_conductors-1)))
        return kii, kh, ki, km

if __name__ == '__main__':
    with open("input_data.json") as file:
        input_data = json.load(file)
    grid1 = Grid(input_data)
    print(grid1.calc_potentials(10, grid1.size_conductor()))

