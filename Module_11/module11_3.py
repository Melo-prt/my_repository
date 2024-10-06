import inspect


def introspection_info(obj):
    obj_info = {'Тип объекта:': type(obj), 'Атрибуты объекта': [attr for attr in dir(obj)],
                'Методы объекта': [method for method in dir(obj)],
                'Модуль, к которому объект принадлежит': inspect.getmodule(obj)}
    return obj_info


number_info = introspection_info(42)
print(number_info)
