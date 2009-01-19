#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    int a =5;
    char buf[250];
    strncpy(buf, argv[1], sizeof(buf) - 1);

    printf(buf);

    return 0;
}

