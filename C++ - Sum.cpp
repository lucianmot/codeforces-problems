// C++ - Sum
// Rating - ---
// https://codeforces.com/contest/1742/problem/A

#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t, a, b, c;
    cin >> t;
    while(t--) {
        cin >> a >> b >> c;
        int sum = 0;
        if ( a == b + c ) {
            sum = 1;
        } else if ( b == a + c ) {
            sum = 1;
        } else if ( c == a + b ) {
            sum = 1;
        }
        sum == 1 ? cout << "YES" << endl : cout << "NO" << endl;
    }
    return 0;
}
