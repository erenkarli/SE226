#include <iostream>

using namespace std;

double get_gn_recursive(int n, double r) {
    if (n == 0) {
        return 1.0;
    }

    double term = 1.0;
    for(int i = 0; i < n; i++) {
        term *= r;
    }

    return term + get_gn_recursive(n - 1, r);
}

int main() {
    int n;
    double r;

    cout << "n: ";
    cin >> n;
    cout << "r: ";
    cin >> r;

    cout << get_gn_recursive(n, r) << endl;

    return 0;
}