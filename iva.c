/*
 *Autor: Oscar Enrique González Escurra
 *Asunción-Paraguay
 *2018
 *
 */

#include<stdlib.h>
#include <stdio.h>
#define IVA10 0
#define IVA5 1
#define EXENTA 2
#define TRUE 100
#define FALSE -1
//FUNCIONES
int calculo10(short int *);
int calculo5(short int * );
int exenta(short int * );
void cerar();
void imprimetotales();
int borrar(short int *, short int *, short int *);
void imprimeresultados();
void ultimos_ingresados();

//Variables globales
int iva[3];
int iva_r[3];
int ultimos[5][3];
/*
 *PROGRAMA PRINCIPAL
 */
int main(){
	short int opcion;
	short int borra;
	short int ultimo_iva10=0;
	short int ultimo_iva5=0;
	short int ultimo_exenta=0;
	int valor_borrado;
	cerar();
	do{
		printf("\n...::BIENVENIDO AL MANEJADOR DE IVA PARA PEQUEÑOS CONTRIBUYENTES::..\n1-Carga Monto de IVA 10%\n");
		printf("2-Carga Monto de IVA 5%\n3-Carga Monto exentas\n");
		printf("4-Imprimir 5 últimos cargados de cada opción\n5-Eliminar valor\n6-Mostrar resultado para declaración\n0-SALIR\n::");
		scanf("%d", &opcion);
		switch(opcion){
			case 1:
				calculo10(&ultimo_iva10);	
				//printf("\nEstan cargados %d",ultimo_iva10);

				break;
			case 2:
				calculo5(&ultimo_iva5);

				break;
			case 3:
				exenta(&ultimo_exenta);

				break;
			case 4:
				ultimos_ingresados();	
				break;

			case 5:
				
				valor_borrado=borrar(&ultimo_iva10, &ultimo_iva5, &ultimo_exenta );	
				
				printf("\nSe borro %d\n",valor_borrado);

				break;
			case 6:
				//Aca se calcula todo
					
				imprimetotales();
				puts("\n");
				printf("\n A continuación se imprimirán los montos que se tendrá que ingresar en la declaración del formulario 120 del sistema Marangatu");
				imprimeresultados();	
				break;

			case 0:
				//Sale del while
				break;
			default:
				printf("\nERROR:Opcion no válida\n");
		}
	}while(opcion!=0);
	
	return 1;
}

//Simplemente imprime los últimos datos ingresados en las 3 categorías (se guardaron en otras funciones)
void ultimos_ingresados(){
	int i,j;
	printf("\nUltimos 5 datos ingresados de cada categoría\n\tIVA 10%\tIVA 5%\tEXENTAS");
	for(i=0;i<5;i++){
		printf("\n");
		for(j=0;j<EXENTA+1;j++){
			printf("\t%d",ultimos[i][j]);
		}
	}
}



/*
 *En esta función se calcula el monto de las gravadas 10% y 5% de todas las facturas cargadas y se calculo el monto a ingresar en el formulario 120 del 
 *sistema Marangatu 
 *Parametros:
 *-
 *Retorno:
 *-
 *
 */
void imprimeresultados(){
	
	short int i;

	iva_r[IVA10]=iva[IVA10]*11-iva[IVA10];
	
	iva_r[IVA5]=iva[IVA5]*21-iva[IVA5];

	iva_r[EXENTA]=iva[EXENTA];
	
	printf("\n\tGravadas 10% \tGravadas 5% \tEXENTAS\n");
	printf("\t%d", iva_r[IVA10]);
	printf("\t\t%d", iva_r [IVA5]);
	printf("\t\t%d", iva_r[EXENTA]);

}


//Simplemente cera la matriz de IVA

void cerar(){
	int i, j;
	for(i=0;i<EXENTA;i++){
		iva[i]=0;
		iva_r[i]=0;
		for(j=0;j<6;j++){
			ultimos[j][i]=0;
		}
	
	}
}

//Simplemente imprime la matriz de IVA
void imprimetotales (){
	short int i;

	printf("\n\tIVA 10% \tIVA 5% \t\tEXENTAS\n");
	printf("\t%d", iva[IVA10]);
	printf("\t\t%d", iva [IVA5]);
	printf("\t\t%d", iva[EXENTA]);
}

/*
 *En esta función se cargara el valor del IVA 10% de una factura y se tendrá en cuenta para el cálculo del monto de la declaración más adelante
 *Parámetros:
 *-
 *Retorno:
 *-Monto de valor cargado
 */
int calculo10(short int * ultimo_iva10){
	int monto_a_cargar;	
	short int i;
	do{
		printf("\nIngrese el monto del IVA 10% (de una factura) o 0 para volver:");
		scanf("%d", &monto_a_cargar);
		if(monto_a_cargar==0)
			break;
	}while(monto_a_cargar<0);
	printf("\nEl monto cargado fue %d\n", monto_a_cargar);
	if(monto_a_cargar>0){
		if((*ultimo_iva10)==5){
			for(i=1;i<5;i++)
				ultimos[i-1][IVA10]=ultimos[i][IVA10];
			ultimos[(*ultimo_iva10)-1][IVA10]=monto_a_cargar;
		}
		else{
			ultimos[(*ultimo_iva10)][IVA10]=monto_a_cargar;
			(*ultimo_iva10)++;
		}
			
		iva[IVA10]=iva[IVA10]+monto_a_cargar;
	}
	
	return monto_a_cargar;
}
/*
 *En esta función se cargara el valor del IVA 5% de una factura y se tendrá en cuenta para el cálculo del monto de la declaración más adelante
 *Parámetros:
 *-
 *Retorno:
 *-Monto de valor cargado
 */
