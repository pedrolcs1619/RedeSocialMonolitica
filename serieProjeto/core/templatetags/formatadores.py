from django import template

register = template.Library()

@register.filter
def formatar_temporada(valor):
    return f"{valor}ª temporada" if valor else "Sem temporada"
