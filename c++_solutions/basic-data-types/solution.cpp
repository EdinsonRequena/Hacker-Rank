#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int integer;
    long longNumber;
    char ch;
    float floatNumber;
    double doubleNumber;

    scanf("%d %ld %c %f %lf", &integer, &longNumber, &ch, &floatNumber, &doubleNumber);
    printf("%d\n%ld\n%c\n%f\n%lf\n", integer, longNumber, ch, floatNumber, doubleNumber);

    return 0;
}
