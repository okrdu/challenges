#include <stdio.h>

int main() {

    int j = 60, i = 1;

    for (j; j >= 0; j -= 5) {
        printf("I=%d J=%d\n", i, j);
        i += 3;
    }

    return 0;

}