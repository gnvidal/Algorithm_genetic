import random

questions = {
    'question1': {
        'number': 1,
        'question': "¿Quién es considerado el padre de la ciencia ficción?",
        'alternatives': """
        A) Isaac Asimov
        B) Jules Verne
        C) H.G. Wells""",
        'correct': "B",
        'feedback': """Jules Verne es considerado uno de los padres de la ciencia ficción por sus novelas que combinan aventuras y ciencia, como "Viaje al centro de la Tierra" y "Veinte mil leguas de viaje submarino"."""
    },
    'question2': {
        'number': 2,
        'question': "¿Cuál de las siguientes obras es un ejemplo de ciencia ficción dura?",
        'alternatives': """
        A) "Dune" de Frank Herbert
        B) "2001: Una odisea del espacio" de Arthur C. Clarke
        C) "Fahrenheit 451" de Ray Bradbury""",
        'correct': "B",
        'feedback': """'2001: Una odisea del espacio' es un ejemplo de ciencia ficción dura porque se enfoca en la precisión científica y técnica."""
    },
    'question3': {
        'number': 3,
        'question': "¿Qué tema común se aborda en 'Un mundo feliz' de Aldous Huxley?",
        'alternatives': """
        A) Inteligencia artificial
        B) Ingeniería genética
        C) Colonización espacial""",
        'correct': "B",
        'feedback': """'Un mundo feliz' trata sobre una sociedad que utiliza la ingeniería genética para controlar la población y mantener la estabilidad social."""
    },
    'question4': {
        'number': 4,
        'question': "¿En qué novela aparece el concepto de 'Gran Hermano'?",
        'alternatives': """
        A) "1984"
        B) "Fahrenheit 451"
        C) "Brave New World""",
        'correct': "A",
        'feedback': """En '1984' de George Orwell, el Gran Hermano es el líder omnipresente y vigilante de un estado totalitario."""
    },
    'question5': {
        'number': 5,
        'question': "¿Quién es el autor de 'Frankenstein'?",
        'alternatives': """
        A) Mary Shelley
        B) H.G. Wells
        C) Jules Verne""",
        'correct': "A",
        'feedback': """Mary Shelley escribió 'Frankenstein', considerada una de las primeras obras de ciencia ficción."""
    },
    'question6': {
        'number': 6,
        'question': "¿Cuál es el enfoque principal del subgénero cyberpunk?",
        'alternatives': """
        A) Realidades virtuales y tecnologías avanzadas
        B) Robots y androides
        C) Mutaciones genéticas""",
        'correct': "A",
        'feedback': """El cyberpunk se centra en realidades virtuales, ciberespacios y la integración de la tecnología en la sociedad."""
    },
    'question7': {
        'number': 7,
        'question': "¿Qué novela popularizó el concepto de 'tres leyes de la robótica'?",
        'alternatives': """
        A) "Yo, Robot"
        B) "Dune"
        C) "2001: Una odisea del espacio""",
        'correct': "A",
        'feedback': """Isaac Asimov introdujo las tres leyes de la robótica en su colección de cuentos 'Yo, Robot'."""
    },
    'question8': {
        'number': 8,
        'question': "¿Cuál de estas series de televisión es un ejemplo clásico de ciencia ficción?",
        'alternatives': """
        A) "Star Trek"
        B) "Breaking Bad"
        C) "Game of Thrones""",
        'correct': "A",
        'feedback': """'Star Trek' es una serie de televisión icónica en el género de la ciencia ficción, que explora el espacio y el futuro de la humanidad."""
    },
    'question9': {
        'number': 9,
        'question': "¿Qué autor es conocido por su serie de novelas 'Fundación'?",
        'alternatives': """
        A) Isaac Asimov
        B) Robert Heinlein
        C) Arthur C. Clarke""",
        'correct': "A",
        'feedback': """Isaac Asimov es el autor de la serie 'Fundación', que trata sobre el declive y resurgimiento de un imperio galáctico."""
    },
    'question10': {
        'number': 10,
        'question': "¿En qué novela aparece el personaje 'Paul Atreides'?",
        'alternatives': """
        A) "Dune"
        B) "Neuromancer"
        C) "1984""",
        'correct': "A",
        'feedback': """Paul Atreides es el protagonista de 'Dune', una novela de Frank Herbert sobre intrigas políticas y ecología en un planeta desértico."""
    },
    'question11': {
        'number': 11,
        'question': "¿Cuál es el tema central de la novela 'El hombre en el castillo' de Philip K. Dick?",
        'alternatives': """
        A) Realidades alternativas
        B) Viaje en el tiempo
        C) Inteligencia artificial""",
        'correct': "A",
        'feedback': """'El hombre en el castillo' explora una realidad alternativa en la que los Aliados perdieron la Segunda Guerra Mundial."""
    },
    'question12': {
        'number': 12,
        'question': "¿Qué película de ciencia ficción está basada en una obra de Arthur C. Clarke?",
        'alternatives': """
        A) "2001: Una odisea del espacio"
        B) "Blade Runner"
        C) "Minority Report""",
        'correct': "A",
        'feedback': """'2001: Una odisea del espacio' es una película basada en la novela homónima de Arthur C. Clarke, dirigida por Stanley Kubrick."""
    },
    'question13': {
        'number': 13,
        'question': "¿Cuál de estos autores es conocido por escribir ciencia ficción blanda?",
        'alternatives': """
        A) Ursula K. Le Guin
        B) Kim Stanley Robinson
        C) Greg Egan""",
        'correct': "A",
        'feedback': """Ursula K. Le Guin es conocida por su enfoque en aspectos sociológicos y antropológicos, característicos de la ciencia ficción blanda."""
    },
    'question14': {
        'number': 14,
        'question': "¿Qué novela explora una sociedad distópica donde los libros están prohibidos?",
        'alternatives': """
        A) "Fahrenheit 451"
        B) "1984"
        C) "Brave New World""",
        'correct': "A",
        'feedback': """'Fahrenheit 451' de Ray Bradbury trata sobre una sociedad futura donde los bomberos queman libros para suprimir el conocimiento."""
    },
    'question15': {
        'number': 15,
        'question': "¿En qué novela se popularizó la idea de un 'anillo-mundo'?",
        'alternatives': """
        A) "Ringworld" de Larry Niven
        B) "Neuromancer" de William Gibson
        C) "Hyperion" de Dan Simmons""",
        'correct': "A",
        'feedback': """'Ringworld' de Larry Niven presenta un anillo artificial gigantesco que orbita una estrella."""
    },
    'question16': {
        'number': 16,
        'question': "¿Qué autor escribió 'Las estrellas, mi destino'?",
        'alternatives': """
        A) Alfred Bester
        B) Isaac Asimov
        C) Philip K. Dick""",
        'correct': "A",
        'feedback': """Alfred Bester es el autor de 'Las estrellas, mi destino', una novela sobre venganza y teletransportación."""
    },
    'question17': {
        'number': 17,
        'question': "¿Cuál es el nombre del superordenador en '2001: Una odisea del espacio'?",
        'alternatives': """
        A) HAL 9000
        B) GERTY
        C) Skynet""",
        'correct': "A",
        'feedback': """HAL 9000 es el superordenador de '2001: Una odisea del espacio', conocido por su inteligencia avanzada y comportamiento problemático."""
    },
    'question18': {
        'number': 18,
        'question': "¿En qué novela aparece el concepto de la 'nave generacional'?",
        'alternatives': """
        A) "Non-Stop" de Brian Aldiss
        B) "Rendezvous with Rama" de Arthur C. Clarke
        C) "Hyperion" de Dan Simmons""",
        'correct': "A",
        'feedback': """'Non-Stop' de Brian Aldiss trata sobre una nave espacial cuyos habitantes han olvidado su propósito original."""
    },
    'question19': {
        'number': 19,
        'question': "¿Qué tema aborda principalmente 'Solaris' de Stanisław Lem?",
        'alternatives': """
        A) Contacto con una forma de vida alienígena
        B) Exploración espacial
        C) Distopía futurista""",
        'correct': "A",
        'feedback': """'Solaris' se centra en el encuentro con una forma de vida alienígena en un planeta cubierto de un océano viviente."""
    },
    'question20': {
        'number': 20,
        'question': "¿Cuál de estos autores es conocido por su estilo literario poético y filosófico en la ciencia ficción?",
        'alternatives': """
        A) Ursula K. Le Guin
        B) H.G. Wells
        C) Philip K. Dick""",
        'correct': "A",
        'feedback': """Ursula K. Le Guin es conocida por su estilo literario poético y sus profundas exploraciones filosóficas en obras como 'La mano izquierda de la oscuridad'."""
    }
}

