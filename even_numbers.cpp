#include <iostream>
using namespace std;

int main (){
    int num;
    int i = 1;
    int sum;

    cout << "enter a number: ";
    cin >> num;

    while (i < num){
        if (i%2 == 0){
            sum = sum +1;
        }
    i= i+1;
    }

    cout <<"The sum of even numbers less than " <<num<< " is " <<sum;
}
