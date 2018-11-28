#include "Header.h"
using namespace std;

int main(int argc, char ** argv) {
	CarFactory* CarPlant;
	int choice;

	cout << "Select a car type: " << endl;
	cout << "1: Gasoline" << endl;
	cout << "2: Electric" << endl;
	cout << "Selection: ";
	cin >> choice;
	cout << endl;

	switch (choice)
	{
	case 1:
		CarPlant = new GasCarFactory;
		break;
	case 2:
		CarPlant = new ElectricCarFactory;
		break;
	default:
		cout << "Invalid Selection" << endl;
		CarPlant = NULL;
		break;
	}

	if (CarPlant != NULL)
	{
		Door* myDoor = CarPlant->BuildDoor();
		Engine* myEngine = CarPlant->BuildEngine();

		myDoor->open();
		myEngine->run();
	}
	system("pause");
	return 0;
}

