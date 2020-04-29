import random
import copy
countryList = ['Oslo','Helsinki','Tallinn','Moscow','Riga','Minsk','Vilnius','Kyiv','Chisinau','Tbilisi','Yerevan','Baku','Ankara','Sofia','Bucharest','Warsaw','Stockholm','Copenhagen','Berlin','Amsterdam','Brussels','Prague','Luxembourg','Paris','Bern','Ljubljana','Zagreb','Belgrade','Budapest','Bratislava','Skopje','Athens','Tirana','Podgorica','Pristina','Sarajevo','Rome','Madrid','Lisbon','Vienna']
countryCoords = [[-104,246],[130,259],[117,229],[313,124],[109,157],[185,81],[129,94],[217,-20],[186,-100],[438,-218],[433,-250],[518,-246],[257,-252],[104,-196],[146,-158],[60,29],[13,229],[-74,119],[-67,36],[-191,44],[-201,-9],[-43,-24],[-174,-43],[-233,-53],[-151,-100],[-48,-122],[-17,-126],[51,-148],[32,-87],[1,-73],[66,-212],[104,-296],[43,-230],[32,-204],[61,-196],[19,-172],[-68,-215],[-322,-240],[-416,-277],[-17,-71]]
countryNumbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
import turtle
import itertools
turtle.bgpic("pythonmap2.gif")
turtle.title('Plan Your EuroTrip!')
global priceGlo
priceGlo = 0

def OneCountryList(length):
    temp = []
    for i in range (0,length):
        temp = temp + [random.randint(150,500)]
    return temp

def generateCountryMatrix(n):
    temp = []
    for i in range (0,n):
        temp = temp + [OneCountryList(n)]
        temp[i][i] = 0
    return temp

matrix = generateCountryMatrix(40)

def positionItem(item,listy):
    return listy.index(item)

def duplicate(path):
    if len([x for x in path if path.count(x) > 1]) > 0:
        return 'true'
    else:
        return 'false'

def noDuplicates(paths):
    return [x for x in paths if duplicate(x) == 'false']

def allPossiblePaths(start,countries,countryNumber):
    def plusStart(microList):
        ball = [start]
        ball.extend(microList)
        return ball
    return noDuplicates(map(plusStart,list(itertools.permutations(countries,countryNumber-1))))

def costTrip(trip,matrix):
    cost = 0
    for i in range(0,len(trip)-1):
        cost = cost + matrix[trip[i]][trip[i+1]]
    return cost

def cheapestPathPrice(startCountry,countryList,countryAmount,matrix):
    temp = allPossiblePaths(startCountry,countryList,countryAmount)
    temp2 = [costTrip(x,matrix) for x in temp]
    temp3 = min(temp2)
    return [temp3,positionItem(temp3,temp2)]

def cheapestNetRoute(startCountry,countryAmount,matrix):
    temp = cheapestPathPrice(startCountry,countryNumbers,countryAmount,matrix)
    position = temp[1]
    routes = allPossiblePaths(startCountry,countryNumbers,countryAmount)
    global priceGlo
    priceGlo = temp[0]
    return routes[position]

#def pathPrice(listy):
    #for i in range(0,len(listy)):

def cheapestInList(listy):
    return min([x for x in listy if x != 0])

def cheapestTrip(country,amount,matrix):
    tempMatrix = copy.deepcopy(matrix)
    temp = [country]
    price = 0
    cCountry = country
    def zeroItem(listy):
        temp = listy
        temp[cCountry] = 0
        return temp
    for i in range(0,amount-1):
        nCountry = positionItem(
        cheapestInList(tempMatrix[cCountry]),tempMatrix[cCountry]
        )
        temp = temp + [nCountry]
        price = price + cheapestInList(tempMatrix[cCountry])
        map(zeroItem,tempMatrix)
        cCountry = nCountry
    global priceGlo
    priceGlo = price
    return temp

def cheapestTripWithNames(country,amount,matrix):
    numberAnswer = cheapestTrip(country,amount,matrix)
    return [countryList[x] for x in numberAnswer]

def cheapestTripWithNamesNet(country,amount,matrix):
    numberAnswer = cheapestNetRoute(country,amount,matrix)
    return [countryList[x] for x in numberAnswer]

