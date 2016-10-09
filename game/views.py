from django.shortcuts import render
from django.conf import settings
from game.data_mgmt import Data_mgmt

def title_screen(request):
    context = {"controls": {"a": {"action": "worldmap", "value": "default_settings"}, "b": {"action": "options/load_game", "value": "load"} } }
    dat = Data_mgmt()
    dat.load_default_settings()
    return render(request, "game/title_screen.html", context)

def worldmap(request):
    #data = Data_mgmt().load_default_settings()
    data = {"position": {"x": 9, "y": 9}}
    def attack_link(part):
        return ""
    position = data["position"]
    board_size = { "width": range(settings.BOARD_SIZE["width"]), "height": range(settings.BOARD_SIZE["height"]) }
    if position["x"] != 0:
        left = {"action": "worldmap", "value": "left"}
    else:
        left = {"action": "", "value": ""}
    if position["y"] != 0:
        up = {"action": "worldmap", "value": "up"}
    else:
        up = {"action": "", "value": ""}
    if position["x"] != int(settings.BOARD_SIZE["height"]) - 1:
        right = {"action": "worldmap", "value": "right"}
    else:
        right = {"action": "", "value": ""}
    if position["y"] != int(settings.BOARD_SIZE["height"]) - 1:
        down = {"action": "worldmap", "value": "down"}
    else:
        down = {"action": "", "value": ""}
    controls = {
            "left": left,
            "up": up,
            "right": right,
            "down": down,
            "a": {"action": attack_link("action"), "value": attack_link("moviemon_id")},
            "start": {"action": "options", "value": "options"},
            "select": {"action": "moviedex", "value": "moviedex"},
            }
    context = { "board_size": board_size, "controls": controls, "position": position }
    return render(request, "game/worldmap.html", context)

def battle(request):
    context = {}
    return render(request, "game/battle.html", context)

def battle_moviemon(request, moviemon_id):
    dat = Data_mgmt()
    dump = dat.dump()
    mov = {}
    balls = dump["nbr_balls"]
    sgt = dat.get_strength()
    for item in dump['Movies']:
        if item['imdbID'] == moviemon_id:
            mov = item
    taux = 50 - (int(mov['imdbRating'][0:1]) * 10) + (sgt * 5)
    context = {"moviemon": mov, "nbr_balls" : balls, "strength" : sgt, "taux" : taux}
    return render(request, "game/battle_moviemon.html", context)

def moviedex(request):
    count = 1
    def increment(count):
        count += 1
        return count
    def decrement(count):
        count -= 1
        return count
    datamg = Data_mgmt()
    # datamg.load_default_settings()
    data = datamg.dump()
    movies = data['Movies']
    print (type(movies))
    controls = {
            "left": {"action": "moviedex", "value": decrement(count)},
            "right": {"action": "moviedex", "value": increment(count)},
            "a": {"action": "moviedex_moviemon", "value": "detail"},
            "select": {"action": "worldmap", "value": "back"},
            }
    context = {"movies":movies, "controls":controls, "count":count}
    return render(request, "game/moviedex.html", context)

def moviedex_moviemon(request, moviemon_id):
    datamg = Data_mgmt()
    data = datamg.dump()
    movies = data['Movies']
    for elem in movies:
        if elem['imdbID'] == moviemon_id:
            movie = elem
    controls = {
            "b": {"action": "moviedex", "value": "back"},
            }
    context = {"movie": movie}
    return render(request, "game/moviedex_moviemon.html", context)

def options(request):
    context = {}
    return render(request, "game/options.html", context)

def options_save_game(request):
    context = {}
    return render(request, "game/options_save_game.html", context)

def options_load_game(request):
    context = {}
    return render(request, "game/options_load_game.html", context)

