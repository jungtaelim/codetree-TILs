#include <iostream>
using namespace std;
#define max_n 20

int n;
int M[max_n][max_n];

int summ(int r, int c, int k, int l) {
    int dir_x[4] = { 1, -1, -1, 1 };
    int dir_y[4] = { -1, -1, 1, 1 };
    int count[4] = { k, l, k, l };

    int sum_t = 0;
    int x = c;
    int y = r;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < count[i]; j++) {
            y += dir_y[i];
            x += dir_x[i];

            if (x<0 or y<0 or x>n or y>n) {
                return 0;
            }

            sum_t += M[y][x];
        }
    }
    return sum_t;

}



int main() {
    cin >> n;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            cin >> M[row][col];
        }
    }

    int a = 0;
    int maxi = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            for (int k = 1; k < n; k++) {
                for (int l = 1; l < n; l++) {
                    a = summ(row, col, k, l);
                    if (maxi < a) {
                        maxi = a;
                    }
                }
            }
        }
    }
    cout << maxi;
    return 0;
}