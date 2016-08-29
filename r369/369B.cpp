#include <iostream>
#include <algorithm>
using namespace std;
int grid[501][501] = {0};

int main(){
    int n;
    cin >> n;
    int mrow,mcolumn;
    for(int i = 0; i < n; i++){
        for(int k = 0; k < n; k++){
            int temp;
            cin >> temp;
            if(temp == 0){
                mrow  = i;
                mcolumn = k;
            }
            grid[i][k] = temp;
        }
    }
    if(n==1){
        cout << "1" << endl;
        return 0;
    }
    long long int total[1002] = {0};
    for(int i = 0; i < n; i++){
        for(int k = 0; k < n; k++){
            total[i] += grid[i][k];
            total[k+500] += grid[i][k];
        }
        total[1000] += grid[i][i];
        total[1001] += grid[i][n-i-1];
    }

    bool flag = false;
    long long int minTotal = total[mrow];
    long long int maxTotal = 0;
    long long int missing = 0;
    for(int i = 0; i < n; i++){
        if(maxTotal < total[i] )
            maxTotal = total[i];
        if(total[i] < minTotal){
            cout << -1;
            return 0;
        }
    }
    missing = maxTotal-total[mrow];
    total[mrow] += missing;
    total[500+mcolumn] += missing;
    if(mrow == mcolumn)
        total[1000] += missing;
    if(mrow == n-mcolumn-1)
        total[1001] += missing;

    for(int i = 0; i < n; i++){
//        cout << total[i]  << " "<< total[i+500] << " " << total[1000] << " " << total[1001];
        if(maxTotal !=  total[i] || maxTotal != total[i+500]|| maxTotal != total[1000] || maxTotal != total[1001]){
            cout << "-1" << endl;
            return 0;
        }
    }
    if(missing != 0)
        cout << missing;
    else
        cout << -1;
    return 0;
}
