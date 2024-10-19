#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Input: ");
    printf("Output: ");
    int n = strlen(s);  // 文字列の長さを変数 n に格納
    for (int i = 0; i < n; i++)
    {
        printf("%c", s[i]);  // 各文字を順に出力
    }
    printf("\n");
}

