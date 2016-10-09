from django.shortcuts import render

def title_screen(request):
    context = {}
    return render(request, "game/title_screen.html", context)

def worldmap(request):
    context = {}
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

