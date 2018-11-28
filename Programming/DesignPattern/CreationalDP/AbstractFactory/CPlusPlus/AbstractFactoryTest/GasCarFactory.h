#pragma once
#include "Header.h"

class GasCarFactory :
	public CarFactory
{
public:
	GasCarFactory();
	~GasCarFactory();
	Door * BuildDoor();
	Engine * BuildEngine();
};

