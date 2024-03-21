#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define max_num 20
int n, m;
int M[max_num][max_num];

int fee(int k) {
    return k * k + (k + 1) * (k + 1);
}

int how_much(int x, int y, int k) {
    int gold = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (abs(row - x) + abs(col - y) <= k) {
                gold += M[row][col];
            }
        }
    }
    return gold;
}


int main() {



    cin >> n >> m;
   

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            cin >> M[row][col];
        }
    }
    int maxi = 0;

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            for (int k = 0; k < 2 * (n - 1)+1; k++) {
                int a = how_much(row, col, k);

                if (a*m >= fee(k)) {
                    maxi = max(maxi, a);
                }
            }
        }
    }

    cout << maxi;

    return 0;
}