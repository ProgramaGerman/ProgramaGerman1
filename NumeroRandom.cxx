#include <iostream>
#include <vector>
#include <algorithm> // Para std::shuffle
#include <random>    // Para std::default_random_engine
#include <ctime>     // Para std::time

using namespace std;

int main() {
    // Inicializa la semilla para el generador de números aleatorios
    srand(static_cast<unsigned int>(time(0)));

    // Vector para almacenar los números del 1 al 5
    vector<int> numbers = {1, 2, 3, 4, 5};

    // Crea un generador de números aleatorios
    default_random_engine engine(static_cast<unsigned int>(time(0)));
    
    // Mezcla los números aleatorios
    shuffle(numbers.begin(), numbers.end(), engine);

    // Muestra los números en orden aleatorio
    for (int number : numbers) {
        cout << number << endl;
    }

    return 0;
}