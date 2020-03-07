#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<windows.h>

struct details
{
    char name[20]; int age; char gender[10]; float dist_covered ;int step_s;
};
struct details read_heart( struct details e)
{
    printf("Please enter the following details \n");
    /*printf("Enter name :");
    scanf("%s",e.name);*/

    printf("Enter your gender :");
    scanf("%s",e.gender);
    printf("Enter your distance covered in meters :");
    scanf("%f",&e.dist_covered);
    printf("Enter age :");
    scanf("%d",&e.age);


    return e;

};
void heartrates(struct details e)
{ if(e.dist_covered>0 && e.dist_covered<=5)
   {

    if (e.age>10 && e.age <=20)
    {
        printf("Your heart rate is 130 BPM \n");
    }
    if (e.age>20 && e.age <=30)
    {
        printf("Your heart rate is 120 BPM \n");
    }
    if(e.age>30 && e.age<=40)
    {
        printf("Your heart rate is 116 BPM \n");
    }
    if (e.age>40 && e.age<=50)
    {
        printf("Your heart rate is 98 BPM \n");
    }
    if (e.age>50 && e.age <=60)
    {
        printf("Your heart rate is 90 BPM \n");
    }
    if(e.age>60 && e.age<= 70)
    {
        printf("Your heart rate is 84 BPM \n");
    }
    if (e.age>70)
    {
        printf("Your heart rate is 82 BPM \n");
    }}

 if (e.dist_covered>5)
    {
         if (e.age>10 && e.age <=20)
    {
        printf("Your heart rate is 160 BPM \n");
    }
    if (e.age>20 && e.age <=30)
    {
        printf("Your heart rate is 150 BPM \n");
    }
    if(e.age>30 && e.age<=40)
    {
        printf("Your heart rate is 146 BPM \n");
    }
    if (e.age>40 && e.age<=50)
    {
        printf("Your heart rate is 120 BPM \n");
    }
    if (e.age>50 && e.age <=60)
    {
        printf("Your heart rate is 94 BPM \n");
    }
    if(e.age>60 && e.age<= 70)
    {
        printf("Your heart rate is 89 BPM \n");
    }
    if (e.age>70)
    {
        printf("Your heart rate is 84 BPM \n");
    }

    }

};
void steps (struct details e)
{
    float step_s;
    step_s=e.dist_covered*1250;
    printf("Distance covered : %.2f \n",e.dist_covered);
    printf("number of steps : %.0f\n",step_s);
}


struct client
{
  char name[100];
  int height_inches;
  float weight_kilograms;
  float bmi;
}b;
struct client cal_bmi(struct client b)
{ float meters; float ans;
  meters=b.height_inches*.025;
  b.bmi=(b.weight_kilograms)/(meters*meters);
  printf("%s's bmi is %f \n",b.name,b.bmi);
  b.bmi<18.5?printf("%s is Underweight\n",b.name):(b.bmi<25)?printf("%s is of Normal weight\n",b.name):(b.bmi<30)?printf("%s is Overweight\n",b.name):printf("%s is  Obese\n",b.name);
return b;
}
struct user
{

    float calories_burnt;
    float speed;
    float MET;
}s;
// MET is your metabolic equivalent used to calculate the calories burnt by using the speed of your movement.
float calorie(struct user s,struct client b)
{
    float calories_burnt,cal;
     if (3.2<=s.speed&&s.speed<4)
     {s.MET=2.5;}
     if(4<=s.speed&&s.speed<4.8)
     {s.MET=3;}
     if(4.8<=s.speed&&s.speed<6.4)
     {s.MET=3.5;}
     if(6.4<=s.speed&&s.speed<7.2)
     {s.MET=4;}
     if(7.2<=s.speed&&s.speed<8)
     {s.MET=4.5;}
     if(8<=s.speed&&s.speed<8.32)
     {s.MET=8;}
     if(8.32<=s.speed&&s.speed<9.6)
     {s.MET=9;}
     if(9.6<=s.speed&&s.speed<10.72)
     {s.MET=10;}
     if(10.72<=s.speed&&s.speed<11.2)
     {s.MET=11;}
     if(11.2<=s.speed&&s.speed<12)
     {s.MET=11.5;}
     if(12<=s.speed&&s.speed<12.8)
     {s.MET=12.5;}
     if(12.8<=s.speed&&s.speed<13.76)
     {s.MET=13.5;}
     if(13.76<=s.speed&&s.speed<14.4)
     {s.MET=14;}
     if(14.4<=s.speed&&s.speed<16)
     {s.MET=15;}
     if(16<=s.speed&&s.speed<17.44)
     {s.MET=16;}
     if(17.44<=s.speed&&s.speed<20)
     {s.MET=18;}
     cal=s.calories_burnt=.0175*s.MET*b.weight_kilograms;
     printf("%s burnt %f calories\n",b.name,s.calories_burnt);
     return cal;
}

