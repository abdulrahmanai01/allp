#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x=10, y=12, z=15;
    int *p=&x, *q=&y, *r=&z;

    printf("\t.........................\n ");
    printf("\t.........................\n ");
    printf("Enter the value of x : %d \n\t",x);
    printf(".........................\n ");
    printf("\t.........................\n ");
    printf("Address of the value x : %d \n\t",p);
    printf("\t.........................\n ");
    printf("\t.........................\n ");
    printf("Enter the value of x : %d \n\t",*p);
    printf("\t.........................\n ");
    printf("\t.........................\n ");


    printf("Enter the value of y : %d \n\t",y);
    printf("\t.........................\n ");
    printf("\t.........................\n ");
    printf("Address of the value y : %d \n\t",q);
    printf("\t.........................\n ");
    printf("\t.........................\n ");
    printf("Enter the value of y : %d \n\t",*q);
    printf("\t.........................\n ");
    printf("\t.........................\n ");


    printf("Enter the value of z : %d \n\t",z);
    printf("\t.........................\n ");
    printf("\t.........................\n ");
    printf("Address of the value z : %d \n\t",r);
    printf("\t.........................\n ");
    printf("\t.........................\n ");
    printf("Enter the value of z : %d \n\t",*r);
    printf("\t.........................\n ");
    printf("\t.........................\n ");


    return 0;
}