welcome="""
    \n
    =================================================
    BIENVENIDOS AL JUEGO DE TRIVIA DE CIENCIA FICCIÓN
    =================================================
    \n
    """
print(welcome)

players=[]
for i in range(2):
    player = input(f"\nIngrese el nombre del jugador número {i + 1}: ").strip().title()
    players.append(player)
    print(f"Hola {player}, tú eres el jugador número {i + 1}")

instructions= f"""
=================================================================

Instrucciones del juego:

1. Ingrese la cantidad de preguntas que desean responder por jugador. El máximo es de 20 preguntas por jugador.
2. El juego se desarrolla por turnos. La primera pregunta la responde {players[0]}, quien podrá observar las alternativas.
3. {players[0]}, seleccione la letra de su alternativa correcta.
4. Una vez ingresada la alternativa correcta de {players[0]}, si la respuesta es correcta, aparecerá un mensaje que dirá "Su respuesta es correcta" y sumará un punto.
5. Si la respuesta de {players[0]} es incorrecta, no sumará puntos y recibirá una retroalimentación de la pregunta. Después de la retroalimentación, es el turno de {player[1]}.
6. Ahora es el turno de {players[1]}, quien debe leer la pregunta y seleccionar su alternativa correcta.
7. {players[1]}, seleccione la letra de su alternativa correcta. Si la respuesta es correcta, sumará un punto. Si es incorrecta, recibirá una retroalimentación de la pregunta.
8. El juego continuará por turnos hasta completar la cantidad de preguntas seleccionadas por jugador.
9. Ganará el jugador que tenga mayor puntaje.
\n
"""
print(instructions)

