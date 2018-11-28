#include "Header.h"
using namespace std;

GasCarEngine::GasCarEngine()
{
	strcpy_s(_sound, "vroom");
	cout << "Making a gas Engine." << endl;
}


GasCarEngine::~GasCarEngine()
{
}

void GasCarEngine::run() {
	cout << "Sound like a Gas car running: " << _sound << " ..." << endl;
}