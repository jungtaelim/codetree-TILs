#include<iostream>
using namespace std;
long long dp[1000];

int main() {
	int s[3] = { 1,2,5 };
	long long n;
	dp[1] = 1;
	dp[2] = 1;
	dp[5] = 1;
	
	cin >> n;
	
	for (long long i = 1; i <= n; i++) {

		if (dp[i] != 0) {

			for (int j = 0; j < 3; j++) {
				if (i + s[j] > n) {
					continue;
				}
				dp[i + s[j]] = dp[i + s[j]] + dp[i];

			}
		}
	}
	
	cout << dp[n]%10007;

}