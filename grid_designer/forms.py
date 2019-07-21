from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML

class ProjectGrid(forms.Form): 
    name = forms.CharField(label='Project Name', initial='My first Grounding project')
    fault_current = forms.FloatField(label='Fault current (kA)', initial=6.814, help_text="Enter the projects fault current.")
    max_grid_current = forms.FloatField(label= 'Maximum grid current (A)', initial=1908, help_text='Enter the maximum current which will flow into the grid on faulty conditions.')
    spacement = forms.FloatField(label= 'Initial Spacement (m)', initial=20, help_text="Enter the initial spacement for the simulation.") 
    if_ground_rods = forms.BooleanField(label='Ground rods?', initial=False, help_text="Check this item if there are grounding rods stuck on the ground.", required=False)
    conductor_kf = forms.FloatField(label='Conductor KF', initial=7.06, help_text="Enter the conductor KF coefficient.")
    rods_length = forms.FloatField(label='Total rods length (m)', initial=0, help_text="Enter the total length of the rods stuck on the ground.")
    rods_number = forms.IntegerField(label='Amount of ground rods', initial=0, help_text="Enter the total amount of ground rods.") 
    increment_step = forms.FloatField(label='Increment step (m)', initial=0.5, help_text="Please enter the increment step for the simulation (a lower step means slower and more accurate results.).") 
    trip_time = forms.FloatField(label='Trip time (s)', initial=0.5, help_text="Enter the protection trip time for the project.")
    grid_depth = forms.FloatField(label='Grid depth (m)', initial=0.5, help_text="Enter the depth in which the grid will be buried in.")
    grid_height = forms.FloatField(label='Grid height (m)', initial=70, help_text="Enter the grid height.")
    grid_width = forms.FloatField(label='Grid width (m)', initial=70, help_text="Enter the grid width.")
    ground_resistivity = forms.FloatField(label='Ground resistivity (Ω-m)', initial=400, help_text="Enter the ground resistivity for the substation location.")
    gravel_depth = forms.FloatField(label='Gravel layer depth (m)', initial=0.102, help_text="Enter the depth of the layer of insulating material above the ground (commonly, gravel)")
    gravel_resistivity = forms.FloatField(label='Gravel resistivity (Ω-m)', initial=2500, help_text="Enter the resistivity of the insulating material.")
    room_temperature = forms.FloatField(label='Room temperature of the substation (°C)', initial=30, help_text="Enter the room temperature of the substation.")
    maximum_temperature = forms.FloatField(label='Maximum conductor temperature (°C)', initial=1084, help_text="Enter the maximum temperature supported by the chosen conductor.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'dark'
        self.helper.layout = Layout(
            HTML('<p class="h2 text-center"> Design a grounding mesh </p><br><br>'),
            Div('name'),
            HTML('<p class="h3 text-center"> Electrical Data </p>'),
            Column('conductor_kf', css_class='form-group col-md-3 mb-0'),
            Row(
                Column('fault_current', css_class='form-group col-md-4 mb-0'),
                Column('max_grid_current', css_class='form-group col-md-4 mb-0'),
                Column('trip_time', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML('<p class="h3 text-center"> Layout Data </p>'),
            Row(
                Column('grid_depth', css_class='form-group col-md-3 mb-0'),
                Column('grid_height', css_class='form-group col-md-3 mb-0'),
                Column('grid_width', css_class='form-group col-md-3 mb-0'),
                Column('spacement', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('if_ground_rods', css_class='form-group col-md-3 mb-0'),
                Column('rods_length', css_class='form-group col-md-3 mb-0'),
                Column('rods_number', css_class='form-group col-md-3 mb-0'),
                Column('increment_step', css_class='form-group col-md-3 mb-0'),
                
                css_class='form-row'
            ),
            HTML('<p class="h3 text-center"> Resistivity Data </p>'),
            Row(
                Column('ground_resistivity', css_class='form-group col-md-4 mb-0'),
                Column('gravel_depth', css_class='form-group col-md-4 mb-0'),
                Column('gravel_resistivity', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML('<p class="h3 text-center"> Temperature Data </p>'),
            Row(
                Column('room_temperature', css_class='form-group col-md-6 mb-0'),
                Column('maximum_temperature', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Div(
            Submit('submit', 'Design!'),
            css_class='text-center')
        )