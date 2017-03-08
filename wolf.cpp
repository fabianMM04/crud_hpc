#include <iostream>
#include <stdlib.h>

using namespace std;

void LLenar(int, int,int Matriz[4][5]);///Funcion encargada de llenar vecindad
void Recorrer(int, int,int Matriz[4][5]);///Funcion encargada de recorrer la matriz

int L=1;///L guardara el valor que se insertara
int Temp;///Temp almacenara el numero de valores modificados en la tabla

int main()
{


    int Matriz[4][5]= { {0,0,0,0,0},
        {0,0,-1,-1,0},
        {0,0,0,-1,0},
        {0,0,0,-1,0}
    };
    cout<<"--------------------------------------"<<endl;
///Imprimir

    for (int i=0; i<4; i++)
    {
        for (int j=0; j<5; j++)
            cout<<"  "<<" "<<Matriz[i][j]<<",";
        cout<<endl;

    }
///--------------------------------------------------------------------------
    int A,B,C,D;///Coordenadas A & D=columna, B & C=fila

    cout<<"--------------------------------------"<<endl;
    cout<<"Ingrese las coordenadas del estado final"<<endl;
    cout<<"Ingrese la fila:";
    cin>>B;
    cout<<"Ingrese la Columna:";
    cin>>A;


    for (int i=0; i<4; i++)/// Hasta fila 4
    {

        for (int j=0; j<5; j++)///hasta columna 5
        {
            if(i==B and j==A )///Si la posicion actual es igual a la ingresada
            {
                if(Matriz[i][j]==-1 )///Si nuestra posicion contiene el valor -1 entonces es un obstaculo
                {
                    cout<<"--------------------------------------"<<endl;
                    cout<<"¡Esta posicion pertenece a un obstaculo!"<<endl;
                    cout<<"--------------------------------------"<<endl;
                    exit(0);
                }
                else
                {
                    Matriz[i][j]=L;///Si no lo es rellenar con 1

                }

            }

        }
    }



    LLenar(A,B, Matriz);///LLamamos a la funcion para llenar la vencidad LLenar(Fila, Columna, Matriz)

///--------------------------------------------------------------------------

    for( int p=0; p<Temp; p++)///Hasta numero de veces que se ingreso un valor en matriz
    {

        for (int i=0; i<4; i++)
        {
            for (int j=0; j<5; j++)

                if(Matriz[i][j]==L  )///Si nuestra posicion actual fue el valor antes modificado
                {
                    LLenar(j,i,Matriz);///llenamos vencindad respecto a esta nueva posicion
                    L--;///Disminuimos L ya que en la llamda a llenar este aumenta y L puede estar en la matriz mas de una vez
                }

        }
        L++;///Al finalizar el recorrido reestablecemos L a su valor original de modificacion

    }
///--------------------------------------------------------------------------
 cout<<"--------------------------------------"<<endl;
///Imprimir

    for (int i=0; i<4; i++)
    {

        for (int j=0; j<5; j++)
            cout<<"  "<<" "<<Matriz[i][j]<<",";
        cout<<endl;

    }


    cout<<"--------------------------------------"<<endl;
    cout<<"Ingrese las coordenadas del estado inicial"<<endl;
    cout<<"Ingrese la fila :";
    cin>>D;
    cout<<"Ingrese la Columna :";
    cin>>C;
    cout<<"----------------------------------"<<endl;

    cout<<"Recorrido"<<endl;
    cout<<"----------------------------------"<<endl;

    cout<<Matriz[D][C]<<"["<<D<<"]"<<"["<<C<<"]"<<endl;///Imprimimos la posicion actual seleccionada
    Recorrer(D, C, Matriz);///llamamos a la funcion Recorrer y enviamos como parametros las coordenadas y la matriz

///--------------------------------------------------------------------------
    return 0;

}



