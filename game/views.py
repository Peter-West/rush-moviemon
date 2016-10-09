from django.shortcuts import render
from django.conf import settings
from game.data_mgmt import Data_mgmt

def title_screen(request):
    context = {"controls": {"a": {"action": "worldmap", "value": "default_settings"}, "b": {"action": "options/load_game", "value": "load"} } }
    dat = Data_mgmt()
    # dat.load_default_settings()
    # print (dat.get_random_movie()['Title'])
    # dump = dat.dump()
    # print (dump['Movies'])
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
    context = {"moviemon_id": moviemon_id}
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

