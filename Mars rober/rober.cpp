#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>


#define PI 3.1415926535


using namespace std;

int main (int argc, char *argv[])
{
    string input = "9.53 10 -1.00 1.00 -2.00 2.00 3.00 -3.00 4.00 4.00 5.00 -5.00 6.00 6.00 7.00 7.00 -8.00 8.00 9.00 9.00 10.00 -10.00";
    stringstream s_input (input);
    string value;
    float base_Angle=0;
    float x_Total=0, y_Total=0;

    getline (s_input, value, ' ');
    float wheelBase=stof(value);

    getline (s_input, value, ' ');
    int num_Movements=stoi(value);

    for (int n=0;n<num_Movements;n++)
    {
        getline (s_input, value, ' ');
        float distance=stof(value);
        
        getline (s_input, value, ' ');
        float steeringAngle=stof(value);

        

        float turnRadius;
        if (steeringAngle>0)
            turnRadius=wheelBase/sin((steeringAngle*PI)/180);
        else if (steeringAngle<0)
        {
            turnRadius=wheelBase/sin((-steeringAngle*PI)/180);
        }
        else
        {
            //cout<<std::fixed<<std::setprecision(2)<<"0.00 "<<distance<<' '<<0.00;
            x_Total+=distance*sin(base_Angle);
            y_Total+=distance*cos(base_Angle);
            continue;
        }
        
            

        float radRideAngle =distance/turnRadius;
        float degRideAngle = (180*(radRideAngle))/PI;
        if(degRideAngle>360)
        {
            int vueltas=degRideAngle/360;
            degRideAngle=degRideAngle-360*vueltas;
        }
        if (degRideAngle<0)
        {
            degRideAngle=360+degRideAngle;
        }
        if (steeringAngle<0)
        {
            degRideAngle=360.0-degRideAngle;
        }
        float x,y;
        if(steeringAngle>0)
        {
            x=turnRadius-(turnRadius*cos(radRideAngle));
            y=turnRadius*sin(radRideAngle);
        }
        else
        {
            x=(turnRadius*cos(radRideAngle))-turnRadius;
            y=turnRadius*sin(radRideAngle);
        }

        float x_New=cos(base_Angle)*x+sin(base_Angle)*y;
        float y_New=-sin(base_Angle)*x+cos(base_Angle)*y;
        x_Total+=x_New;
        y_Total+=y_New;
        base_Angle+=(degRideAngle*PI)/180;
    }
    float final_Angle=(base_Angle*180)/PI;
    if ((int)final_Angle>=360)
    {
        int vueltas=final_Angle/360;
        final_Angle-=360*vueltas;
    }
    if(final_Angle<0)
        final_Angle=360-final_Angle;
    
    cout<<std::fixed<<std::setprecision(2)<<x_Total<<' '<<y_Total<<' '<<final_Angle;
}