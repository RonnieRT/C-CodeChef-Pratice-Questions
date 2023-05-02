#include <iostream>
#include<algorithm>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    long long m,sum=0,count=0;
	    cin>>m;
	    long long a[n];
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	    }
	    int val=0;
	    sort(a,a+n);
	    for(int j=n-1;j>=0;j--){
	         if(sum>=m){
	             break;
	         }
	        sum=sum+a[j];
	         count++;
	        
	    }
	    if(sum>=m)
	     cout<<count<<endl;
	     else 
	     cout<<"-1"<<endl;

	}
	return 0;
}
