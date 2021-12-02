// Oleksandr Tkachenko
// Problem 2

#include <iostream> 
#include <stdlib.h> // getenv call
#include <sys/sysinfo.h> // system uptime call
#include <cgicc/Cgicc.h> // the cgicc headers
#include <cgicc/CgiDefs.h>
#include <cgicc/HTTPHTMLHeader.h>
#include <cgicc/HTMLClasses.h>
#include <string>
#include "GPIO.h"

using namespace std;
using namespace cgicc;
using namespace exploringBB;


int main(){
    Cgicc form;

    GPIO button(46);

    cout << HTTPHTMLHeader() << endl;   // Generate the HTML form
    cout << html() << head() << title("Homework 10 problem 2") << head() << endl;
    cout << h1("Reading Pushbutton From Beaglebone Black") << "<br>" << h2("Reading GPIO46") << endl;
      
    cout << "<form action =\"/cgi-bin/read_button.cgi\" method =\"POST\">\n";
    cout << "<div> <input type = \"Submit\" value =\"Read Button\" />";
    cout << "</div></form>";

    cout << body() << h1("Pushbutton State") << endl;
   // if (button.read(BUTTON_GPIO,"value") == "1")
    if (button.getValue()){
        cout << h1("Button Not Pressed");
        cout << button.getValue();
}
    else{
        cout << h1("Button Pressed");
        cout << button.getValue();
}
    cout << body() << html();

}
