from django.forms.widgets import Select

class NobodyExpectsSelect(Select):

    class Media:
        css = {'all': (
            '/static/nobody-expects.css',)
        }
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js',
            '/static/nobody-expects.js',

        )

    def render(self, name, value, attrs=None, choices=()):
        html = super(NobodyExpectsSelect, self).render(name, value, attrs, choices)
        html += '<div id="nobody-expects"><img src="/static/nobody-expects.jpg" /></div>'
        return html