#include "Header.h"
using namespace std;

GasCarFactory::GasCarFactory()
{
}

GasCarFactory::~GasCarFactory()
{
}

Door * GasCarFactory::BuildDoor() {
	return new GasCarDoor();
}

Engine * GasCarFactory::BuildEngine() {
	return new GasCarEngine();
}