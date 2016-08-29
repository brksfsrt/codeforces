#include <iostream>
#include <algorithm>
using namespace std;
char arr[1001][5];

int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int k = 0; k < 5; k++){
            cin >> arr[i][k];
        }
    }
    bool flag = false;
    for(int i = 0; i < n; i++){
        if((arr[i][0] == 'O' && arr[i][1] == 'O' )){
            flag = true;
            arr[i][0] = '+';
            arr[i][1] = '+';
            break;
        }
        else if((arr[i][3] == 'O' && arr[i][4] == 'O' )){
            flag = true;
            arr[i][3] = '+';
            arr[i][4] = '+';
            break;
        }
    }
    if(flag){
        cout << "YES" << endl;
        for(int i = 0; i < n; i++){
            for(int k = 0; k < 5; k++)
                cout << arr[i][k];
            cout << endl;
        }
    }
    else{
        cout << "NO" << endl;
    }


    return 0;
}
