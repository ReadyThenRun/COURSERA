#include "Header.h"
using namespace std;


ElectricCarFactory::ElectricCarFactory()
{
}


ElectricCarFactory::~ElectricCarFactory()
{
}


Door * ElectricCarFactory::BuildDoor() {
	return new ElectricCarDoor();
};
Engine * ElectricCarFactory::BuildEngine() {
	return new ElectricCarEngine();
};