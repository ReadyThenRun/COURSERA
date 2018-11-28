#pragma once
#include "Header.h"


class ElectricCarFactory :
	public CarFactory
{
public:
	ElectricCarFactory();
	~ElectricCarFactory();
	Door * BuildDoor();
	Engine * BuildEngine();
};

