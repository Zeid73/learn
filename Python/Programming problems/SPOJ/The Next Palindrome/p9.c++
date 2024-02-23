//Author: Mohd. Ali Solanki
#include <bits/stdc++.h>
#define lli long long int
using namespace std;

string findNextPalin(string K) {
    lli len = K.length();
    string x = K;
    for (lli i = len/2; i < len; i++) {
        K[i] = K[len-i-1];
    }
    if(K > x){
        return K;
    }else{
        for (lli i = (len-1)/2; i >= 0; i--) {
            if(x[i]!='9'){
                x[i]++;
                break;
            }else{
                x[i] = '0';
            }
        }
        for (lli i = len/2; i < len; i++) {
            x[i] = x[len-i-1];
        }
        if(x[0] == '0'){
            x+='1';
            x[0] = '1';
        }
        return x;
    }
}

int main() {
	int T;
	scanf("%d", &T);
	while(T--){
	    string K;
	    cin>>K;
	    cout<<findNextPalin(K)<<endl;
	}
	return 0;
}