///Funcion llenar vencindad
void LLenar(int A, int B, int Matriz[4][5])
{
    L++;///Como su valor inicial es 1 este debe aumentar en una unidad para llenar la vencindad

    for (int i=0; i<4; i++)
    {

        for (int j=0; j<5; j++)

        {
            ///Llenar celda de arriba respecto a nuestra ubicacion actual
            if(i==(B-1) and j==A and Matriz[i][j]!=-1  and Matriz[i][j]==0 )/// se llenara si y solo si, "i" sea igual a la columna de nuestra posicion actual menos 1,
                /// si no estamos ubicados en un obstaculo y finalmente si  nuestra posicion actual es 0
                /// y es modificable
            {
                Matriz[i][j]=  L;///llenamos la posicion actual con el valor de L
                Temp++;///Aumentamos en una unidad ya que se ha insertado un valor  en la matriz

            }
            ///Llenar celda de abajo respecto a nuestra ubicacion actual
            if(i==(B+1) and j==A and Matriz[i][j]!=-1 and Matriz[i][j]==0  )/// se llenara si y solo si, "i" sea igual a la columna de nuestra posicion actual mas 1,
                /// si no estamos ubicados en un obstaculo y finalmente si  nuestra posicion actual es 0
                /// y es modificable
            {
                Matriz[i][j]=L;///llenamos la posicion actual con el valor de L
                Temp++;///Aumentamos en una unidad ya que se ha insertado un valor  en la matriz
            }
            ///Llenar celda de la izquierda respecto a nuestra ubicacion actual
            if(i==B and j==(A-1) and Matriz[i][j]!=-1  and Matriz[i][j]==0 )/// se llenara si y solo si, "j" sea igual a la fila de nuestra posicion actual menos 1,
                /// si no estamos ubicados en un obstaculo y finalmente si  nuestra posicion actual es 0
                /// y es modificable
            {
                Matriz[i][j]=L;///llenamos la posicion actual con el valor de L
                Temp++;///Aumentamos en una unidad ya que se ha insertado un valor  en la matriz
            }
            if(i==B and j==(A+1) and Matriz[i][j]!=-1  and Matriz[i][j]==0  )/// se llenara si y solo si, "j" sea igual a la fila de nuestra posicion actual mas 1,
                /// si no estamos ubicados en un obstaculo y finalmente si  nuestra posicion actual es 0
                /// y es modificable
            {
                Matriz[i][j]=L;///llenamos la posicion actual con el valor de L
                Temp++;///Aumentamos en una unidad ya que se ha insertado un valor  en la matriz
            }

        }

    }





}




