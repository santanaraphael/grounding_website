from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML

class ProjectGrid(forms.Form): 
    name = forms.CharField(initial='My first project using Grounding')
    fault_current = forms.FloatField(initial=6.814, help_text="Enter the fault current for the substation. (kA)")
    max_grid_current = forms.FloatField(initial=1908, help_text="Enter the max grid current. (A)")
    spacement = forms.FloatField(initial=20, help_text="Enter the initial spacement (m)") 
    if_ground_rods = forms.BooleanField(initial=False, help_text="Check this item if there are ground rods tucked on the soil.", required=False)
    conductor_kf = forms.FloatField(initial=7.06, help_text="Enter the conductor coefficient")
    rods_length = forms.FloatField(initial=0, help_text="Enter the total ground rods length (m)")
    rods_number = forms.IntegerField(initial=0, help_text="Enter the amout of ground rods") 
    increment_step = forms.FloatField(initial=0.5, help_text="Enter the increment step for the simulation (m)") 
    trip_time = forms.FloatField(initial=0.5, help_text="Enter the duration time for the fault (s)")
    grid_depth = forms.FloatField(initial=0.5, help_text="Enter on which depth will the grid be buried (m)")
    grid_height = forms.FloatField(initial=70, help_text="Grid height (m)")
    grid_width = forms.FloatField(initial=70, help_text="Grid width (m)")
    ground_resistivity = forms.FloatField(initial=400, help_text="Enter the ground resistivity for the region (omhs.m)")
    gravel_depth = forms.FloatField(initial=0.102, help_text="Enter the gravel layer depth (m)")
    gravel_resistivity = forms.FloatField(initial=2500, help_text="Enter the gravel layer resistivity (omhs.m)")
    room_temperature = forms.FloatField(initial=30, help_text="Enter the base temperature for the substation (Celsius)")
    maximum_temperature = forms.FloatField(initial=1084, help_text="Enter the maximum temperature for the conductor (Celsius)")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'dark'
        self.helper.layout = Layout(
            HTML('<p class="h2 text-center"> Design a grounding mesh </p><br><br>'),
            Div('name'),
            HTML('<p class="h3 text-center"> Electrical data </p>'),
            Column('conductor_kf', css_class='form-group col-md-3 mb-0'),
            Row(
                Column('fault_current', css_class='form-group col-md-4 mb-0'),
                Column('max_grid_current', css_class='form-group col-md-4 mb-0'),
                Column('trip_time', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML('<p class="h3 text-center"> Layout data </p>'),
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
            HTML('<p class="h3 text-center"> Resistivity data </p>'),
            Row(
                Column('ground_resistivity', css_class='form-group col-md-4 mb-0'),
                Column('gravel_depth', css_class='form-group col-md-4 mb-0'),
                Column('gravel_resistivity', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML('<p class="h3 text-center"> Temperature data </p>'),
            Row(
                Column('room_temperature', css_class='form-group col-md-6 mb-0'),
                Column('maximum_temperature', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Div(
            Submit('submit', 'Design'),
            css_class='text-center')
        )