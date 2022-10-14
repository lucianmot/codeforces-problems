// C++ - Increasing
// Rating - ---
// https://codeforces.com/contest/1742/problem/B

#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t, n;
    cin >> t;
    while(t--) {
        cin >> n;
        int theList[n];
        for ( int i = 0; i < n; i++ ) {
            int num;
            cin >> num;
            theList[i] = num;
        }
        sort(theList, theList + n);
        if ( n == 1 ) {
            cout << "YES" << endl;
        } else {
            int answer = 0;
            int m = n - 1;
            for ( int j = 0; j < m; j++ ) {
                if ( theList[j] < theList[j+1] ) {
                    answer = 0;
                } else {
                    answer = 1;
                    break;
                }
            }
            if ( answer == 0 ) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
    }
    return 0;
}
