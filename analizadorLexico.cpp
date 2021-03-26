#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

using namespace std;

bool palabraReservada(char []);

int main(){

    char ch;
	char operador[] = "*+-/%";
	char palabra[15];
	char uchar[] = "()[]{},;";
	char oprel[6][3] = {">", "<", ">=", "<=", "==", "!="};
    int j = 0;

    ifstream codigo;

    codigo.open("codigo.txt");

    if(codigo.fail()) {
        cout<<"Error al abrir archivo";
        exit(1);
    }
	else {
        
        while(!codigo.eof()) {

            ch = codigo.get();

            for(int i=0; i<5; i++) {
                if(ch==operador[i]) cout<<ch<<"-> es un operador"<<endl;
            }
            
            for(int i=0; i<8; i++) {
                if(ch==uchar[i]) cout<<ch<<"-> es un caracter especial"<<endl;
            }
            
            if((ch != ' ' && ch != '\n' && ch!='\t')) palabra[j++] = ch;
            else if (j!=0){
            	bool oprel_verifier = false;
            	
                palabra[j]='\0';
                j = 0;
                
                for(int i=0; i<6; i++){
			        if(strcmp(oprel[i],palabra)== 0) {
			        	cout<<palabra<<"-> es una operador relacional"<<endl;
			        	oprel_verifier = true;
					}
			    }
			    
			    if (!oprel_verifier){
					if(palabraReservada(palabra)) cout<<palabra<<"-> es una palabra reservada"<<endl;
	                else if(isalpha(palabra[0])) cout<<palabra<<"-> es un identificador"<<endl;	
				}
            }
        }
        codigo.close();
    }
    return 0;
}

bool palabraReservada(char palabra[]){
    char keywords[26][10] = {
		"main","int","if","else","while","return",
		"float", "bool", "double", "long", "char",
		"string", "for", "foreach", "true", "false",
		"break", "switch", "case", "include", "import",
		"do", "exit", "short", "byte", "print"
	};
  
    for(int i=0; i<26; i++){
        if(strcmp(keywords[i],palabra)== 0) return true;
    }
    return false;
}