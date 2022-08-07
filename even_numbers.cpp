#include <iostream>
using namespace std;

int main (){
    int num;
    int i = 1;
    int sum = 0;

    cout << "enter a number: ";
    cin >> num;
/*Odd numbers can be found by letting the if statement's condition to be 1*/
    while (i < num){
        if (i%2 == 0){
            sum = sum +i;
        }
    i= i+1;
    }

    cout <<"The sum of even numbers less than " <<num<< " is " <<sum;
    
    return 0;
}
