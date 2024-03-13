#include<stdio.h>

void main()
{

float a,b;
printf("enter length");
scanf("%f",&a);
printf("enter breadth");
scanf("%f",&b);
if(a*b>(2*a+2*b))
printf("area is greater than perimeter\narea:%f\tperimeter:%f",a*b,2*a+2*b);
if(a*b<(2*a+2*b))
printf("peirmeter is greater area\nperimeter:%f\tarea:%f",2*a+2*b,a*b);

}