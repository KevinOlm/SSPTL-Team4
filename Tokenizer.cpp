#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

using namespace std;

bool palabraReservada(char []);
bool operadorRelacional(string);

int main(){

    char ch, operador[]="*+-/%=", palabra[15];
    int j = 0;
	string concat = "";
	//agregamos la magia de abrir archivos
    ifstream codigo;
	//Creamos el archivo
    codigo.open("codigo.txt");
	//If por si falla el archivo
    if(codigo.fail()){
        cout<<"Error al abrir archivo";
        exit(1);
    }else{
        //Mientras no termine de scanear el archivo, guarda el valor en ch
        while(!codigo.eof()){

            ch = codigo.get();
			//Aquí comparamos el arreglo de operador con el caracter para saber si pertenece o no e imprime cosas
            for(int i=0; i<=5;i++){
                if(ch==operador[i]){
                    cout<<ch<<"-> es un operador"<<endl;
                }
            }
            switch(ch)
            {
            	case '(':
            		cout<<ch<<"-> abre parentesis"<<endl;
            		continue;
            	case ')':
            		cout<<ch<<"-> cierra parentesis"<<endl;
            		continue;
				case '{':
            		cout<<ch<<"-> abre llaves"<<endl;
					continue;
				case '}':
            		cout<<ch<<"-> cierra llaves"<<endl;
            		continue;
            	case '[':
            		cout<<ch<<"-> abre corchete"<<endl;
					continue;
				case ']':
            		cout<<ch<<"-> cierra corchete"<<endl;
            		continue;
            	case ',':
            		cout<<ch<<"-> coma"<<endl;
            		continue;
				case ';':
            		cout<<ch<<"-> fin de la sentencia"<<endl;
					continue;      	
			}
			//isalnum checa que sean caracteres alfa numericos
            if(isalnum(ch)){
                palabra[j++] = ch;
            }else if(j>0){
                
				if(j!=0){
					palabra[j]='\0';
                	j = 0;
					if(palabraReservada(palabra)){
                    cout<<palabra<<"-> es una palabra reservada"<<endl;
                	}else{
                    cout<<palabra<<"-> es un identificador"<<endl;
                	}
				}
				if(concat.size()>0&&operadorRelacional(concat))
				{
					cout<<concat<<"-> es un operador relacional"<<endl;
				}
                concat = "";
            }
            else if(ch=='<'||ch=='>'||ch=='='||ch=='!'){
            	concat += ch;
			}
        	//cout<<concat<<endl;
        }

        codigo.close();
    }




    return 0;
}


bool palabraReservada(char palabra[]){
    char keywords[26][10] = {"main","int","if","else","while","return",
							"float", "bool","for","switch","break","case","default","true","false","long",
							"double","delete","try","catch","void","char","goto","new","sizeof","short"};
    bool bandera = false;
  
    for(int i=0; i<26; i++){
        
        if(strcmp(keywords[i],palabra)== 0){
           return true;
           bandera = true;
           break;
        }
        
    }

    return bandera;
}

bool operadorRelacional(string palabra){
    string operador[] = {"<",">","<=",">=","==","!="};
    bool bandera = false;
  
    for(int i=0; i<6; i++){
        
        if(operador[i].compare(palabra) == 0){
           bandera = true;
           break;
        }
        
    }

    return bandera;
}
