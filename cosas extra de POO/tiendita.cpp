#include <iostream>
#include <string>

using namespace std;

int main() {
    // Declaramos los dos arreglos para 15 elementos
    string PRODUCTS[15];
    double PRICES[15];

    // 1. LECTURA DE DATOS
    cout << "--- INGRESO DE DATOS ---\n";
    for (int i = 0; i < 15; i++) {
        cout << "Ingrese el producto " << i + 1 << ": ";
        cin >> PRODUCTS[i];

        cout << "Ingrese el precio de " << PRODUCTS[i] << ": $";
        cin >> PRICES[i];
        cout << "------------------------\n";
    }

    // 2. MOSTRAR RESULTADOS
    cout << "\n--- LISTA DE PRODUCTOS Y PRECIOS ---\n";
    for (int i = 0; i < 15; i++) {
        cout << i + 1 << ". " << PRODUCTS[i] << " - $" << PRICES[i] << endl;
    }

    return 0;
}