def cheapestTripAnimated(country,amount,matrix):
    countryCounter = 0
    numberAnswer = cheapestTrip(country,amount,matrix)
    coordAnswer = [countryCoords[x] for x in numberAnswer]
    turtle.penup()
    turtle.goto(coordAnswer[0])
    turtle.pendown()
    turtle.pencolor(0,0,0)
    turtle.write('Start here!',font=('Courier',20,'bold'))
    turtle.pencolor(1,1,1)
    turtle.write('Start here!',font=('Courier',20,'normal'))
    turtle.pensize(2)
    turtle.pencolor(1,0,0)
    for i in range(0,len(coordAnswer)):
        countryCounter = countryCounter + 1
        turtle.goto(coordAnswer[i])
        if countryCounter != 1:
            turtle.pencolor(0,0,0)
            turtle.write(str(countryCounter) + '.',font=('Courier',16,'bold'))
            turtle.pencolor(1,1,1)
            turtle.write(str(countryCounter) + '.',font=('Courier',16,'normal'))
        turtle.pencolor(1,0,0)
    return cheapestTripWithNames(country,amount,matrix)

def cheapestTripAnimatedNet(country,amount,matrix):
    countryCounter = 0
    numberAnswer = cheapestNetRoute(country,amount,matrix)
    coordAnswer = [countryCoords[x] for x in numberAnswer]
    turtle.penup()
    turtle.goto(coordAnswer[0])
    turtle.pendown()
    turtle.pencolor(0,0,0)
    turtle.write('Start here!',font=('Courier',20,'bold'))
    turtle.pencolor(1,1,1)
    turtle.write('Start here!',font=('Courier',20,'normal'))
    turtle.pensize(2)
    turtle.pencolor(1,0,0)
    for i in range(0,len(coordAnswer)):
        countryCounter = countryCounter + 1
        turtle.goto(coordAnswer[i])
        if countryCounter != 1:
            turtle.pencolor(0,0,0)
            turtle.write(str(countryCounter) + '.',font=('Courier',16,'bold'))
            turtle.pencolor(1,1,1)
            turtle.write(str(countryCounter) + '.',font=('Courier',16,'normal'))
        turtle.pencolor(1,0,0)
    return cheapestTripWithNamesNet(country,amount,matrix)

def xyCoord():
    canvas = turtle.getcanvas()
    x = canvas.winfo_pointerx()
    y = canvas.winfo_pointery()
    return (x,y)

def zingAll():
    for i in range(0,len(countryCoords)):
        turtle.goto(countryCoords[i])

def reset():
    turtle.goto(0,0)
    turtle.clear()

def ELrunScript():
    reset()
    print("Welcome to EuroTrip Planner!")
    question1 = input("Does your dad earn more than $150,000 a year?: ")
    if question1 == 'yes':
        question2 = input("Do you attend a private high school?: ")
        if question2 == 'yes':
            print('Great! Sounds like you\'ve got enough money and class to afford the trip of your life!')
            startCountry = str(input("What capital city would you like to start in?: "))
            countryCount = input("How many countries would you like to visit?: ")
            print(cheapestTripWithNames(positionItem(startCountry,countryList),countryCount,matrix))
            print('Your trip will cost $' + str(priceGlo))
            print("Generating map...")
            cheapestTripAnimated(positionItem(startCountry,countryList),countryCount,matrix)
            print('Map complete. Enjoy your trip and don\'t forget to use location tags when you post photos of all the cool spots you can afford to visit!')
        else:
            print('I\'m sorry, you aren\'t of a high enough class to pull of a EuroTrip...')
    else:
        print("I'm sorry, you don't have enough money to afford a EuroTrip...")

def runScript():
    reset()
    print("Welcome to EuroTrip Planner!")
    startCountry = input("In which capital city would you like to start?: ")
    countryCount = input("How many countries would you like to visit?: ")
    print(cheapestTripWithNames(positionItem(startCountry,countryList),countryCount,matrix))
    print('Your trip will cost $' + str(priceGlo))
    print("Generating map...")
    cheapestTripAnimated(positionItem(startCountry,countryList),countryCount,matrix)
    print('Map complete. Enjoy your trip and don\'t forget to use location tags when you post photos of all the cool spots you can afford to visit!')

#runScript()

def runNetScript():
    reset()
    print("Welcome to EuroTrip Planner!")
    startCountry = input("In which capital city would you like to start?: ")
    countryCount = input("How many countries would you like to visit? Don't enter any more than 5: ")
    print('Computing cheapest possible trip. This may take a minute...')
    print(cheapestTripWithNamesNet(positionItem(startCountry,countryList),countryCount,matrix))
    print('Your trip will cost $' + str(priceGlo))
    print("Generating map...")
    cheapestTripAnimatedNet(positionItem(startCountry,countryList),countryCount,matrix)
    print('Map complete. Enjoy your trip and don\'t forget to use location tags when you post photos of all the cool spots you can afford to visit!')

runNetScript()
