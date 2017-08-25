final int screenWidth = 200;
final int screenHeight = 200;
void initialize () {
	addScreen("mylevel", new MyLevel(screenWidth, screenHeight));
}

class MyLevel extends Level {
	MyLevel(float LevelWidth, float LevelHeight) {
	super(levelWidth, levelHeight)
	}
}


void setup()
{
	size(500,500);
	background(100);
}

void draw() 
{
	
}

