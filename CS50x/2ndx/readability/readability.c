#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");

    int n = strlen(text);
    float l = 0;
    float w = 1;
    float s = 0;

    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            l++;
        }
        if (text[i] == 32)
        {
            w++;
        }
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            s++;
        }
    }
    float L = 100 * (l / w);
    float S = 100 * (s / w);

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}