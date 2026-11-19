unsigned long otpornik = 100000;
float kapacitet = 47e-6;
float tau;
float vrijemepunjenja;

void setup()
{
  Serial.begin (9600);
  tau = otpornik * kapacitet;
  
  Serial.println(tau, 3);
  vrijemepunjenja = (5* tau);
  Serial.print("vrijeme punjenja");
  Serial.println(vrijemepunjenja);
  

  
  
  
  
  
}

void loop()
{
  
  
  
  
  
 
}
