#include <cs50.h> 
#include <stdio.h> 

// int add(int x, int y);

int main(void)
{
    double x = get_int("x: ");
    double y = get_int("y: ");

    double z = x / y;

    printf("%.20f\n", z);
}

// int add(int x, int y)
// {
//     return x + y;
// }