from django.http import HttpResponse

def recipe_list(request):
    return HttpResponse("""
        <h1>Recipe Book</h1>
        <ul>
            <li><a href='/recipe/1'>Recipe 1</a></li>
            <li><a href='/recipe/2'>Recipe 2</a></li>
        </ul>
    """)

def recipe_1(request):
    return HttpResponse("""
        <h1>Recipe 1</h1>
        <ul>
            <li>Tomato - 3pcs</li>
            <li>Onion - 1pc</li>
            <li>Pork - 1kg</li>
            <li>Water - 1L</li>
            <li>Sinigang mix - 1 packet</li>
        </ul>
        <a href='/recipes/list'>Back to list</a>
    """)

def recipe_2(request):
    return HttpResponse("""
        <h1>Recipe 2</h1>
        <ul>
            <li>Garlic - 1 head</li>
            <li>Onion - 1pc</li>
            <li>Vinegar - 1/2 cup</li>
            <li>Water - 1 cup</li>
            <li>Salt - 1 tablespoon</li>
            <li>Whole black peppers - 1 tablespoon</li>
            <li>Pork - 1 kilo</li>
        </ul>
        <a href='/recipes/list'>Back to list</a>
    """)