void bp(int sys,int dia)
{

    if(sys<120 || dia<80)
    {
        printf("your blood pressure is low \n");
    }
    if(sys>120 || dia>80)
    {
        printf("your blood pressure is high\n");
    }
    else
    {
        printf("normal blood pressure \n");
    }
}
void protein(struct client b )

{ float g;
 g=b.weight_kilograms*1.7;
 printf("grams of protein needed to be consumed per day %f \n",g);


}
void calcium_vitamin(struct details e)
{

      if(e.age<=50)
       {
           printf("calcium required is 1000mg and  vitamin D required is 400 IU\n");
       }
        else
            printf("calcium required is 1200mg and vitamin D required is 800 IU \n ");

}



int main()
{
    printf("\n\t\t\tWELCOME TO FITNESS CALCULATOR\n\n");

    char choice,option,username[100],password[100],email[100],*line[100],*line1[100],*user[100],*pas[100],*line2[100];
    int phno,count=0,i=1,k=1,z=1,x=1,a=0;
    float calories_burnt;

    struct details e,r,c;
    struct client b,q;

    int sys; int dia;

    //FILE * fp_U = fopen("username.txt","a");
    //FILE * fp_P = fopen("password.txt","a");
    FILE * fp_N = fopen("names.txt","a");

    while (i>0)
    {printf("Are you an existing user?(y/n) :");
    scanf("%s",&choice);
     switch(choice)
     {
         case 'y':
             x=1;
             FILE * fp_U = fopen("username.txt","r");
             FILE * fp_P = fopen("password.txt","r");
             FILE * f1=fopen("data.txt","r");
             while(x>0)
             {   printf("Enter username :");
                 scanf("%s",username);
                 while(fgets(line,sizeof(line),fp_U)!=NULL)
                { //printf("%s",line);
                    strtok(line,"\n");
                    count+=1;
                    strcpy(user,line);
                    if(strcmp(line,username)==0)
                    { //printf("%d\n",count);
                        //printf("yes\n");
                        strcpy(user,line); }}
                 if(strcmp(user,username)==0)
                 {
                     x--;
                 }
                 else
                 {  printf("Invalid Username Try again!\n");

                 }}
                 int xx=1;
                 while(xx>0)
                  {
                      printf("Enter your password :");
                      int p=0;
                      do{
                        password[p]=getch();
                        if(password[p]!='\r'){
                        printf("*");
                        }p++;
                    }while(password[p-1]!='\r');
                    password[p-1]='\0';
                    printf("\n");
                    while((fgets(line1,sizeof(line1),fp_P)!=NULL) && a<count)

                    {



                    /*printf("%s",line1);*/
                    strtok(line1,"\n");
                    strcpy(pas,line1);
                    if(strcmp(line1,password)==0)
                    {printf("Correct password\n");
                    strcpy(pas,line1);}
                    else
                    {a++;}}
                    if(strcmp(pas,password)==0)
                    {
                        printf("Correct password\n");
                        xx--;
                    }
                    else
                    {
                        printf("Invalid Password Try again!\n");
                    }}


                 printf("\nWould you like to\n1.View your previous entered data\n2.Use the calculator again\n");

                printf("Enter your option :");
                scanf("%d",&option);
                //printf("This is for the check of a and count %d,%d",a,count);
                if(option==1)
                { a=0;
                 while((fgets(line2,sizeof(line2),f1)!=NULL) && a<count)
                 {
                     if(a==(count-1))
                     {    printf("%s",line2);
                         //fscanf(f1,"%s\n",line2);
                     }
                     else
                     {a++;}
                 }

                }
                if(option==2)
                {   FILE * f2=fopen("updated_data.txt","a");
                    printf("\nBMI CALCULATION\n");
                printf("enter your name :");
                scanf("%s",&b.name);
                printf("enter your weight in kilograms :");
                scanf("%f",&b.weight_kilograms);
                printf("enter your height in inches :");
                scanf("%d",&b.height_inches);
                q=cal_bmi(b);

                // calories burnt
                printf("\nCALORIES BURNT\n");
                printf("enter the speed you are moving at kilometers per hour  at a range 3.2 to 20 :");
                scanf("%f",&s.speed);
                float j=calorie(s,b);

                printf("\nSTEPS COVERED AND HEART RATE\n");
                r=read_heart(e);
                /*printf("\n"); printf("HELLO %s\n",b.name);*/
                fprintf(fp_N,"%s\n",b.name);

                heartrates(r);
                steps(r);

                printf("\nBLOOD PRESSURE CHECK\n");

                printf("enter your systolic pressure :");
                scanf("%f",&sys);
                printf("enter your diastolic pressure :");
                scanf("%f",&dia);
                bp(sys,dia);
                protein(b);
                calcium_vitamin(e);
                fprintf(f2, "the clients name is:%s, height is:%d,weight is:%f,bmi is:%f,calories burnt is:%f,Speed is:%f,age is:%d, gender is: %s,distance covered is :%f\n",b.name,b.height_inches,b.weight_kilograms,q.bmi,j,s.speed,r.age,r.gender,r.dist_covered);
                fclose(f2);
                }
                printf("\n\t\t\tTHANK YOU FOR USING FITNESS CALCULATOR!\n");

            fclose(fp_U);fclose(fp_P);fclose(f1);
            i=0;break;
         case 'n':
             printf("Enter your username :");
             scanf("%s",username);
             fp_U = fopen("username.txt","a");
             fp_P = fopen("password.txt","a");
             fprintf(fp_U,"%s\n",username);
             while(k>0)
             {

                 printf("Enter your password :");
                 int p=0;
                 do{
                password[p]=getch();
                if(password[p]!='\r'){
                    printf("*");
                    }p++;
                }while(password[p-1]!='\r');
                password[p-1]='\0';
                printf("\n");
                if(strlen(password)>6 )
                {
                    k=0;
                }
                else
                {
                    printf("Weak Password Try again!\n");k++;
                }
                }k=1;
                fprintf(fp_P,"%s\n",password);
                while(k>0)
                {   int flag=0;
                    printf("Enter your email id :");
                    scanf("%s",email);
                    for(int j=0;j<strlen(email);j++)
                    {
                        if('@'==email[j])
                        {
                            flag=1;
                        }
                    }
                    if (flag==1)
                    {
                        k=0;
                    }
                    else
                    {   printf("Invalid email id Try again!\n");
                        k++;
                    }

                }k=1;
                while(k>0)
                {   int count=0;
                    printf("Enter your phone number :");
                    scanf("%d",&phno);
                    while(phno!=0)
                    {   phno /=10;
                        count++;
                    }
                    if(count==10)
                    {
                        k=0;
                    }
                    else
                    {
                        printf("Invalid phone number try again!\n");k++;
                    }
                }
                printf(" * YOUR  ACCOUNT HAS BEEN SUCCESFULLY CREATED *\nYou can now proceed to use the fitness calculator\n");

                //FILE * fp_U = fopen("username.txt","a");
                //FILE * fp_P = fopen("password.txt","a");
                //FILE * fp_N = fopen("names.txt","a");
                f1=fopen("data.txt","a");


                printf("\nBMI CALCULATION\n");
                printf("enter your name :");
                scanf("%s",&b.name);
                printf("enter your weight in kilograms :");
                scanf("%f",&b.weight_kilograms);
                printf("enter your height in inches :");
                scanf("%d",&b.height_inches);
                q=cal_bmi(b);

                // calories burnt
                printf("\nCALORIES BURNT\n");
                printf("enter the speed you are moving at kilometers per hour  at a range 3.2 to 20 :");
                scanf("%f",&s.speed);
                float j=calorie(s,b);

                r=read_heart(e);
                /*printf("\n"); printf("HELLO %s\n",b.name);*/
                fprintf(fp_N,"%s\n",b.name);
                printf("\nSTEPS COVERED AND HEART RATE\n");
                heartrates(r);
                steps(r);

                printf("\nBLOOD PRESSURE CHECK\n");

                printf("enter your systolic pressure :");
                scanf("%f",&sys);
                printf("enter your diastolic pressure :");
                scanf("%f",&dia);
                bp(sys,dia);
                protein(b);
                calcium_vitamin(e);


                fprintf(f1, "the clients name is:%s, height is:%d,weight is:%f,bmi is:%f,calories burnt is:%f,Speed is:%f,age is:%d, gender is: %s,distance covered is :%f\n",b.name,b.height_inches,b.weight_kilograms,q.bmi,j,s.speed,r.age,r.gender,r.dist_covered);
                fclose(fp_U);fclose(fp_P);fclose(f1);





                printf("\n\t\t\tTHANK YOU FOR USING FITNESS CALCULATOR!\n");
                i=0;break;
         default: printf("Wrong input try again\n");i++;
     }

    }
}
