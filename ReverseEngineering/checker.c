#include <stdio.h>
#include <string.h>
#include <stdint.h>

#define LENGTH 12

uint8_t target[LENGTH] = {
    0x91,0xA3,0xB2,0x80,0xA6,0xC1,
    0x97,0x8F,0xB5,0x92,0xA4,0x88
};

uint8_t key[LENGTH] = {
    0x13,0x37,0x42,0x55,0x21,0x19,
    0xAA,0xFE,0x10,0x99,0xAB,0xCD
};

uint8_t encrypted_flag[] = {
    0x21,0x3d,0x35,0x29,0x5a,0x11,0x07,0x1c,
    0x00,0x17,0x0d,0x17,0x1c,0x02,0x0b,0x06,
    0x00,0x00,0x17,0x00,0x10,0x07,0x00,0x01
};

uint8_t rotate_left(uint8_t value, int shift)
{
    return (value << shift) | (value >> (8 - shift));
}

int check_password(char *input)
{
    if(strlen(input) != LENGTH)
        return 0;

    for(int i = 0; i < LENGTH; i++)
    {
        uint8_t x = input[i];

        x ^= key[i];
        x = rotate_left(x,3);
        x += i;
        x ^= 0x5A;

        if(x != target[i])
            return 0;
    }

    return 1;
}

void print_flag(char *password)
{
    int flag_len = sizeof(encrypted_flag);

    printf("Flag: ");

    for(int i = 0; i < flag_len; i++)
    {
        char c = encrypted_flag[i] ^ password[i % LENGTH];
        printf("%c", c);
    }

    printf("\n");
}

int main()
{
    char password[64];

    printf("Enter password: ");
    scanf("%63s", password);

    if(check_password(password))
    {
        printf("Correct!\n");
        print_flag(password);
    }
    else
    {
        printf("Wrong password.\n");
    }

    return 0;
}
