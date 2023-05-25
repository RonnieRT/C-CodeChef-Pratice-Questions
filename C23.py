#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	string s;
	cin>>s;
	reverse(begin(s),end(s));
	int count=0,maxi=0;
	for(int i=0;i<=t;i++){
	   if(s[i]=='0'){
	       count++;
	       
	   }
	   else{
	       break;
	   }
	}
	cout<<count<<endl;
	return 0;
}
