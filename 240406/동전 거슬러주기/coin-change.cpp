#include<iostream>
int A[100];
int B[100];
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;
	for (int i = 0; i < 100; i++) {
		B[i]=INT_MAX;
	}
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		A[i] = a;
		B[a] = 1;
	}

	for (int i = 1; i < M; i++) {
		for (int j = 0; j < N; j++) {

			if (B[i] != INT_MAX && (B[i + A[j]] > B[i] + 1)) {
				
				B[i + A[j]] = B[i];
				B[i + A[j]]++;
			}
		}
	}

	cout << B[M];



}