number_of_questions=input("""\nIngrese la cantidad de preguntas por persona que quieren responder. Debe ingresar un numero entre 1 y 20: """)
try:
    number_of_questions=int(number_of_questions)
    if number_of_questions>20:
        number_of_questions = 20
        print(f"Cada jugador respondera {number_of_questions} preguntas.\n")
    elif number_of_questions<1:
        print("El número minimo de preguntas es 1. Se ajustará a 1 pregunta por jugador.")
        print("El número máximo de preguntas es 20. Se ajustará a 20 preguntas por jugador.")
        number_of_questions = 1
        print(f"Cada jugador respondera {number_of_questions} pregunta.\n")
    else: 
        print(f"La cantidad de preguntas que debe responder por jugador es de {number_of_questions} preguntas.")

except ValueError:
    number_of_questions =random.randint(1,20)
    print(f"""
        Debe ingresar un numero entre 1 a 20 preguntas por jugador.
        Se le seleccionara la cantidad de preguntas al azar. 
        La cantidad de preguntas que debe responder por jugador es de {number_of_questions} preguntas. \n""")

score_player1=0
score_player2=0
question_keys=list(questions.keys()) #ingresa en una lista las keys de cada pregunta
random.shuffle(question_keys) #Barajar las preguntas
#Asegurarse de tener suficientes pregutnas
if len(question_keys) < number_of_questions * 2:
    raise ValueError("No hay suficientes preguntas para el número de turnos.")


for i in range(number_of_questions):
    for j in range(2):
        print("\n================================================================\n")
        current_player=players[j]
        print(f"""\nEs el turno del jugador {current_player}""")
        # Seleccionar una pregunta para el jugador
        question_key = question_keys.pop(i)  
        # Obtiene y elimina una pregunta de la lista
        activity = questions[question_key]
        # Mostrar pregunta y alternativas
        activity_question=f"\nResponda la siguiente pregunta {activity['question']}\n"
        activity_alternative=f"\nSeleccione su alternativa correcta:\n {activity['alternatives']}"
        print(f"\t {activity_question}")
        print(f"\t {activity_alternative}")
        #Obtener respuesta del jugador
        option=str(input("Ingrese su respuesta, tenga cuidado porque si no se escribe una letra perdera su puntaje del turno. Escriba A, B o C: ")).upper()
        #Verificar respuesta del jugador
        if option==activity['correct']:
            print("\nSu respuesta es correcta. Ha sumado un punto.")
            if players[j]==players[0]:
                score_player1=score_player1+1
            elif players[j]==players[1]:
                score_player2=score_player2+1     
        elif option!=activity['correct']:
            print ("\nSu respuesta es incorrecta. No ha sumado puntaje")
            print (f"La respuesta correcta es {activity['correct']} porque {activity['feedback']}")
        # Mostrar puntajes actuales
        print(f"Puntaje actual de {players[0]}: {score_player1}")
        print(f"Puntaje actual de {players[1]}: {score_player2}")


#Determinar ganador
if score_player1>score_player2:
    print(f"El ganador es {score_player1}")
elif score_player1==score_player2:
    print("Ha habido un empate")
else: 
    print(f"El ganador es {score_player2}")

#Mostrar puntaje final
print(f"""
    El puntaje final es: 
    Jugador {players[0]} obtuviste {score_player1} puntos.
    Jugador {players[1]} obtuviste {score_player2} puntos.
    """)