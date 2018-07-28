my_heart = 0
my_desire = 1
my_thirst = 2
def liftin_high(the_spirit, greatness):
    Davy = 0
    Gina = 1
    while Davy != greatness:
        Gina = the_spirit * Gina
        Davy += 1
    return Gina
def show_me_the_way(my_love):
    Existence = 0
    if my_love < my_thirst:
        return Existence
    while liftin_high(my_thirst,Existence) < my_love + my_desire:
        Existence += 1
    Existence -= 1
    return Existence
def truth_of_the_now(my_time, your_place):
    if your_place < my_heart:
        return my_heart
    while my_time > my_heart:
        Truth = 0
        Truth = show_me_the_way(my_time)
        if your_place > Truth:
            return my_heart
        if your_place == Truth:
            return True
        my_time = my_time - liftin_high(my_thirst,Truth)
    return my_heart
def truth_of_the_world(the_soul, the_singer):
    the_song = ""
    the_stage = the_singer - my_desire
    while the_stage > my_heart - my_desire:
        if truth_of_the_now(the_soul,the_stage):
            the_song = the_song + "*"
        if truth_of_the_now(the_soul, the_stage) != True:
            the_song = the_song + "_"
        the_stage -= 1
    print(the_song)
def livin_life(my_cool, my_calm, my_need, my_breath):
    a_moment = my_cool + 2 * my_calm + 4 * my_need
    if truth_of_the_now(my_breath, a_moment):
        return my_desire
    return my_heart
def livin_large(my_time, my_money, the_way):
    Life = 0
    while my_money != my_heart - my_desire:
        my_money -= 1
        my_cool = truth_of_the_now(my_time, my_money)
        my_money += 1
        my_calm = truth_of_the_now(my_time, my_money)
        my_money += 1
        my_need = truth_of_the_now(my_time, my_money)
        my_money -= 1
        your_life = livin_life(my_cool, my_calm, my_need, the_way)
        Life = Life + your_life * liftin_high(my_thirst, my_money)
        my_money -= 1
    return Life
def rock_remembrance(a_man, a_lifetime):
    the_beat = 2 * a_lifetime + 1
    a_story = liftin_high(2,a_lifetime)
    while a_lifetime != False:
        truth_of_the_world(a_story,the_beat)
        a_story = livin_large(a_story,the_beat,a_man)
        a_lifetime -= 1
Scottie = 165
Life = 24
rock_remembrance(Scottie, Life)
