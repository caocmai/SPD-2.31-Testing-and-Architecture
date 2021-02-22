# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def sodium_nitrate_in(ingredients):
    if "sodium nitrate" in ingredients:
        return True
    return False

def sodium_benzoate_in(ingredients):
    if "sodium benzoate" in ingredients:
        return True
    return False

def sodium_oxide_in(ingredients):
    if "sodium oxide" in ingredients:
        return True
    return False

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

ingredients = ['sodium benzoate']
if  sodium_benzoate_in(ingredients) or sodium_nitrate_in(ingredients) or sodium_oxide_in(ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()

