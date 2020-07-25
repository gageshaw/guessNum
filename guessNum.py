import random as r
class numGame:
    
    def generateRandNum(self):
        self.randNum = int(r.random() *100) % 20
        
    
    def play(self):
        self.generateRandNum()
        guess = 21
        
        print("Guess The Number (0-20): ")
        
        while(guess != self.randNum):
            
            guess = int(input())
            
            if (guess == self.randNum):
                print("Your Guess Was Correct, You Won!!")
            
            elif (guess < self.randNum):
                print("Your Guess Was Too Low, Guess Again (0-20): ")
                
            else:
                print("Your Guess Was Too High, Guess Again (0-20): ")
        
        
new = numGame()
new.play()
