#include "Header.h"
using namespace std;


ElectricCarEngine::ElectricCarEngine()
{
	strcpy_s(_sound, "SHHHH");
	cout << "Makine a Electric engine." << endl;
}


ElectricCarEngine::~ElectricCarEngine()
{
}

void ElectricCarEngine::run() {
	cout << "Sound like a Electric car is running: " << _sound << "..." <<endl;
}