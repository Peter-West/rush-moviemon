from django.shortcuts import render
from django.conf import settings
from game.data_mgmt import Data_mgmt

def title_screen(request):
    context = {"controls": {"a": {"action": "worldmap", "value": "default_settings"}, "b": {"action": "options/load_game", "value": "load"} } }
    dat = Data_mgmt()
    dat.load_default_settings()
    return render(request, "game/title_screen.html", context)

def worldmap(request):
    data_mgmt = Data_mgmt()
    data = data_mgmt.dump()
    board_size = { "width": range(settings.BOARD_SIZE["width"]), "height": range(settings.BOARD_SIZE["height"]) }
    if request.method == 'POST' and request._get_post()['clicked']:
        val = request._get_post()['val']
        if val == "down":
            data['position']['x'] = data['position']['x'] + 1
        Data_mgmt.load()
    def attack_link(part):
        return ""
    position = data["position"]
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
    datamg = Data_mgmt()
    # datamg.load_default_settings()
    data = datamg.dump()
    movies = data['Movies']
    print (type(movies))
    context = {"movies":movies}
    return render(request, "game/moviedex.html", context)

def moviedex_moviemon(request, moviemon_id):
    datamg = Data_mgmt()
    data = datamg.dump()
    movies = data['Movies']
    for elem in movies:
        if elem['imdbID'] == moviemon_id:
            movie = elem
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

