class Bulletin:
    def __init__(self, cc=0, tpe=0, tp=0, examen=0):
        self.cc = cc
        self.tpe = tpe
        self.tp = tp
        self.examen = examen

    def calculer_note_finale(self):
        has_cc = self.cc > 0
        has_tpe = self.tpe > 0
        has_tp = self.tp > 0

        if has_tp and has_tpe and has_cc:
            # TP 5%, TPE 5%, CC 20%, Examen 70%
            note = (self.tp * 0.05) + (self.tpe * 0.05) + (self.cc * 0.20) + (self.examen * 0.70)
        elif has_tpe and has_cc:
            # TPE 10%, CC 20%, Examen 70%
            note = (self.tpe * 0.10) + (self.cc * 0.20) + (self.examen * 0.70)
        elif has_cc:
            # CC 30%, Examen 70%
            note = (self.cc * 0.30) + (self.examen * 0.70)
        else:
            # Examen 100%
            note = self.examen
        
        return round(note, 2)

    def get_statut(self, note_finale):
        if note_finale >= 10:
            return "Validé"
        elif note_finale >= 8:
            return "Compensable"
        else:
            return "Échec"

    def get_mention(self, moyenne):
        if moyenne >= 16:
            return "Très Bien"
        elif moyenne >= 14:
            return "Bien"
        elif moyenne >= 12:
            return "Assez Bien"
        elif moyenne >= 10:
            return "Passable"
        else:
            return "Ajourné"