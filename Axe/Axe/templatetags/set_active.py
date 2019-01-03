from django import template

register = template.Library()

@register.simple_tag
def active(param1,param2,param3):
    print("param1:",param1)
    print("param2:", param2)
    if(param1 == param2):
        return "class=""active"""
    else:
        return ""


# {% active "1" "2" "3" %}