void Recorrer(int C, int D, int  Matriz[4][5])
{

    int VOptimo1=0,VOptimo2=0,VOptimo3=0,VOptimo4=0;///valores que almacenaran diferencia entre el valor de la posicion actual y su vencindad


    for (int i=0; i<4; i++)
    {

        for (int j=0; j<5; j++)
        {


            if(i==C and j==D and Matriz[i][j]!=-1)///Nos ubicamos en la posicion ingresada y comprobamos que esta no sea un obstaculo
            {

                if(Matriz[i-1][j]!=-1)///mientras el valor de la posicion arriba respecto a la actual sea diferente de -1
                {
                    VOptimo1= Matriz[i][j]- Matriz[i-1][j];///VOptimo1 sera igual a la diferencia de nuestra posicion actual y el valor de la posicion de arriba
                }

                if(Matriz[i+1][j]!=-1)///mientras el valor de la posicion abajo respecto a la actual sea diferente de -1
                {
                    VOptimo2=Matriz[i][j]- Matriz[i+1][j];///VOptimo2 sera igual a la diferencia de nuestra posicion actual y el valor de la posicion de abajo
                }

                if(Matriz[i][j-1]!=-1)///mientras el valor de la posicion izquierda respecto a la actual sea diferente de -1
                {
                    VOptimo3=Matriz[i][j]- Matriz[i][j-1];///VOptimo3 sera igual a la diferencia de nuestra posicion actual y el valor de la posicion de izquierda
                }
                if(Matriz[i][j+1]!=-1)///mientras el valor de la posicion derecha respecto a la actual sea diferente de -1
                {
                    VOptimo4=Matriz[i][j]- Matriz[i][j+1];///VOptimo4 sera igual a la diferencia de nuestra posicion actual y el valor de la posicion de derecha
                }



                ///Comprobamos si la diferencia entre la vecindad el valor de nuestra posicion actual es 1

                if(VOptimo1==1)///si el valor de VOptimo1(diferencia de estado actual y arriba) es identico a 1
                {
                    cout<<Matriz[i-1][j]<<"["<<i-1<<"]"<<"["<<j<<"]"<<endl;///Imprimimos el valor de arriba y sus coordenadas
                    ///Si se cumplio la condicion significa que la funcion se llamara asi misma, por lo tanto la posicion actual cambiara, esto
                    ///nos obliga a convertir en 0 las diferencias entre el el valor actual y su vencindad
                    VOptimo1=0;
                    VOptimo2=0;
                    VOptimo3=0;
                    VOptimo4=0;

                    if(Matriz[i][j]!=1)///Mientras nuestra posicion actual sea diferente de 1, podemos seguir
                    {
                        Recorrer(i-1,j,Matriz);/// si la diferencia entre actual y arriba fue 1 entonces  se llamara a recorrer pero esta vez con las coordenadas de la
                        ///posicion de arriba
                    }


                }
                if(VOptimo2==1)///si el valor de VOptimo2 es identico a 1
                {
                    cout<<Matriz[i+1][j]<<"["<<i+1<<"]"<<"["<<j<<"]"<<endl;///Imprimimos el valor de abajo y sus coordenadas
                    ///Si se cumplio la condicion significa que la funcion se llamara asi misma, por lo tanto la posicion actual cambiara, esto
                    ///nos obliga a convertir en 0 las diferencias entre el el valor actual y su vencindad
                    VOptimo1=0;
                    VOptimo2=0;
                    VOptimo3=0;
                    VOptimo4=0;
                    if(Matriz[i][j]!=1)///Mientras nuestra posicion actual sea diferente de 1, podemos seguir
                    {
                        Recorrer(i+1,j,Matriz);/// si la diferencia entre actual y abajo fue 1 entonces  se llamara a recorrer pero esta vez con las coordenadas de la
                        ///posicion de abajo
                    }


                }
                if(VOptimo3==1)
                {
                    cout<<Matriz[i][j-1]<<"["<<i<<"]"<<"["<<j-1<<"]"<<endl;///Imprimimos el valor de izquierda y sus coordenadas
                    ///Si se cumplio la condicion significa que la funcion se llamara asi misma, por lo tanto la posicion actual cambiara, esto
                    ///nos obliga a convertir en 0 las diferencias entre el el valor actual y su vencindad
                    VOptimo1=0;
                    VOptimo2=0;
                    VOptimo3=0;
                    VOptimo4=0;
                    if(Matriz[i][j]!=1)///Mientras nuestra posicion actual sea diferente de 1, podemos seguir
                    {
                        Recorrer(i,j-1,Matriz);/// si la diferencia entre actual y izquierda fue 1 entonces  se llamara a recorrer pero esta vez con las coordenadas de la
                        ///posicion de izquierda
                    }

                }

                if(VOptimo4==1)
                {
                    cout<<Matriz[i][j+1]<<"["<<i<<"]"<<"["<<j+1<<"]"<<endl;///Imprimimos el valor de derecha y sus coordenadas
                    ///Si se cumplio la condicion significa que la funcion se llamara asi misma, por lo tanto la posicion actual cambiara, esto
                    ///nos obliga a convertir en 0 las diferencias entre el el valor actual y su vencindad
                    VOptimo1=0;
                    VOptimo2=0;
                    VOptimo3=0;
                    VOptimo4=0;
                    if(Matriz[i][j]!=1)///Mientras nuestra posicion actual sea diferente de 1, podemos seguir
                    {
                        Recorrer(i,j+1,Matriz);/// si la diferencia entre actual y derecha fue 1 entonces  se llamara a recorrer pero esta vez con las coordenadas de la
                        ///posicion de derecha
                    }
                }



            }

        }

    }
}
