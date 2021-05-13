#include <iostream>
#include <string> 
#include <math.h>
using namespace std;

#define Pi = 3.14;
#define Day = 7;

// function 
int add(int num1, int num2) {
    int sum = num1 + num2;
    return sum;
}
int main() {
    const int month = 12;
    int radius = 4;
    cout << "hello world" << endl;
    // system("pause");
    // integer: short, int, long, long long.
    // sizeof
    short shortNum = 10;
    cout << sizeof(short) << endl;
    //float: float(up to 7), double (15-16)
    float f1 = 3.14f;
    double d1 = 3.14;
    cout << f1 << endl;
    cout << d1 << endl;
    // character: char.
    cout << sizeof(char) << endl;
    char letter = 'a';
    cout << letter << endl;
    cout << (int)letter << endl;
    // string: char variable[] = "chars", string variable = "string here"
    char chars[] = "abcdefg";
    string chars2 = "hijklmn";
    cout << chars << endl;
    cout << chars2 << endl;
    // boolean/bool: true, flase 
    bool isRunning = true;
    bool isDriving = false;
    cout << isRunning << endl;
    cout << isDriving << endl;
    // input 
    /*
    int userInput = 0;
    cout << "enter a number here: " << endl;
    cin >> userInput;
    cout << "number entered: " << userInput << endl; */

    /*int score = 0;
    cout << "enter your score: " << endl;
    cin >> score;
    if (score >= 600) {
        cout << "考上一本了";
    }else if(score >= 500) {
        cout << "二本";
    }else if(score >= 400) {
        cout << "三本";
    }else{
        cout << "trash score";
    }*/

    /*int pig1 = 0, pig2 = 0, pig3 = 0;
    cout << "enter pig1 weight: " << endl;
    cin >> pig1;
    cout << "enter pig2 weight: " << endl;
    cin >> pig2;
    cout << "enter pig3 weight: " << endl;
    cin >> pig3;
    int maxWeight = 0;
    if (maxWeight < pig1){
        maxWeight = pig1;
        if (maxWeight < pig2){
            maxWeight = pig2;
        }
        if (maxWeight < pig3){
            maxWeight = pig3;
        }
    }
    if (pig1 > pig2) {
        if (pig1 > pig3) {
            cout << "pig1: " << pig1 << endl;
        }else {
            cout << "pig3: " << pig3 << endl;
        }
    }else {
        if (pig2 > pig3) {
            cout << "pig2: " << pig2 << endl;
        }else {
            cout << "pig3: " << pig3 << endl;
        }
    }
    cout << maxWeight << endl; */

    // ternary 
    int num1 = 10; 
    int num2 = 15;
    int c = 0;
    c = num1 > num2 ? num1:num2;
    cout << c << endl;

    // while loop
    int i = 0;
    while (i < 10) {
        cout << i << endl;
        i++;
    }

    // guess number
    int number = 50;
    int userGuess = 0;
    while (0) {
        cout << "guess the number between 1 - 100: " << endl;
        cin >> userGuess;
        if (userGuess > number){
            cout << "too big, go smaller" << endl;
        }else if(userGuess < number) {
            cout << "too small, go bigger" << endl;
        }else{
            cout << "good job, you guessed it";
            break;
        }
    }

    // number 
    int theNum = 0;
    int hth = 0;
    int tenth = 0;
    int ones = 0;
    int sum = 0;
    do {
        hth = pow((theNum/100),3);
        tenth = pow((theNum/10%10),3);
        ones = pow((theNum%100%10),3);
        sum = hth + tenth + ones;
        if (sum == theNum) {
            cout << theNum << endl;;
        }
        theNum++;
    }while (theNum < 1000);

    // for loop
    cout << "for loop" << endl;
    for (int i = 0; i <= 100; i++) {
        if (i % 7 == 0 || i%10 == 7 || i/10 == 7) {
            cout << i << endl;;
        }
    }
    // nested for loop
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cout << "* ";
        }
        cout << '\n';
    }
    
    // 乘法口诀表
    for (int i = 1; i < 10; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << " * " << i  << " = " << j * i << " ";
        }
        cout << endl;
    }

    // array
    int numArray[] = {1, 3, 3, 4, 5};
    for (int i = 0; i < (sizeof(numArray)/sizeof(numArray[0])); i++) {
        cout << numArray[i] << endl;
    }
    cout << &numArray[0] << endl;
    cout << &numArray[1] << endl;
    cout << numArray << endl;

    int pigs[] = {100, 550, 200, 400, 250};
    int maxWeight = 0;
    int minWeight = pigs[0];
    for (int i = 0; i < (sizeof(pigs)/sizeof(pigs[8])); i++) {
        if (pigs[i] > maxWeight) {
            maxWeight = pigs[i];
        }
        if (pigs[i] < minWeight) {
            minWeight = pigs[i];
        }
    }
    cout << maxWeight << endl;
    cout << minWeight << endl;

    // reverse array
    for (int i = (sizeof(pigs)/sizeof(pigs[0]))-1; i >= 0; i--) {
        cout << pigs[i] << endl;
    }

    // bubble sort
    int bubbleSort[] = {4, 2, 8, 0, 5, 7, 1, 3, 9};
    for (int i = 0; i < (sizeof(bubbleSort)/sizeof(bubbleSort[0]))-1; i++) {
        for (int j = i; j < sizeof(bubbleSort)/sizeof(bubbleSort[0]); j++) {
            if (bubbleSort[i] > bubbleSort[j]) {
                int temp = 0;
                temp = bubbleSort[i];
                bubbleSort[i] = bubbleSort[j];
                bubbleSort[j] = temp;
            }
        }
    }
    for (int i = 0; i < sizeof(bubbleSort)/sizeof(bubbleSort[0]); i++) {
        cout << bubbleSort[i] << endl;
    }

    // 2d array
    int twoDArray[][3] = {{1,2,3}, {4,5,6}};
    cout << sizeof(twoDArray[0])/sizeof(twoDArray[0][0]) << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << twoDArray[i][j] << " ";
        }
        cout << endl;
    }
    
    // output total score for each student
    int grades [][3] = {{100, 100, 100}, {90, 50, 100}, {60, 70, 80}};
    int stu1 = 0, stu2 = 0, stu3 = 0;
    for (int i = 0; i < sizeof(grades)/sizeof(grades[0]); i++) {
        int sum = 0;
        for (int j = 0; j < sizeof(grades[0])/sizeof(grades[0][0]); j++) {
            sum += grades[i][j];
        }
        cout << sum << endl;
    }

    // function
    cout << add(1,2) << endl;
    return 0;
}