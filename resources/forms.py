import datetime
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Row, Column, Fieldset, Div, Field, Button, MultiField
from crispy_forms.bootstrap import FieldWithButtons,StrictButton, AppendedText, PrependedText, PrependedAppendedText
from crispy_forms.bootstrap import InlineRadios

from betterforms.forms import BetterForm, BetterModelForm
from betterforms.multiform import MultiModelForm

from .models import BOBAanvraag, PvVerdenking, Verbalisant, RechtsPersoon, NatuurlijkPersoon
from .custom_layout_object import VerbalisantFormSection


class BOBAanvraagForm(forms.ModelForm):
    mondeling_aanvraag_datum = forms.DateField(
        label='Datum mondelinge aanvraag',
        widget=DatePickerInput(format='%d/%m/%Y'),
        initial=datetime.date.today(),
        help_text='Datum v/d mondelinge vordering',
        input_formats=settings.DATE_INPUT_FORMATS
    )

    class Meta:
        model = BOBAanvraag
        exclude = ('unique_id', 'created_by', 'updated_by', 'status', 'created_at', 'updated_at')
        help_texts = {
            'dvom_aanvraagpv': 'PV nummer van het aanvraag PV',
            'mondeling_aanvraag_bevestiging': 'Betreft het een bevestiging van een mondelinge aanvraag',
        }
        widgets = {
            'mondeling_aanvraag_bevestiging': forms.RadioSelect,
            'bijlage_toevoegen': forms.RadioSelect,
            'onderzoeksbelang_toelichting': forms.Textarea(attrs={'rows':3})
        }

        error_messages = {
            "pv_nummer": {
                "required": _("Dit veld is verplicht.")
            },
            "verbalisant": {
                "required": _("Dit veld is verplicht.")
            },
            "verbalisant_email": {
                "required": _("Dit veld is verplicht.")
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = "."
        self.helper.form_id = 'aanvraagFormId'
        self.helper.attrs = {'novalidate': 'true'}

        self.helper.layout = Layout(
            Fieldset(
                'Algemeen',
                Row(
                    #Column('mondeling_aanvraag_bevestiging', css_class='bobaanvraag-mondeling-check col-md-6 mb-0'),
                    Div(InlineRadios('mondeling_aanvraag_bevestiging'), css_class='bobaanvraag-mondeling-check col-md-6 mb-0'),
                    Field('mondeling_aanvraag_datum', css_class='bobaanvraag-mondeling-datum',
                          wrapper_class='col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Field('naam_ovj', id="id_naam_ovj", css_class='bob-data-required', wrapper_class="col-sm-4 pl-0"),
                Row(
                    Field('parket_nummer', css_class='bob-data-required', wrapper_class='col-md-6 mb-0'),
                    Field('rc_nummer', css_class='bob-data-required', wrapper_class='col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Field('naam_onderzoek', wrapper_class='col-md-6 mb-0', css_class='bob-data-required'),
                    Field('onderzoeksbelang_toelichting', wrapper_class='col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Field('verstrekking_gegevens_aan', wrapper_class='col-md-3 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Field('verbalisant', wrapper_class='col-md-6 mb-0'),
                    Field('verbalisant_email', wrapper_class='col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Field('bijlage_toevoegen', wrapper_class='col-md-6 mb-0'),
                    Field('bijlage', wrapper_class='col-md-6 mb-0'),
                    css_class='form-row'
                ),
            ),
            Submit('btn_submit_id', 'Opslaan &raquo;', id="id_btn_submit", css_class='btn-politie float-right btn-submit')
        )

    def clean(self):

        print('BOBAanvraagForm::clean()')

        cleaned_data = super().clean()

        return cleaned_data



class BOBAanvraagFilterFormHelper(FormHelper):
    form_method = 'GET'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    layout = Layout(
       'verbalisant',
        'verbalisant_email',
        'pv_nummer',
        Submit('submit', 'Zoeken', css_class='btn-politie btn-sm'),

    )

    #layout = Layout(
    #    FieldWithButtons('dvom_verbalisant', StrictButton('Go!')),
    #)


class BOBAanvraagStatusForm(forms.Form):
    next_status = forms.ChoiceField(label="Ik wil deze aanvraag: ", widget=forms.Select(), choices=[], required=True)
    class Meta:
        fields = ('next_status',)

    def __init__(self, *args, **kwargs):
        available_transitions = kwargs.pop('available_transitions')
        super().__init__(*args, **kwargs)
        self.fields['next_status'].choices = available_transitions
        self.helper = FormHelper()
        self.helper.form_class = 'inline-form'
        self.helper.form_action = "."
        self.helper.form_id = 'aanvraagStatusFormId'
        self.helper.attrs = {'novalidate': 'true'}
        self.helper.layout = Layout(
            Row(
                Column('next_status', css_class="col-sm-4"),
                Column(Submit('btn_submit_id', 'Verzenden &raquo;', id="id_btn_submit",
               css_class='btn-politie  btn-submit ')),
                css_class="row-form d-flex justify-content-end align-items-end"
            )
        )

################################
# Form: PV Verdenking
################################

# VerbalisantLayout
class VerbalisantLayout(Layout):
    def __init__(self, *args, **kwargs):
        super(VerbalisantLayout, self).__init__(
            Field('verbalisanten', template='resources/verbalisanten.html'),
        )


# PersoonLayout
class PersoonLayout(Layout):
    def __init__(self, *args, **kwargs):
        super(PersoonLayout, self).__init__(
            Field('rechtspersoon', template='resources/persoon_form.html'),
            Field('natuurlijkpersoon', template='resources/persoon_form.html'),
        )

# PvVerdenkingLayout
class PvVerdenkingLayout(Layout):
    def __init__(self, *args, **kwargs):
        super(PvVerdenkingLayout,self).__init__(
            Fieldset('PV verdenking',
                Row(
                    Field('pv_nummer', wrapper_class='col-sm-6'),
                    Field('bvh_nummer', wrapper_class='col-sm-6'),
                    Field('naam_ovj', wrapper_class='col-sm-6'),
                    Field('parket_nummer', wrapper_class='col-sm-6'),
                    Field('rc_nummer', wrapper_class='col-sm-6'),
                    css_class='form-row'
                ),
                css_class='border p-3 shadow-sm'
            )
        )

class PvVerdenkingForm(forms.ModelForm):
    class Meta:
        model = PvVerdenking
        exclude = ()
        #fields = ('pv_nummer', 'bvh_nummer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'inline-form'
        self.helper.form_action = "."
        self.helper.form_method = "post"
        self.helper.form_id = 'pvVerdenkingFormId'
        self.helper.attrs = {'novalidate': 'true'}
        self.helper.layout = Layout(

            PvVerdenkingLayout(),
            VerbalisantLayout(),
            PersoonLayout(),
            Div(
                Submit('btn_submit_id', 'Volgende &raquo;', css_class='btn-politie float-right btn-submit'),
                css_class='d-flex justify-content-end p-2'
            ),

        )

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['naam'] = 'test naam'



class VerbalisantForm(forms.ModelForm):
    class Meta:
        model = Verbalisant
        fields = ('naam', 'rang', 'email') # '__all__'
        #fieldsets = (
        #    Fieldset('Verbalisanten', fields=('naam', 'rang', 'email'), legend='Verbalisanten'),
        #)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
        )


class RechtsPersoonForm(forms.ModelForm):
    class Meta:
        model = RechtsPersoon
        fields = '__all__'


class NatuurlijkPersoonForm(forms.ModelForm):
    class Meta:
        model = NatuurlijkPersoon
        fields = '__all__'




class PvMultiForm(MultiModelForm):
    form_classes = {
        'verdenking': PvVerdenkingForm,
        'verbalisant': VerbalisantForm,
    }
