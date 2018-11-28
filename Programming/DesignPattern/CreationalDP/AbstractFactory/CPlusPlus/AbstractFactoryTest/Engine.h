#pragma once
#include "Header.h"

class Engine
{
protected:
	char _sound[15];
public:
	Engine();
	~Engine();
	virtual void run() = 0;
};

