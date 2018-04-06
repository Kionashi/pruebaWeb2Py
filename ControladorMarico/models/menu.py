response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Pagina1'),URL('default','pagina1')==URL(),URL('default','pagina1'),[]),
(T('Pagina2'),URL('default','pagina2')==URL(),URL('default','pagina2'),[]),
(T('Pagina3'),URL('default','pagina3')==URL(),URL('default','pagina3'),[]),
(T('Pagina4'),URL('default','pagina4')==URL(),URL('default','pagina4'),[]),
(T('Pagina5'),URL('default','pagina5')==URL(),URL('default','pagina5'),[]),
]