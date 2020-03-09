from pyramid.view import view_config

from cc_starter.templates.Test import A


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    x = A(5,6)
    print(x.b)
    print(x._a)
    x._getA()
    return {'project': 'cc_starter'}
