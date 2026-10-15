#include <iostream>
#include <vector>

using namespace std;

// Función para mostrar un arreglo en pantalla
void mostrarArreglo(const vector<int>& arr) {
    cout << "[ ";
    for (int val : arr) {
        cout << val << " ";
    }
    cout << "]\n";
}

// 1. Suma de 2 arreglos guardada en un tercero
vector<int> sumarArreglos(const vector<int>& a, const vector<int>& b) {
    int n = a.size();
    vector<int> resultado(n);
    
    for (int i = 0; i < n; i++) {
        resultado[i] = a[i] + b[i];
    }
    return resultado;
}

// 2. Multiplica elemento por elemento y suma todos los resultados (Producto punto)
int multiplicarYSumar(const vector<int>& a, const vector<int>& b) {
    int sumaTotal = 0;
    
    for (size_t i = 0; i < a.size(); i++) {
        sumaTotal += (a[i] * b[i]);
    }
    return sumaTotal;
}

int main() {
    int tamano;

    cout << "=== OPERACIONES CON ARREGLOS ===\n\n";
    cout << "Ingresa el tamaño de los arreglos: ";
    cin >> tamano;

    vector<int> arreglo1(tamano);
    vector<int> arreglo2(tamano);

    // Llenado del primer arreglo
    cout << "\n--- Llenando Arreglo 1 ---\n";
    for (int i = 0; i < tamano; i++) {
        cout << "Elemento [" << i << "]: ";
        cin >> arreglo1[i];
    }

    // Llenado del segundo arreglo
    cout << "\n--- Llenando Arreglo 2 ---\n";
    for (int i = 0; i < tamano; i++) {
        cout << "Elemento [" << i << "]: ";
        cin >> arreglo2[i];
    }

    // --- OPERACIÓN 1: SUMA ---
    vector<int> arregloSuma = sumarArreglos(arreglo1, arreglo2);

    // --- OPERACIÓN 2: MULTIPLICAR Y SUMAR ---
    int acumuladoMultiplicacion = multiplicarYSumar(arreglo1, arreglo2);

    // --- MOSTRAR RESULTADOS ---
    cout << "\n================ RESULTADOS ================\n";
    cout << "Arreglo 1:           "; mostrarArreglo(arreglo1);
    cout << "Arreglo 2:           "; mostrarArreglo(arreglo2);
    cout << "Suma (Arreglo 3):    "; mostrarArreglo(arregloSuma);
    cout << "Suma de productos:   " << acumuladoMultiplicacion << "\n";

    return 0;
}