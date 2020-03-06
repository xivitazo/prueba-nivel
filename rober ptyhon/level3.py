import math
PI= 3.1415926535
input = "1.09 4 9.86 10 9.86 10 9.86 10 9.86 10"
splited=input.split()
base_Angle=0
x_Total=0
y_Total=0
wheelBase=float(splited[0])
num_Movements=int(splited[1])
for n in range (2,2+2*num_Movements,2) :
    distance=float(splited [n])
    steeringAngle=float(splited[n+1])
    if steeringAngle>0 :
        turnRadius=wheelBase/math.sin((steeringAngle*PI)/180)
    elif steeringAngle <0 :
        turnRadius=wheelBase/math.sin((-steeringAngle*PI)/180)
    else :
        x_Total+=distance*math.sin(base_Angle)
        y_Total+=distance*math.cos(base_Angle)
        continue
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
    x_New=math.cos(base_Angle)*x+math.sin(base_Angle)*y
    y_New=-math.sin(base_Angle)*x+math.cos(base_Angle)*y
    x_Total+=x_New
    y_Total+=y_New
    base_Angle+=(degRideAngle*PI)/180
final_Angle=(base_Angle*180)/PI
if final_Angle>=360 :
    vueltas=final_Angle/360
    final_Angle-=360*vueltas
if(final_Angle<0) :
    final_Angle=360-final_Angle
print (round(x_Total,2), round(y_Total), round(final_Angle,2))