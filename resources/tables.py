from django_tables2 import tables, TemplateColumn

from .models import BOBAanvraag

class BOBAanvraagTable(tables.Table):
    class Meta:
        model = BOBAanvraag
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('id', 'dvom_aanvraagpv', 'dvom_datumpv', 'dvom_verbalisant', 'dvom_verbalisantcontactgegevens',
                  'pdf_document', 'edit', 'view','delete')


        attrs = {
            'th': {
                '_ordering': {
                    'orderable': 'sortable',
                    'ascending': 'ascend',
                    'descending': 'descend'
                },
                'class': 'p-2'
            },
            'td': {
                'class': 'p-2'
            },
            'class': 'table-bordered'
        }

    edit = TemplateColumn(template_name='resources/bobaanvraag_update_column.html')
    view = TemplateColumn(template_name='resources/bobaanvraag_view_column.html')
    delete = TemplateColumn(template_name='resources/bobaanvraag_delete_column.html')