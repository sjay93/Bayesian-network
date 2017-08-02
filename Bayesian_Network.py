class Bayesian_Network:
    prob_array = {}
    prob_B = 0.001
    prob_notB = 1 - prob_B
    prob_E = 0.002
    prob_notE = 1 - prob_E
    prob_array['Mary_Calls_True'] = {'alarm_T':0.70,'alarm_F':0.01}
    prob_array['John_Calls_True'] = {'alarm_T':0.90,'alarm_F':0.05}
    prob_array['alarm_T'] = {'Bur_True_Ear_True':0.95,'Bur_True_Ear_False':0.94,'Bur_False_Ear_True':0.29,'Bur_False_Ear_False':0.001}


    def calculateProbability(self, B, E, A, J, M, conditions):
        prob_earthquake = prob_burglary = prob_alarm = prob_John_Calls = prob_Mary_Calls = 0.00

        if E:
            prob_earthquake = self.prob_E
        else:
            prob_earthquake = self.prob_notE

        if B:
            prob_burglary = self.prob_B
        else:
            prob_burglary = self.prob_notB

        if A:
            if J:
                prob_John_Calls = self.prob_array['John_Calls_True']['alarm_T']
            else:
                prob_John_Calls = 1 - self.prob_array['John_Calls_True']['alarm_T']
            if M:
                prob_Mary_Calls = self.prob_array['Mary_Calls_True']['alarm_T']
            else:
                prob_Mary_Calls = 1 - self.prob_array['Mary_Calls_True']['alarm_T']
        else:
            if J:
                prob_John_Calls = self.prob_array['John_Calls_True']['alarm_F']
            else:
                prob_John_Calls = 1 - self.prob_array['John_Calls_True']['alarm_F']
            if M:
                prob_Mary_Calls = self.prob_array['Mary_Calls_True']['alarm_F']
            else:
                prob_Mary_Calls = 1 - self.prob_array['Mary_Calls_True']['alarm_F']

        if B and E:
            if A:
                prob_alarm = self.prob_array['alarm_T']['Bur_True_Ear_True']
            else:
                prob_alarm = 1 - self.prob_array['alarm_T']['Bur_True_Ear_True']
        if (not B) and E:
            if A:
                prob_alarm = self.prob_array['alarm_T']['Bur_False_Ear_True']
            else:
                prob_alarm = 1 - self.prob_array['alarm_T']['Bur_False_Ear_True']
        if B and (not E):
            if A:
                prob_alarm = self.prob_array['alarm_T']['Bur_True_Ear_False']
            else:
                prob_alarm = 1 - self.prob_array['alarm_T']['Bur_True_Ear_False']
        if (not B) and (not E):
            if A:
                prob_alarm = self.prob_array['alarm_T']['Bur_False_Ear_False']
            else:
                prob_alarm = 1 - self.prob_array['alarm_T']['Bur_False_Ear_False']

        multiplier = 1.00
        for condition in conditions:
            if condition == 'B':
                multiplier*=prob_burglary
            if condition == 'E':
                multiplier*=prob_earthquake
            if condition == 'A':
                multiplier*=prob_alarm
            if condition == 'J':
                multiplier*=prob_John_Calls
            if condition == 'M':
                multiplier*=prob_Mary_Calls

        divisor = (prob_John_Calls*prob_Mary_Calls*prob_alarm*prob_burglary*prob_earthquake)
        return divisor/multiplier
