#Define character by stats

class Character ( ):
    def __init__ ( self ):
        #Symptom intensities
        self.nose       = 0
        self.headache   = 0
        self.nausea     = 0

        #Amount added to symptom every update
        # Idealy these slopes would be controled by separate quadratic
        # equations that would give each symptom a characteristic rhythm
        self.noseSlope  = 0.1
        self.headSlope  = 0.1
        self.nauseaSlope= 0.1

        #These define the symptom thresholds
        # These may become more complex than single numbers. We may use
        # several thresholds to simulate different stages of suffering.
        self.noseThresh = 1
        self.headThresh = 0.5
        self.nauseaTresh= 1
    

    def snease(self):
        print("Achoo!")#Game relivant code here


    def pound(self):
        print("Argh!")#Game relivant code here


    def vomit(self):
        print("Hurgle!")#Game relivant code here


    def update(self):
        self.nose = self.nose + self.noseSlope
        self.headache = self.headache + self.noseSlope
        self.nausea = self.nausea + self.nauseaSlope

        #These check the different symptom thresholds
        if(self.nose >= self.noseThresh):
            self.snease()

        if(self.headache >= self.headThresh):
            self.pound()

        if(self.nausea >= self.nauseaTresh):
            self.vomit()


#Test Main
if __name__ == '__main__':

    john = Character()

    while(john.nausea < 1):
        print("Nose: " + str(john.nose))
        print("Headache: " + str(john.headache))
        print("Nausea: " + str(john.nausea) + "\n")
        john.update()

    print("Oh, this terible cold...\n")
    john.noseSlope = john.noseSlope * -1
    john.headSlope = john.headSlope * -1
    john.nauseaSlope = john.nauseaSlope * -1

    while(john.nausea > 0.0):
        print("Nose: " + str(john.nose))
        print("Headache: " + str(john.headache))
        print("Nausea: " + str(john.nausea) + "\n")
        john.update()

    print("Ah, much better.")
