#include <stdio.h>

int main(){

    int n,i;
    int prime = 1;
    printf("enter your number: ");
    scanf("%d",&n);

    if (n==0 || n==1)
    {
        printf("it is neither prime nor composite"); 
    }
    if(n==2 || n==3){
        printf("it is prime");
    }
for(i=2;i<=n/2;i++){
    if(n%i==0){
        prime=0;
    break;
}
}

if(prime==0){
    printf("it is not prime");
}

else{
    printf("it is prime");
}
   
    return 0;
}

//prime number method 2

#include<stdio.h>

int main(){

int n,i;
int flag=1; 
printf("Enter your number: ");
scanf("%d",&n);

if(n==0 || n==1){
    printf("neither prime nor composite");
}

for(i=2;i*i<=n;i++){

if(n%i==0){
    flag=0;
    break;
}
}

if(flag==1){
    printf("number is prime");
}
else{
    printf("number is composite");
}
return 0;
}