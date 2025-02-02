#include <iostream> 

using namespace std;

int main() {
    double a, b;
    char op;

    cout << "Пиши: ";
    cin >> a >> op >> b;

    if (op == '+') cout << a + b;
    else if (op == '-') cout << a - b;
    else if (op == '*') cout << a * b;
    else if (op == '/' && b != 0) cout << a / b;
    else cout << "Такого нету";

    return 0;
}
