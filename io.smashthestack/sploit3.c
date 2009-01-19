#include <stdio.h>

int main(int argc, char** argv){
            int i;
            char buf[1024], *p;

            p = buf;

            for(i=0; i<10; i++){
                sprintf(p, "%s","\x7f\x84\x04\x08"); //"\x08\x04\x84\x2f");
                p += 4;
            }

            printf("%s\n", buf);

}

