from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def calc_ingredients(request, recipe):
    dict_new = {}
    servings = int(request.GET.get('servings', 1))
    if DATA.get(recipe):
        for key, val in DATA[recipe].items():
            dict_new[key] = val * servings
        context = {
            'recipe': dict_new,
            'servings': servings
        }
    else:
        context = {
            'recipe': None,
            'servings': servings
        }
    return render(request, 'calculator/index.html', context)