int calculo5(short int * ultimo_iva5){
	int monto_a_cargar;	
	short int i;
	do{
		printf("\nIngrese el monto del IVA 5% (de una factura) o 0 para volver:");
		scanf("%d", &monto_a_cargar);
		if(monto_a_cargar==0)
			break;
	}while(monto_a_cargar<0);
	printf("\nEl monto cargado fue %d\n", monto_a_cargar);
	if(monto_a_cargar>0){
		if((*ultimo_iva5)==5){
			for(i=1;i<5;i++)
				ultimos[i-1][IVA5]=ultimos[i][IVA5];
			ultimos[(*ultimo_iva5)-1][IVA5]=monto_a_cargar;
		}
		else{
			ultimos[(*ultimo_iva5)][IVA5]=monto_a_cargar;
			(*ultimo_iva5)++;
		}
			
		iva[IVA10]=iva[IVA10]+monto_a_cargar;
	}
	return monto_a_cargar;
}
/*
 *En esta función se cargara el valor de EXENTAS de una factura y se tendrá en cuenta para el cálculo del monto de la declaración más adelante
 *Parámetros:
 *-
 *Retorno:
 *-Monto de valor cargado
 */
int exenta(short int * ultimo_exenta){
	int monto_a_cargar;	
	short int i;
	do{
		printf("\nIngrese el monto de Exentas (de una factura) o 0 para volver:");
		scanf("%d", &monto_a_cargar);
		if(monto_a_cargar==0)
			break;
	}while(monto_a_cargar<0);
	printf("\nEl monto cargado fue %d\n", monto_a_cargar);
	if(monto_a_cargar>0){
		if((*ultimo_exenta)==5){
			for(i=1;i<5;i++)
				ultimos[i-1][EXENTA]=ultimos[i][EXENTA];
			ultimos[(*ultimo_exenta)-1][EXENTA]=monto_a_cargar;
			}
		else{
			ultimos[(*ultimo_exenta)][EXENTA]=monto_a_cargar;
			(*ultimo_exenta)++;
		}
	}
	return monto_a_cargar;
}
/*
 *Esta función recibe un parametro de que lugar quiere que se borre un valor que se ingreso anteriormente o un valor específico (IVA10, IVA5, EXENTA) 
 * y resta de lo que tiene en ese momento
 *Parámetro:
 *-
 *Retorna:
 *-Valor borrado int 
 */
int borrar(short int * ultimo_iva10, short int * ultimo_iva5, short int * ultimo_exenta){
	int monto_borrado;
	int opcion;
	short int i=0;
	short int j=0;
	int ban=FALSE;
	do{
		printf("\n\tIngrese de donde desea borrar:\n\t1-IVA 10%\n\t2-IVA 5%\n\t3-EXENTAS\n");
		scanf("%d", &opcion);
	}while(opcion!=1 && opcion!=2 && opcion != 3);
					
	do{
		printf("\nIngrese el monto a borrar o restar de la opcion que escogio o 0 para volver:");
		scanf("%d", &monto_borrado);
		if(monto_borrado==0)
			break;
	}while(monto_borrado<0);
	
	printf("\nEl monto borrado fue %d\n", monto_borrado);
	
	if(monto_borrado>0){
		opcion=opcion-1;
		iva[opcion]=iva[opcion]-monto_borrado;
		switch (opcion){
			case IVA10:
				while(i<5){
					if(ultimos[i][IVA10] == monto_borrado && ban==FALSE){
						for(j=i+1;j<6;j++){
							if(j<5)
								ultimos[j-1][IVA10]=ultimos[j][IVA10];	
							else if(j==5)
								ultimos[j-1][IVA10]=0;
							else
								break;
						}
						(*ultimo_iva10)--;
						ban=TRUE;
					}
					i++;
				}
				break;
			case IVA5:
				while(i<5){
					if(ultimos[i][IVA5] == monto_borrado && ban==FALSE){
						for(j=i+1;j<6;j++){
							if(j<5)
								ultimos[j-1][IVA5]=ultimos[j][IVA5];	
							else if(j==5)
								ultimos[j-1][IVA5]=0;
							else
								break;
						}
						(*ultimo_iva5)--;
						ban=TRUE;
					}
					i++;
				}
				break;
			case EXENTA:
				while(i<5){
					if(ultimos[i][EXENTA] == monto_borrado && ban==FALSE){
						for(j=i+1;j<6;j++){
							if(j<5)
								ultimos[j-1][EXENTA]=ultimos[j][EXENTA];	
							else if(j==5)
								ultimos[j-1][EXENTA]=0;
							else
								break;
						}
						(*ultimo_exenta)--;
						ban=TRUE;
					}
					i++;
				}
				break;
			default:
				printf("\nERROR: mala opcion");
				//sale
				break;
		}
	}

	return monto_borrado;
}
