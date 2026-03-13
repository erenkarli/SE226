#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}

int findMax(int* arr, int size) {
    int max = *arr;
    for (int i = 1; i < size; i++) {
        if (*(arr + i) > max) {
            max = *(arr + i);
        }
    }
    return max;
}

void reverseArray(int* arr, int size) {
    int* left = arr;
    int* right = arr + size - 1;
    while (left < right) {
        swapValues(left, right);
        left++;
        right--;
    }
}

int* createArray(int n) {
    return new int[n];
}

void deleteArray(int* arr) {
    delete[] arr;
    cout << "Memory released successfully." << endl;
}

int main() {
    int n;
    cout << "Creating dynamic array..." << endl;
    cout << "Enter array size: ";
    cin >> n;

    int* arr = createArray(n);

    cout << "Enter values: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Array elements:" << endl;
    printArray(arr, n);
    cout << "Maximum element: " << findMax(arr, n) << endl;

    cout << "----------------------------------" << endl;
    cout << "Swapping two numbers" << endl;
    int a = 5, b = 8;
    cout << "Before swap\na = " << a << "\nb = " << b << endl;
    swapValues(&a, &b);
    cout << "After swap\na = " << a << "\nb = " << b << endl;

    cout << "----------------------------------" << endl;
    cout << "Reversing array..." << endl;
    reverseArray(arr, n);
    cout << "Array after reverseArray:" << endl;
    printArray(arr, n);

    cout << "----------------------------------" << endl;
    cout << "Deleting array..." << endl;
    deleteArray(arr);

    return 0;
}