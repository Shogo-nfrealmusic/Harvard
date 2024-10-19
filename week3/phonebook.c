#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[3];
    people[0].name = "Shogo";
    people[0].number = "+1-000-000-0000";
    people[1].name = "Haruka";
    people[1].number = "+1-111-111-1111";
    people[2].name = "Harvard";
    people[2].number = "+1-222-222-2222";

    string name = get_string("Name: ");

    for (int i =0; i < 3; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}