menu = [
    {'title': 'Главная', 'path': '/'},
    {'title': 'Добавить статью', 'path': '/add-post'},
    {'title': 'Войти', 'path': '/login'},
]

category_list = [
    {'title': 'Люди', 'path': 'man'},
    {'title': 'Электроника', 'path': 'el'},
    {'title': 'Книги', 'path': 'book'}
]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        else:
            user_menu.pop(2)

        context['navs'] = user_menu
        context['cats'] = category_list
        return context
