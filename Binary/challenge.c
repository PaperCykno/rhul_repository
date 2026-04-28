#include <stdio.h>
#include <stdlib.h>

void win() {
    FILE *f = fopen("flag.txt", "r");
    if (!f) {
        puts("Missing flag.txt");
        exit(1);
    }

    char flag[128];
    fgets(flag, sizeof(flag), f);
    printf("%s", flag);
    fclose(f);
    exit(0);
}

void vuln() {
    char buf[64];
    puts("Enter your name:");
    gets(buf);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    puts("RHUL ret2win challenge");
    vuln();
    return 0;
}
