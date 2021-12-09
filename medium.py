# define the fuction
def hi(lang):      #parameter - lang <------ "ro"
    # function body
    if lang == "en":
        print("Hello!!!")
    elif lang == "ro":
        print("Salut!!!")
    elif lang == "ru":
        print("Привет!!!")
    else:
        print("This language does not exist!!! ")
# HW 1: upgrade the logic of "bye (lang)"
#      * lang - doenst exit -> "Hello !!!"
def bye(lang):
    if lang == "en":
        print("Good bye!!!")
    elif lang == "ro":
        print("La revedere!!!")
    elif lang == "ru":
        print("Пока!!!")
    else:
        print("This language does not exist!!! ")
# call the fuction
hi("en")
hi("ro")
hi("ru")
hi("fr")
bye("en")
bye("ro")
bye("ru")
bye("fr")