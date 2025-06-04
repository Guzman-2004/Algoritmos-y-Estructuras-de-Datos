class Jugador():
    def __init__(self, name, is_full = False, sportquestion= 0, historyquestion= 0, geographyquestion= 0, sciencequestion= 0, sport_cheese= False, history_cheese= False, geography_cheese= False, science_cheese= False):
        self.name = name
        self.is_full = is_full
        self.sportquestion = sportquestion
        self.historyquestion = historyquestion
        self.geographyquestion = geographyquestion
        self.sciencequestion = sciencequestion

        self.sport_cheese = sport_cheese
        self.history_cheese = history_cheese
        self.geography_cheese = geography_cheese
        self.science_cheese = science_cheese

    def __str__(self):
        str=(f"""
        El jugador {self.name} lleva:

        -------------------
        PREGUNTAS ACERTADAS
        -------------------

        -Correctas de historia: {self.historyquestion}
        -Correctas de deportes: {self.sportquestion}
        -Correctas de geografía: {self.geographyquestion}
        -Correctas de ciencias naturales: {self.sciencequestion}

        --------
        QUESITOS
        --------

        -Historia: {self.history_cheese}
        -Deportes: {self.sport_cheese}
        -Geografía: {self.geography_cheese}
        -Ciencias Naturales: {self.science_cheese}
        """)        
        return str
    
    def sumarpreg(self,tematica):
        if tematica == "Deportes":
            self.sportquestion += 1
        
        if tematica == "Historia":
            self.historyquestion += 1

        if tematica == "Ciencias Naturales":
            self.sciencequestion += 1

        if tematica == "Geografía":
            self.geographyquestion += 1

        if self.sportquestion == 3:
            self.sport_cheese = True

        if self.historyquestion == 3:
            self.history_cheese = True     

        if self.sciencequestion == 3:
            self.science_cheese = True

        if self.geographyquestion == 3:
            self.geography__cheese = True

        if (self.science_cheese == True) and (self.sport_cheese == True) and (self.geography__cheese == True) and (self.history_cheese == True):
            self.is_full = True


