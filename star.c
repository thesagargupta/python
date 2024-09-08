//start program

#include<stdio.h>

int main(){

int n;

printf("enter your number: ");
scanf("%d",&n);

for(int i=0; i<=n; i++){
    
    for(int j=0;j<i+1; j++){
    printf(" * ");
}
printf("\n");
}
return 0;
}


#include<stdio.h>

int main(){

    int n;

    printf("enter your number: ");
    scanf("%d",&n);

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n-i; j++){
            printf(" ");
        }

        for(int k=1; k<=(2*i-1); k++){

            printf("*");

        }
        printf("\n");
    }
    

    return 0;
}