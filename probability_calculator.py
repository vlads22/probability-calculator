import random

class Hat:
    def __init__(self, red=0, orange=0, green=0, yellow=0, blue=0, black=0, pink=0, striped=0, test=0):
        self.contents = list()
        self.contents_addon = list()

        self.red = red
        self.green = green
        self.orange = orange
        self.yellow = yellow
        self.blue = blue
        self.black = black
        self.pink = pink
        self.striped = striped
        self.test = test
        
        self.contents_addon = ['red'] * int(red) 
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['orange'] * int(orange) 
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['green'] * int(green) 
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['yellow'] * int(yellow) 
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['blue'] * int(blue)
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['black'] * int(black) 
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['pink'] * int(pink) 
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['striped'] * int(striped) 
        self.contents.extend(self.contents_addon)
        self.contents_addon = ['test'] * int(test) 
        self.contents.extend(self.contents_addon)

        #print(self.contents)    # testing

    
    def draw(self, number__of_balls_to_extract):
        if number__of_balls_to_extract <= len(self.contents):
        
            balls_to_extract = list()
            self.number_of_balls_to_extract = number__of_balls_to_extract
            balls_to_extract= random.sample(self.contents, number__of_balls_to_extract)  # the random generated numbers must be each unique
                    # The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. 
            print(balls_to_extract)    # testing
            for x in balls_to_extract:
                self.contents.remove(x)
            print(self.contents)  #testing
        
            return(balls_to_extract)
        else:
            return(self.contents)

def experiment(hat=0, expected_balls=0, num_balls_drawn=0, num_experiments=0):
    list_of_balls = hat.contents
    how_many_times_M = 0
    num_experiments_done = 0
    
    while num_experiments_done < num_experiments:
        if num_balls_drawn > len(list_of_balls):
            balls_extracted = list_of_balls
        elif num_balls_drawn <= len(list_of_balls):
            balls_extracted = random.sample(list_of_balls, num_balls_drawn)  
        balls_extracted_dictionary = {"red":0, "orange":0, "green":0, "yellow":0, "blue":0, "black":0, "pink":0, "striped":0, "test":0}
    # we have to transform balls_extracted from list to dictionary
        # print(balls_extracted) OK
        for x in balls_extracted:
            if x in balls_extracted_dictionary:
                balls_extracted_dictionary[x] = balls_extracted_dictionary[x] + 1
        #print(balls_extracted_dictionary)  ok 
        #print(expected_balls)   ok
    # we have to compare expected balls with balls extracted dictionary, that is:
        #balls_extracted_dictionary = {"red":2, "orange":0, "green":1, "yellow":0, "blue":0, "black":2, "pink":0, "striped":0}
        #VS
        # expected_balls={"red":2,"green":1},
        number_of_matches = 0
        for x in expected_balls:    # you have to iterate through expected_balls, not balls_extracted_dictionary
            
            number_of_expected_balls = len(expected_balls)
            if expected_balls[x] <= balls_extracted_dictionary[x]:
                number_of_matches = number_of_matches + 1
            elif expected_balls[x] > balls_extracted_dictionary[x]:
                number_of_matches = number_of_matches
            if number_of_matches == number_of_expected_balls:  #every value in the balls_extracted must equal or higher to expected_balls
                how_many_times_M = how_many_times_M + 1
            #print(number_of_matches)# testin
        num_experiments_done = num_experiments_done + 1

    probability = how_many_times_M / num_experiments
    #ok print(how_many_times_M)  # testin
    #print(probability)   # testin
    
    return probability

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
