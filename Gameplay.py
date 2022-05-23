from cgitb import text


print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
text="Tim Is Greate!" 
print(text.lower())

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)") 
score=0


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
   
else:
    print("Incorrect!")


answer = input("What are programming languages? ")
if answer.lower() == "python, kotlin, javascrip and ruby":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Python is backend or frontend language? ")
if answer.lower() == "backend":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Are Kotlin used for Mobile development? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 


answer = input("What does Hypertext makeup language? ")
if answer.lower() == "html":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/5 )* 100) + "%")

        