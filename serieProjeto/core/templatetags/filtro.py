from django import template

register = template.Library()

@register.filter
def formatar_temporada(valor):
    if not valor:
        return ''
    elif valor == 1:
        return '1ª temporada'
    else:
        return f'{valor}ª temporada'
