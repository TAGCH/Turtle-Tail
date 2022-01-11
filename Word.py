import csv
class word:
    def Question_list(self):
        Word_data = []
        with open('Word.csv') as f:
            rows = csv.DictReader(f)
            for r in rows:
                Word_data.append(r)
        List1 = []
        List2 = []
        List3 = []
        List4 = []
        List5 = []
        for a in Word_data:
            List1.append(a["SetA"])
        for b in Word_data:
            List2.append(b["SetB"])
        for c in Word_data:
            List3.append(c["SetC"])
        for d in Word_data:
            List4.append(d["SetD"])
        for e in Word_data:
            List5.append(e["SetE"])
        return List1, List2, List3, List4, List5
        

    