#include <cs50.h>
#include <stdio.h>

void print__colum(int height);


int main(void)
{
    int h = get_int("Height: ");
    print__colum(h);
}

void print__colum(int height)
{
    for ( int i = 0; i < height; i++)
    {
        printf("#\n");
    }
}