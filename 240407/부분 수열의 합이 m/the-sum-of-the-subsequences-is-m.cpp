#include<iostream>
using namespace std;
int A[10000];

int main() {
	
	int n, m;
	cin >> n >> m;
	int N[100];

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		N[i] = a;
	}

	for (int i = 0; i < m+1; i++) {
		A[i] = 100000;
	}

	A[0] = 0;

	for (int j = 0; j < n; j++) {
		for (int i = m+1; i > 0; i--) {
			if (A[i - N[j]] == 100000 || i - N[j] < 0) {
				continue;
			}
			if (A[i] > A[i- N[j]] + 1) {
				A[i] = A[i - N[j]] + 1;
			}
		}
	}

	if (A[m] == 100000) {
		cout << -1;
	}
	else {
		cout << A[m];
	}
}