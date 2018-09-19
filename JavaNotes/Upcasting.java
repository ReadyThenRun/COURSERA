public class Upcasting {
	  public static void main (String args[])
	   {
	      Fish f = new Fish();
	      // Upcasting by interface
	      Runner runnerFish = new Fish();
	      System.out.println("upcasting can run on a class of which father class is an interface");
	      ((Fish)runnerFish).breathe();
	      System.out.println();
	   }

}

interface Runner
{
  int ID = 1;
  void run();
}


interface Animal extends Runner
{
  void breathe();
}

class Fish implements Animal
{
	public void run ()
	{
	   System.out.println("fish is swimming");
	}
	
  	@Override
	public void breathe(){
	   System.out.println("fish is bubbing");   
	}
}

abstract class LandAnimal implements Animal
{
	public void breathe ()
	{
	   System.out.println("LandAnimal is breathing");
	}
}


interface Flyer
{
	void fly ();
}
class Bird implements Runner , Flyer
{
	public void run ()
	{
       System.out.println("the bird is running");
	}
	public void fly ()
  	{
       System.out.println("the bird is flying");
  	}
}
