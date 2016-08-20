#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int minValues[100001][3] = {0};

bool binarySearch(int *array,int key,int first,int last){
    if(first > last)
        return false;
    int middle = (first+last)/2;
    if(array[middle] < key)
        return binarySearch(array,key,middle+1,last);
    if(array[middle] > key)
        return binarySearch(array,key,first,middle-1);
    else
        return true;
}

int main()
{
    int n,m,k;
    cin >> n >> m >> k;
    for (int i = 0; i < m; i++){
        int x,y,z;
        cin >> x >> y >> z;

        minValues[i][0] = x;
        minValues[i][1] = y;
        minValues[i][2] = z;
    }
    int *storages = new int[k];
    for(int i = 0; i < k; i++)
        cin >> storages[i];
    if(k == 0){
            cout << -1;
            return 0;
    }
    int minimum = -1;
    sort(storages,storages+k);
    for(int i = 0; i < m; i++){
        int temp;
        if((binarySearch(storages,minValues[i][0],0,k) && !(binarySearch(storages,minValues[i][1],0,k)))||(!(binarySearch(storages,minValues[i][0],0,k)) && (binarySearch(storages,minValues[i][1],0,k)))){
            temp = minValues[i][2];
            if(minimum > temp || minimum == -1)
                minimum = temp;
        }
    }
    cout << minimum;
    return 0;

}
