from django.shortcuts import render
from django.conf import settings
from game.data_mgmt import Data_mgmt

def title_screen(request):
    context = {}
    dat = Data_mgmt()
    dat.load_default_settings()
    return render(request, "game/title_screen.html", context)

def worldmap(request):
    context = {"board_size": {
                "width": range(settings.BOARD_SIZE["width"]),
                "height": range(settings.BOARD_SIZE["height"])
              }}
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
    context = {}
    return render(request, "game/moviedex.html", context)

def moviedex_moviemon(request, moviemon_id):
    context = {"moviemon_id": moviemon_id}
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

