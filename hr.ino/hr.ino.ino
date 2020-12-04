
#include <SoftwareSerial.h>
SoftwareSerial ESPserial(2, 3); //Wifi RX | TX
//Variables globales se guardan en datos
int hrBuffer;
String dataToSend;
int sensorHR;
long milis;
char data[100];
String command;
String response;
//subimos el codigo se corre primero el setup
void setup() {
  Serial.begin(9600); // initialize serial communication at 115200 bits per second:
  dataToSend.reserve(100);
  sensorHR=0;
  command.reserve(300);
  response.reserve(200);
  ESPserial.begin(9600);
  Serial.println("Setting up client mode");
  sendCommand("AT+CWMODE=1\r\n", 1000); 
  sendCommand2("AT+CWJAP=\"renunezswn\",\"1230984567\"\r\n", 4000,1); 
  delay(20000);
  sendCommand2("AT+CIPSTART=\"UDP\",\"10.0.1.14\",1337\r\n", 2000, 1);
  delay(1000);
 
}


void loop() {
   hrBuffer = analogRead(sensorHR);
   milis=millis();
   dataToSend="HR:";
   dataToSend+=hrBuffer;
   dataToSend+=";ML:";
   dataToSend+=milis;
   //Serial.println(dataToSend);  
   dataToSend+=";\r\n";
   command="AT+CIPSEND=";
   command+=dataToSend.length();
   command+="\r\n";
   sendCommand(command, 50);
   sendData(50);
}

void sendData(const int timeout)
{
  while ( ESPserial.available() ) {
    Serial.write( ESPserial.read());
    delay(1000);
  }
  response = "";
  int dataSize = dataToSend.length();
  dataToSend.toCharArray(data,dataSize);
  ESPserial.write(data,dataSize); // 
  long int time = millis();
  while( (time+timeout) > millis())
  {
  while(ESPserial.available())
  {
  // The esp has data so display its output to the serial window
  char c = ESPserial.read(); // read the next character.
  response+=c;
  }
  }
  Serial.print(response);
  //return response;
}

void sendCommand(String command, const int timeout)
{
  while ( ESPserial.available() ) {
    Serial.write( ESPserial.read());
    delay(100);
  }
  response="";
  ESPserial.print(command); // send the read character to the wifi
  long int time = millis();
  while( (time+timeout) > millis())
  {
  while(ESPserial.available())
  {
  // The esp has data so display its output to the serial window
  char c = ESPserial.read(); // read the next character.
  response+=c;
  }
  }
  Serial.print(response);
  //return response;
} 
void sendCommand2(String command, const int timeout, int times)
{
  response="";
  ESPserial.print(command); // send the read character to the wifi
  int i=0;
  while(i<times){
    long int time = millis();
    while( (time+timeout) > millis())
    {
    while(ESPserial.available())
    {
    // The esp has data so display its output to the serial window
    char c = ESPserial.read(); // read the next character.
    response+=c;
    }
    }
    Serial.print(response);
    i+=1;
  }

  //return response;
} 
