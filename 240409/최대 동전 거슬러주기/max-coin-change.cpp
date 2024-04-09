#include<iostream>
using namespace std;
long long dp[10001];

void init() {
	for (int i = 0; i < 10001; i++) {
		dp[i] = -1;
	}
	dp[0] = 0;
}


int main() {
	int N, M;
	cin >> N >> M;

	int s[101];

	init();

	for (int i = 0; i < N; i++) {
		cin >> s[i];
	}

	for (int i = 0; i < M; i++) {
		if (dp[i] >= 0) {
			for (int j = 0; j < N; j++) {
				if (i + s[j] <= M && dp[i + s[j]] < dp[i] + 1) {
					dp[i + s[j]] = dp[i] + 1;
				}
			}
		}
	}
	if (dp[M] == -1) {
		cout << -1;
	}
	else {
		cout << dp[M];
	}
}