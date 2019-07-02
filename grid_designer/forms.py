from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML

class ProjectGrid(forms.Form): 
    name = forms.CharField(initial='My first project using Grounding')
    fault_current = forms.FloatField(initial=1200, help_text="Enter the fault current for the substation.")
    max_grid_current = forms.FloatField(initial=100)
    spacement = forms.FloatField(initial=8) 
    if_ground_rods = forms.BooleanField(initial=False, help_text="Check this item if there are ground rods tucked on the soil.", required=False)
    conductor_kf = forms.FloatField(initial=7.06)
    rods_length = forms.FloatField(initial=20)
    rods_number = forms.IntegerField(initial=20) 
    increment_step = forms.FloatField(initial=0.5) 
    trip_time = forms.FloatField(initial=0.6)
    grid_depth = forms.FloatField(initial=0.6)
    grid_height = forms.FloatField(initial=40)
    grid_width = forms.FloatField(initial=50)
    ground_resistivity = forms.FloatField(initial=411.8)
    gravel_depth = forms.FloatField(initial=0.2)
    gravel_resistivity = forms.FloatField(initial=2500)
    room_temperature = forms.FloatField(initial=30)
    maximum_temperature = forms.FloatField(initial=450)

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