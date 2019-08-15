import datetime
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Row, Column, Fieldset, Div
from crispy_forms.bootstrap import FieldWithButtons,StrictButton





from .models import BOBAanvraag




class BOBAanvraagForm(forms.ModelForm):
    dvom_datumpv = forms.DateField(
        label='Datum PV',
        widget=DatePickerInput(format='%d/%m/%Y'),
        initial=datetime.date.today(),
        help_text='Datum van het PV',
        input_formats=settings.DATE_INPUT_FORMATS
    )

    dvom_verlengingingaandop = forms.DateField(
        label='Verlenging ingaand op',
        widget=DatePickerInput(format='%d/%m/%Y'),
        input_formats=settings.DATE_INPUT_FORMATS
    )
    dvom_verlengingeinddatum = forms.DateField(
        label='Verlenging einddatum',
        widget=DatePickerInput(format='%d/%m/%Y'),
        input_formats=settings.DATE_INPUT_FORMATS
    )
    dvom_vtmstartdatum = forms.DateField(
        label='VTMStartdatum / op',
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text='Startdatum vordering tot machtiging',
        input_formats=settings.DATE_INPUT_FORMATS
    )
    dvom_vtmeinddatum = forms.DateField(
        label='VTMEinddatum',
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text='Einddatum vordering tot machtiging',
        input_formats=settings.DATE_INPUT_FORMATS
    )

    dvom_machtigingop = forms.DateField(
        label='Machtiging op',
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text='Datum waarop de machtiging is afgegeven',
        input_formats=settings.DATE_INPUT_FORMATS,
        required=False
    )
    dvom_machtigingstartdatum = forms.DateField(
        label='Machtiging startdatum / op',
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text='Startdatum van de machtiging',
        input_formats=settings.DATE_INPUT_FORMATS,
        required=False
    )
    dvom_machtigingeinddatum = forms.DateField(
        label='Machtiging einddatum',
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text='Einddatum van de machtiging',
        input_formats=settings.DATE_INPUT_FORMATS,
        required=False
    )


    #dvom_heterdaad = forms.TypedChoiceField(
    #    coerce=lambda x: x == 'True',
    #    choices=((False, 'False'), (True, 'True')),
    #    widget=forms.RadioSelect
    #)
    class Meta:
        model = BOBAanvraag
        exclude = ('dvom_bobhandelingid', 'dvom_bobhandeling')
        help_texts = {
            'dvom_datumpv': 'Datum van het PV',
            'dvom_aanvraagpv': 'PV nummer van het aanvraag PV',
            'dvom_heeftverlenging': 'Is deze portal handeling verlengd',
            'dvom_verlenging': 'Betreft het een verlenging van een eerdere portal handeling',
        }
        widgets = {
            'dvom_heterdaad': forms.RadioSelect,
            'dvom_heeftverlenging': forms.RadioSelect,
            'dvom_verlenging': forms.RadioSelect,
        }

        error_messages = {
            "dvom_aanvraagpv": {
                "required": _("Dit veld is verplicht.")
            },
            "dvom_verbalisant": {
                "required": _("Dit veld is verplicht.")
            },
            "dvom_verbalisantcontactgegevens": {
                "required": _("Dit veld is verplicht.")
            },
            "dvom_strafvorderlijkebevoegdheidid": {
                "required": _("Dit veld is verplicht.")
            },

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = "."
        self.helper.attrs = {'novalidate': 'true'}

        self.helper.layout = Layout(
            Fieldset(
                'Algemeen',
                Row(
                    Div('dvom_aanvraagpv', css_class='col-md-6 mb-0 bob-data-required'),
                    Div('dvom_datumpv', css_class='col-md-6 mb-0 bob-data-required'),
                    css_class='form-row'
                ),
                Row(
                    Column('dvom_verbalisant', css_class='form-group col-md-6 mb-0'),
                    Column('dvom_verbalisantcontactgegevens', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('dvom_strafvorderlijkebevoegdheidid', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('dvom_verlenging', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('dvom_verlengingingaandop', css_class='form-group col-md-6 mb-0'),
                    Column('dvom_verlengingeinddatum', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('dvom_verlenging_aantal', css_class='form-group col-md-6 mb-0'),
                    Column('dvom_verlenging_periode', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Machtiging tot vordering',
                Row(
                    Column('dvom_vtmstartdatum', css_class='form-group col-md-6 mb-0'),
                    Column('dvom_vtmeinddatum', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('dvom_periode_aantal', css_class='form-group col-md-6 mb-0'),
                    Column('dvom_periode_periode', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
            ),

            Fieldset(
                'PDF Upload',
                Row(
                    Column('pdf_document', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
            ),

            Submit('submit', 'Opslaan &raquo;', id="id_btn_submit", css_class='btn-politie float-right btn-submit')
        )

    def clean(self):

        print('BOBAanvraagForm::clean()')

        cleaned_data = super().clean()
        dvom_aanvraagpv = cleaned_data.get('dvom_aanvraagpv')
        dvom_datumpv = cleaned_data.get('dvom_datumpv')
        dvom_bobhandeling = f"BOB_handeling_{dvom_aanvraagpv}_{dvom_datumpv}"
        cleaned_data['dvom_bobhandeling'] = dvom_bobhandeling
        print(f"dvom_bobhandeling: {dvom_bobhandeling}")

        return cleaned_data



class BOBAanvraagFilterFormHelper(FormHelper):
    form_method = 'GET'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    layout = Layout(
       'dvom_verbalisant',
        'dvom_verbalisantcontactgegevens',
        'dvom_aanvraagpv',
        Submit('submit', 'Zoeken', css_class='btn-politie btn-sm'),

    )

    #layout = Layout(
    #    FieldWithButtons('dvom_verbalisant', StrictButton('Go!')),
    #)


