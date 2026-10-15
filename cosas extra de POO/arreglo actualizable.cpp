#include <iostream>
#include <string>

using namespace std;

int main() {
    string PRODUCTS[15];
    double PRICES[15];
    int cantidad = 0;
    int opcion;

    do {
        cout << "\n1. Agregar\n2. Eliminar\n3. Mostrar\n4. Salir\nOpcion: ";
        cin >> opcion;

        if (opcion == 1) {
            if (cantidad < 15) {
                cout << "Producto: ";
                cin >> PRODUCTS[cantidad];
                cout << "Precio: ";
                cin >> PRICES[cantidad];
                cantidad++;

                // Ordenar
                for (int i = 0; i < cantidad - 1; i++) {
                    for (int j = 0; j < cantidad - i - 1; j++) {
                        if (PRODUCTS[j] > PRODUCTS[j + 1]) {
                            string tempProd = PRODUCTS[j];
                            PRODUCTS[j] = PRODUCTS[j + 1];
                            PRODUCTS[j + 1] = tempProd;

                            double tempPrec = PRICES[j];
                            PRICES[j] = PRICES[j + 1];
                            PRICES[j + 1] = tempPrec;
                        }
                    }
                }
            }
        } 
        else if (opcion == 2) {
            if (cantidad > 0) {
                int pos;
                for (int i = 0; i < cantidad; i++) {
                    cout << i + 1 << ". " << PRODUCTS[i] << "\n";
                }
                cout << "Numero a eliminar: ";
                cin >> pos;

                if (pos >= 1 && pos <= cantidad) {
                    for (int i = pos - 1; i < cantidad - 1; i++) {
                        PRODUCTS[i] = PRODUCTS[i + 1];
                        PRICES[i] = PRICES[i + 1];
                    }
                    cantidad--;
                }
            }
        } 
        else if (opcion == 3) {
            for (int i = 0; i < cantidad; i++) {
                cout << i + 1 << ". " << PRODUCTS[i] << " - $" << PRICES[i] << "\n";
            }
        }

    } while (opcion != 4);

    return 0;
}