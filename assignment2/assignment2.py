#What is the mean, median, and range, for attack, defense, and speed?


with open("pokemon_data.csv", "r") as file: #opening the file in read mode
    contents = file.read() #reading the contents of the file
    lines = contents.splitlines() #splitting the contents by lines
    columns = [line.split(",") for line in lines] #splitting the lines by commas and saving them to a list of columns

#need to find where attack, defense, speed are 
header = columns[0]

#finds the index in the header where it says attack and saves that position to the attackIndex
attackIndex = header.index("attack") #index is 12 for attack 

#finds the index in the header where it says defense and saves that position to the defenseIndex
defenseIndex = header.index("defense") #index is 13 for defense

#finds the index in the header where it says speed and saves that position to the speedIndex
speedIndex = header.index("speed") # index is 16 for speed

#grabs the columns I need using the indexes above and excludes the header . 
attack = [int(row[attackIndex]) for row in columns[1:]]
defense = [int(row[defenseIndex]) for row in columns[1:]]
speed = [int(row[speedIndex]) for row in columns[1:]]

#built in function with base python to sort in ascending order(least to greatest) without having to make a new variable. 
# Sorted() makes a new variable to hold the new list it makes from sorting.
attack.sort()
defense.sort()
speed.sort()

#mean for attack, defense, and speed
attackMean = round(sum(attack)/len(attack), 2) #sum of attack divided by the length of attack, and i rounded it to 2 decimal places
defenseMean = round(sum(defense)/len(defense) ,2) #sum of defense divided by the length of defense, and i rounded it to 2 decimal places
speedMean = round(sum(speed)/len(speed), 2) #sum of speed divided by the length of speed, and i rounded it to 2 decimal places
means = [attackMean, defenseMean, speedMean] #holds the means in a list
print("Means for attack, defense, and speed: ", means) #prints the list


#median for attack, defense, and speed time!
#made easier by the .sort() done above
if len(attack)%2 == 0 : #conditional if the column has an even number of instances
    attackMedian = (attack[len(attack) // 2 - 1 ] + attack[len(attack) // 2]) / 2
    #attack[] is just getting the index
    #the math inside the [] does the floor division to get the first place then subtracts 1 to get the position before
    #the second part of the math does the same by finding the middle but does not need to be subtraced since we found the position before
    #The attack[x] will then be the value and divide by 2
else: #odd instances
    attackMedian = attack[len(attack) // 2] #finds the middle and then finds the value in that position

if len(defense)%2 == 0 : #conditional if the column has an even number of instances
    defenseMedian = (defense[len(defense) // 2 - 1 ] + defense[len(defense) // 2]) / 2
    #defense[] is just getting the index
    #the math inside the [] does the floor division to get the first place then subtracts 1 to get the position before
    #the second part of the math does the same by finding the middle but does not need to be subtraced since we found the position before
    #The defense[x] will then be the value and divide by 2
else: #odd instances
    defenseMedian = defense[len(defense) // 2] #finds the middle and then finds the value in that position

if len(speed)%2 == 0: #conditional if the column has an even number of instances
    speedMedian = (speed[len(speed) // 2 - 1] + speed[len(speed) // 2]) / 2
    #speed[] is just getting the index
    #the math inside the [] does the floor division to get the first place then subtracts 1 to get the position before
    #the second part of the math does the same by finding the middle but does not need to be subtraced since we found the position before
    #The speed[x] will then be the value and divide by 2
else: #odd instances
    speedMedian = speed[len(speed) // 2] #finds the middle and then finds the value in that position

medians = [attackMedian, defenseMedian, speedMedian]  #holds the medians in the list
print("Medians for attack, defense, and speed: ", medians) #prints the list

#range for attack, defense, and speed
attackRange = max(attack) - min(attack) #highest value in attack - the lowest value in attack
defenseRange = max(defense) - min(defense) #highest value in defense - the lowest value in defesne
speedRange = max(speed) - min(speed) #highest value in speed - the lowest value in speed

ranges = [attackRange, defenseRange, speedRange] #holds the ranges in the list
print("Ranges for attack, defense, and speed: ", ranges) #prints the list
