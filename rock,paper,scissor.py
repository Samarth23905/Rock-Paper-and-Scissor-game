import random
rock  = '''
    -----------
 ---'     _ _ _)     
         (_ _ _ _)
         (_ _ _ __) 
         (_ _ _ _)
         (_ __)
 '''

paper ='''

     _ _ _ _ _ _
 ---'    _ _ _ _)_ _ _ _ 
            _ _ _ _ _ _ _)_ _ _
             _ _ _ _ _ _ _ _ __)
            _ _ _ _ _ _ _)
 -----,_ _ _ _ _ _ _)             
    
 '''

scissor = '''
     _ _ _ _ _
 ----'  _ _ _ _)_ _
          _ _ _ _ _)_ _
           _ _ _ _ _ _ )
           (_ _ _)
 - - -, _ _(_ _)

 '''
images = [rock, paper, scissor]
userChoice = int(input("Choose any one? 0, 1, 2: "))
print(images[userChoice])
compChoise = random.randint(0, 2)
print(images[compChoise])


