#include<iostream>
int A[100000];
int B[100000];
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;
	for (int i = 0; i < 100000; i++) {
		B[i]=100000;
	}
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		A[i] = a;
		B[a] = 1;
	}

	for (int i = 1; i < M; i++) {
		for (int j = 0; j < N; j++) {

			if (B[i] != 100000 && (B[i + A[j]] > B[i] + 1)) {
				
				B[i + A[j]] = B[i];
				B[i + A[j]]++;
			}
		}
	}


	cout << B[M];



}