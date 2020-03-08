import requests
import math
def mover (x, y ,angle,distance, steeringAngle) :
    if steeringAngle>0 :
        turnRadius=wheelBase/math.sin((steeringAngle*PI)/180)
    elif steeringAngle <0 :
        turnRadius=wheelBase/math.sin((-steeringAngle*PI)/180)
    else :
        x+=distance*math.sin(angle)
        y+=distance*math.cos(angle)
        return x, y , angle
    radRideAngle =distance/turnRadius
    degRideAngle = (180*(radRideAngle))/PI
    if degRideAngle>360 :
        vueltas=int (degRideAngle/360)
        degRideAngle=degRideAngle-360*vueltas
    if degRideAngle<0 :
        degRideAngle=360+degRideAngle
    if steeringAngle<0 :
        degRideAngle=360.0-degRideAngle
    if steeringAngle>0 :
        x=turnRadius-(turnRadius*math.cos(radRideAngle))
        y=turnRadius*math.sin(radRideAngle)
    else :
        x=(turnRadius*math.cos(radRideAngle))-turnRadius
        y=turnRadius*math.sin(radRideAngle)
    x_New=math.cos(angle)*x+math.sin(angle)*y
    y_New=-math.sin(angle)*x+math.cos(angle)*y
    x+=x_New
    y+=y_New
    angle+=(degRideAngle*PI)/180
    if angle>=360 :
        vueltas=angle/360
        angle-=360*vueltas
    if(angle<0) :
        angle=360-angle
    return x,y,angle
PI=3.1415926535
url_core='https://rover.codingcontest.org'
s_input='L5_MAF3401R'
username='xivitazo'
resp=requests.get(url_core+'/rover/create?map='+s_input+'&username='+username+'&contestId=practice')
UUID=resp.text
#print (UUID)
spetifications=requests.get(url_core+'/rover/'+UUID)
print (spetifications.text)
splited=spetifications.text.split()
wheelBase = float(splited[0])
maxSteeringAngle = float(splited[1])
targetX = float(splited[2])
targetY = float(splited[3])
targetRadius = float(splited[4])

turn_radius=math.sqrt(math.pow(targetX,2)+math.pow(targetY,2))

steeringAngle = ((math.asin(wheelBase/turn_radius))*180)/PI
#minTurnRadius=wheelBase/math.sin((maxSteeringAngle*PI)/180)

#print (str(turn_radius )+ ' ' + str(minTurnRadius))



toMoveDistance=math.atan(targetY/targetX)*turn_radius



status=requests.get(url_core+'/rover/move/'+UUID+'?distance='+str(toMoveDistance)+'&steeringAngle='+str(steeringAngle))
print(status.text)
splited=status.text.split()
if splited[0]== 'OK' :
    movedDistance=float(splited[1])
elif splited [0] == 'ERROR':
    print(status.text)
    exit()
elif splited[0] == 'PASS':
    passKey = splited[1]
    totalDistance = splited [2]
    endPass=requests.get(url_core+'/rover/move/'+UUID+'?distance='+str(toMoveDistance)+'&steeringAngle='+str(steeringAngle))
    splited=endPass.text.split()
    passKey = splited[1]
    totalDistance = splited [2]
    print (passKey)
    exit ()

print (str(mover(0,0,0,toMoveDistance,steeringAngle)) + ' '+ str(toMoveDistance) + ' '+ str(steeringAngle))