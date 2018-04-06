# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

@auth.requires_login()
def pagina1():
    return dict()

@auth.requires_login()
def pagina2():
    return dict()

@auth.requires_login()
def pagina3():
    return dict()

@auth.requires_login()
def pagina4():
    return dict()

@auth.requires_login()
def pagina5():
    return dict()

def error():
    return dict()

