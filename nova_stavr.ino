// C++ code
//
unsigned napon_mV = 3750;
unsigned int kapacitet_mAh = 2600;
float napon_V;
float kapacitet_Ah;
unsigned long ukupna_energija;
void setup()
{
  Serial.begin(9600);
  ukupna_energija = (unsigned long)napon_mV * kapacitet_mAh;
  
  Serial.print("Ukupna energija");
  Serial.println(ukupna_energija);
  
  naponV = (float)napon_mV/ 1000);
  
  
  Serial.prtint("Ukupna energija:");
  Serial.println(ukupna energija);
  
  Serial.prtint("Napon u V:   ");
  Serial.println(naponV);
  
  Serial.prtint("kapacitet u V:   ");
  Serial.println(kapacitet u mAH);
  
  
  
  
  
}

void loop()
{
  
  
  
  
  
 
}
