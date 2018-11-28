#pragma once
#include "Header.h"

class CarFactory
{
public:
	CarFactory();
	~CarFactory();
	virtual Door * BuildDoor() = 0;
	virtual Engine * BuildEngine() = 0;
};

