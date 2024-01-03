#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int present;
    do
    {
        present = get_int("Present Size: ");
    }
    while (present < 9);

    // TODO: Prompt for end size
    int final;
    do
    {
        final = get_int("Final Size: ");
    }
    while (final < present);

    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    int inc = present;

    while (present < final)
    {
        inc = (present / 3) - (present / 4);
        present = present + inc;
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}