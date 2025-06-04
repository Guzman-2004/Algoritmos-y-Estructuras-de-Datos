import requests
import FUNCIONESPROYECTOFINAL as func
import OBJETOSPROYECTOFINAL as ob
import random
import time


func.Menu()
num_jug = func.Opcion()

geografia = {"results":[{"question":"Seoul is the capital of North Korea.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The flag of South Africa features 7 colours.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The surface area of Russia is slightly larger than that of the dwarf planet Pluto.","correct_answer":"True","incorrect_answers":["False"]},{"question":"There are no roads in\/out of Juneau, Alaska.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Israel is 7 hours ahead of New York.","correct_answer":"True","incorrect_answers":["False"]},{"question":"The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.","correct_answer":"True","incorrect_answers":["False"]},{"question":"The Southeast Asian island of Borneo is politically divided among 3 countries.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Vietnam is the only country in the world that starts with V. ","correct_answer":"False","incorrect_answers":["True"]},{"question":"Gothenburg is the capital of Sweden.","correct_answer":"False","incorrect_answers":["True"]},{"question":"There exists an island named &quot;Java&quot;.","correct_answer":"True","incorrect_answers":["False"]},{"question":"&quot;Mongolia&quot; was a part of the now non-existent U.S.S.R.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The Sonoran Desert is located in eastern Africa.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The capital of the US State Ohio is the city of Chillicothe.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Antarctica is the largest desert in the world.","correct_answer":"True","incorrect_answers":["False"]},{"question":"You could walk from Norway to North Korea while only passing through Russia.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Japan has left-hand side traffic.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Liechtenstein does not have an airport.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Norway has a larger land area than Sweden.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The title of the 1969 film &quot;Krakatoa, East_of Java&quot; is incorrect, as Krakatoa is in fact west of Java.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Is Tartu the capital of Estonia?","correct_answer":"False","incorrect_answers":["True"]}]}
cienciasnatu = {"results":[{"question":"Igneous rocks are formed by excessive heat and pressure.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Salt is 100% composed of Sodium.","correct_answer":"False","incorrect_answers":["True"]},{"question":"An atom contains a nucleus.","correct_answer":"True","incorrect_answers":["False"]},{"question":"An exothermic reaction is a chemical reaction that releases energy by radiating electricity.","correct_answer":"False","incorrect_answers":["True"]},{"question":"An Astronomical Unit is the distance between Earth and the Moon.","correct_answer":"False","incorrect_answers":["True"]},{"question":"An average human can go two weeks without water.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Psychology is the science of behavior and mind.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Water always boils at 100&deg;C, 212&deg;F, 373.15K, no matter where you are.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Not including false teeth; A human has two sets of teeth in their lifetime.","correct_answer":"True","incorrect_answers":["False"]},{"question":"A plant that has a life cycle for more than a year is known as an annual.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The Neanderthals were a direct ancestor of modern humans.","correct_answer":"False","incorrect_answers":["True"]},{"question":"A person can get sunburned on a cloudy day.","correct_answer":"True","incorrect_answers":["False"]},{"question":"The planet Mars has two moons orbiting it.","correct_answer":"True","incorrect_answers":["False"]},{"question":"A defibrillator is used to start up a heartbeat once a heart has stopped beating.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Shrimp can swim backwards.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Type 1 diabetes is a result of the liver working improperly.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Scientists accidentally killed the once known world&#039;s oldest living creature, a mollusc, known to be aged as 507 years old.","correct_answer":"True","incorrect_answers":["False"]},{"question":"In the periodic table, Potassium&#039;s symbol is the letter K.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Sugar contains fat.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The most frequent subconscious activity repeated by the human body is blinking.","correct_answer":"False","incorrect_answers":["True"]}]}
historia = {"results":[{"question":"The Tiananmen Square protests of 1989 were held in Hong Kong.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The United States Department of Homeland Security was formed in response to the September 11th attacks.","correct_answer":"True","incorrect_answers":["False"]},{"question":"The United States was a member of the League of Nations.","correct_answer":"False","incorrect_answers":["True"]},{"question":"United States President John F. Kennedy was assassinated during his presidential motorcade in Atlanta, Georgia on November 22nd, 1963.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Former United States Presidents John Adams and Thomas Jefferson died within hours of each other.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Adolf Hitler was a german soldier in World War I.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Adolf Hitler was tried at the Nuremberg trials.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The French Kingdom helped the United States gain their independence over Great Britain during the Revolutionary War.","correct_answer":"True","incorrect_answers":["False"]},{"question":"The United States of America was the first country to launch a man into space.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Thomas Crapper was a plumber who invented the flushing toilet.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The first televised presidential debate was between Jimmy Carter and Gerald Ford.","correct_answer":"False","incorrect_answers":["True"]},{"question":"Theodore Roosevelt Jr. was the only General involved in the initial assault on D-Day.","correct_answer":"True","incorrect_answers":["False"]},{"question":"Abraham Lincoln was the first U.S. President to be born outside the borders of the thirteen original states. ","correct_answer":"True","incorrect_answers":["False"]},{"question":"The Battle of Trafalgar was fought between the Spanish and British navies.","correct_answer":"True","incorrect_answers":["False"]},{"question":"The Spanish Civil War lasted from 1936 to 1939 and resulted in the establishment of a communist government.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The Catholic Monarchs, Isabella I of Castile and Ferdinand II of Aragon, were responsible for the forced conversion or expulsion of Jews and Muslims from Spain in 1492.","correct_answer":"False","incorrect_answers":["True"]},{"question":"The Basque terrorist group ETA was active in Spain from the 1950s until 2018.","correct_answer":"True","incorrect_answers":["False"]},{"question":"During the Spanish Civil War, the city of Madrid was never captured by Franco's forces. ","correct_answer":"True","incorrect_answers":["False"]},{"question":"The Reconquista was a centuries-long period of time in which the Christian kingdoms of Spain slowly reconquered and expelled the Moors from the Iberian Peninsula. ","correct_answer":"True","incorrect_answers":["False"]},{"question":"During the Spanish Civil War, General Franco was supported by the Soviet Union.","correct_answer":"False","incorrect_answers":["True"]}]}
deportes = {"results": [{"question": "Michael Jordan has won 6 NBA championships.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "Serena Williams has won 24 Grand Slam singles titles.", "correct_answer": "False", "incorrect_answers": ["True"]},{"question": "The New York Yankees have won 27 World Series championships.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "The Boston Celtics have won 17 NBA championships.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "The FIFA World Cup takes place every four years.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "The United States has won the most Olympic gold medals of any country.", "correct_answer": "False", "incorrect_answers": ["True"]},{"question": "Peyton Manning has won more than one Super Bowl MVP award.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "The Golden State Warriors hold the record for most regular season wins in an NBA season.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "Roger Federer has won 21 Grand Slam singles titles.", "correct_answer": "False", "incorrect_answers": ["True"]},{"question": "The Los Angeles Lakers have won more NBA championships than the Chicago Bulls.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "The 100-meter dash is a track and field event.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "LeBron James has never won an NBA Finals MVP award.", "correct_answer": "False", "incorrect_answers": ["True"]},{"question": "Usain Bolt holds the world record in the men's 400-meter dash.", "correct_answer": "False", "incorrect_answers": ["True"]},{"question": "The New England Patriots have won six Super Bowl championships.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "Kobe Bryant won five NBA championships with the Los Angeles Lakers.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "The Ryder Cup is a biennial golf competition between the United States and Europe.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "Tiger Woods has won 19 major championships.", "correct_answer": "False", "incorrect_answers": ["True"]},{"question": "The Dallas Cowboys have won eight Super Bowl championships.", "correct_answer": "False", "incorrect_answers": ["True"]},{"question": "The Tour de France is a cycling race.", "correct_answer": "True", "incorrect_answers": ["False"]},{"question": "Steph Curry has won three NBA championships with the Golden State Warriors.", "correct_answer": "True", "incorrect_answers": ["False"]}]}


geographyquestion = [q["question"] for q in geografia["results"]]
correctasgeografia = [q["correct_answer"] for q in geografia["results"]]

sciencequestion = [q["question"] for q in cienciasnatu["results"]]
correctascn = [q["correct_answer"] for q in cienciasnatu["results"]]

historyquestion = [q["question"] for q in historia["results"]]
correctashistoria = [q["correct_answer"] for q in historia["results"]]

sportsquestion = [q["question"] for q in deportes["results"]]
correctasdeportes = [q["correct_answer"] for q in deportes["results"]]


n = 0
jugadores = []

while n < num_jug:
    name = input("Nombre del jugador: ")

    if n == 0:
        jugador1 = ob.Jugador(name, 0,0,0,0,False,False,False,False)
        jugadores.append(jugador1)

    if n == 1:
        jugador2 = ob.Jugador(name, 0,0,0,0,False,False,False,False)
        jugadores.append(jugador2)

    if n == 2:
        jugador3 = ob.Jugador(name, 0,0,0,0,False,False,False,False)
        jugadores.append(jugador3)

    if n == 4:
        jugador4 = ob.Jugador(name, 0,0,0,0,False,False,False,False)
        jugadores.append(jugador4)
    n += 1



while (jugador1.is_full == False):
    for jug in jugadores:
        print(f"Es el turno de {jug.name}: ")
        print("Salio el: ")
        category = func.TirarDado()
        print(f"Le ha tocado la tematica {category}")

        if category == "Historia":
            n = random.randint(0,len(historyquestion)-1)
            print(f"Te ha tocado la pregunta: {historyquestion[n]}")
            answer = input("Es la repuesta True o False?: ")
            if answer == correctashistoria[n]:
                print("¡Respuesta correcta!")
                jug.sumarpreg(category)
                print(jug)
            else:
                print("Respuesta incorrecta")

        if category == "Geografía":
            n = random.randint(0,len(geographyquestion)-1)
            print(f"Te ha tocado la pregunta: {geographyquestion[n]}")
            answer = input("Es la repuesta True o False?: ")
            if answer == correctasgeografia[n]:
                print("¡Respuesta correcta!")
                jug.sumarpreg(category)
                print(jug)
            else:
                print("Respuesta incorrecta")

        if category == "Ciencias Naturales":
            n = random.randint(0,len(sciencequestion)-1)
            print(f"Te ha tocado la pregunta: {sciencequestion[n]}")
            answer = input("Es la repuesta True o False?:")
            if answer == correctascn[n]:
                print("¡Respuesta correcta!")
                jug.sumarpreg(category)
                print(jug)
            else:
                print("Respuesta incorrecta")

        if category == "Deportes":
            n = random.randint(0,len(sportsquestion)-1)
            print(f"Te ha tocado la pregunta: {sportsquestion[n]}")
            answer = input("Es la repuesta True o False?: ")
            if answer == correctasdeportes[n]:
                print("Respuesta correcta")
                jug.sumarpreg(category)
                print(jug)
            else:
                print("Respuesta incorrecta")

        time.sleep(6)

