import sys
from time import sleep
import random
from colorama import init, Fore, Style
import os

# Inicializar colorama
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

chistes = {
    "¿Sabías que el 50% del aguacate es agua?": "El otro 50% está compuesto por nutrientes esenciales. Contiene una variedad de vitaminas como la K, E y varias del grupo B Además, es rico en minerales como el potasio y el magnesio también está lleno de ácidos grasos monoinsaturados y fibra dietética aunque No podemos olvidar los antioxidantes como la luteína y la zeaxantina. Na es coña, es cate",
    "¿Qué es rojo y malo para tus dientes?": "Un ladrillo",
    "¿Cuál es el nombre del pez que cae de un cuarto piso?": "Aaaaaaaaaaaaaaaaaahhhhhh... ¡tún!",
    "¿Cuáles eran los dibujos animados preferidos del capitán del Titanic?": "Timón y PUMBA.",
    "Una vez conté un chiste químico": "pero... no hubo reacción",
    "Un león se comió un jabón": "y ahora es puma",
    "¿Sabes por qué el mar es azul?": "Porque los peces dicen Blue, blue, blue blue",
    "¿De dónde sale la porcelana?": "De las porceovejas.",
    "Tengo un amigo otaku que estaba triste": "así que lo animé.",
    "¿Cómo se llama un bumerán que no vuelve?": "Palo.",
    "¿Qué hace una abeja en el gimnasio?": "Zum-ba.",
    "¿Qué le dice una iguana a su hermana gemela?": "Somos iguanitas.",
    "¿Por qué los pájaros no usan Facebook?": "Porque ya tienen Twitter.",
    "¿Qué hace una computadora en la playa?": "Busca un byte.",
    "¿Por qué los esqueletos no pelean entre ellos?": "Porque no tienen agallas.",
    "¿Qué hace una vaca en el espacio?": "¡Vaca-ciona!",
    "¿Cómo se despiden los químicos?": "Ácido un placer.",
    "¿Qué le dice una impresora a otra?": "¿Esa hoja es tuya o es una impresión mía?",
    "¿Por qué el libro de matemáticas está triste?": "Porque tiene demasiados problemas.",
    "¿Qué hace un pez mago?": "Nada por aquí, nada por allá.",
    "¿Cómo se llama un perro que sabe bailar?": "¡Un perro-gui!",
    "¿Qué hace un perro con un taladro?": "¡Taladrando!",
    "¿Qué hace una abeja en el bar?": "¡Pide una copa de miel!",
    "¿Qué hace un pez en el gimnasio?": "Nada sincronizada.",
    "¿Cómo se llama un perro que sabe matemáticas?": "¡Un perro-científico!",
    "¿Qué hace un pez en la computadora?": "Nada en la red.",
    "¿Por qué los esqueletos no van a fiestas?": "Porque no tienen cuerpo para bailar.",
    "¿Qué hace una vaca con un telescopio?": "¡Observa la Vía Láctea!",
    "¿Cómo se despiden los físicos?": "¡Hasta la vista, Newton!",
    "¿Qué le dice un semáforo a otro?": "No me mires, me estoy cambiando.",
    "¿Por qué el libro de historia está feliz?": "Porque tiene muchos cuentos.",
    "¿Qué hace un pez en la biblioteca?": "Nada entre libros.",
    "¿Cómo se llama un gato que sabe cantar?": "¡Un gato-lírico!",
    "¿Qué hace un perro con una calculadora?": "¡Suma ladridos!",
    "¿Qué hace una abeja en la escuela?": "Zum-ba clases.",
    "¿Qué hace una computadora en el desierto?": "Busca un oasis de datos.",
    "¿Por qué los esqueletos no juegan al fútbol?": "Porque no tienen piel para el balón.",
    "¿Qué hace una vaca en el laboratorio?": "¡Experimenta con leche!",
    "¿Cómo se despiden los biólogos?": "¡Hasta la próxima célula!",
    "¿Qué le dice un árbol a otro?": "¡Déjame en paz!",
    "¿Por qué el libro de ciencia está emocionado?": "Porque tiene muchas fórmulas.",
    "¿Qué hace un pez en el cine?": "Nada en la película.",
    "¿Cómo se llama un perro que sabe cocinar?": "¡Un chef-perro!",
    "¿Qué hace un perro con una linterna?": "¡Busca huesos en la oscuridad!",
}


def escribir_poco_a_poco(texto, color):
    for char in texto:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        sleep(0.05)  # Puedes ajustar el tiempo de espera para cambiar la velocidad
          
while True:
    print(                                 "                                                                                                        ")     
    print(Fore.LIGHTRED_EX + Style.BRIGHT +"              ▄▄▄█████▓ ▒█████   ██▀███  ▄▄▄█████▓ █    ██  ██▀███   ▄▄▄      ▓█████▄  ▒█████   ██▀███  ")
    print(Fore.RED + Style.BRIGHT         +"              ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒")
    print(Fore.RED + Style.NORMAL         +"              ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒")
    print(Fore.RED + Style.NORMAL         +"              ░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ")
    print(Fore.RED + Style.NORMAL         +"                ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░██▓ ▒██▒")
    print(Fore.RED + Style.NORMAL         +"                ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░")
    print(Fore.RED + Style.NORMAL         +"                  ░      ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░░▒░ ░ ░   ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░")
    print(Fore.BLACK + Style.BRIGHT       +"                ░      ░ ░ ░ ▒    ░░   ░   ░       ░░░ ░ ░   ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ")
    print(Fore.BLACK + Style.BRIGHT       +"                           ░ ░     ░                 ░        ░           ░  ░   ░        ░ ░     ░     ")
    print(Fore.BLACK + Style.NORMAL       +"                                                                               ░                        ")
    print(Fore.RED + Style.NORMAL         +"                                                                                                        ")            
    chiste_aleatorio = random.choice(list(chistes.keys()))
    escribir_poco_a_poco(chiste_aleatorio, Fore.LIGHTRED_EX + Style.BRIGHT)
    print()
    sleep(5)
    print(Fore.RED + Style.BRIGHT         +"                                                                                          ")   
    escribir_poco_a_poco(chistes[chiste_aleatorio], Fore.RED + Style.BRIGHT)
    print()
    sleep(3)
    clear()
