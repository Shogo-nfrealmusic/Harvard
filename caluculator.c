#include <cs50.h> 
#include <stdio.h> 

// int add(int x, int y);

int main(void)
{
    float x = get_int("x: ");
    float y = get_int("y: ");

    float z = x / y;

    printf("%f\n", z);
}

// int add(int x, int y)
// {
//     return x + y;
// }