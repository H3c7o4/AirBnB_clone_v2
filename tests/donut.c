#include <stdio.h>
#include <math.h>

const float pi = 3.14159265358979323846;

int main() {
    for(float i = 0; i < 2 * pi; i += 0.05) {
        for(float j = 0; j < 2 * pi; j += 0.01) {
            float x = sin(i) * (2 + cos(j));
            float y = cos(i) * (2 + cos(j));
            float z = sin(j);
            float dist = sqrt(x * x + y * y + z * z);
            int intensity = (int)((cos(dist * 6) - dist * sin(dist * 2)) * 8);
            putchar(".,-~:;=!*#$@"[intensity]);
        }
        putchar('\n');
    }
    return 0;
}
