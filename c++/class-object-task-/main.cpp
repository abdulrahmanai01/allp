/*



#include<iostream>
using namespace std;
class aadharid
{
public:
     aadharid()
    {
    int age;


        cout <<" Entet the age";
        cin >> age;
        if (age>=5){
        cout <<"You are eligible for biometric";

    }
    else{
        cout <<"age does not match";

    }
}
aadharid(float age)
{
    if (age>4.9)
    {
        cout <<"\n Eligible for bio";
    }
    else{
        cout <<"age not match";
    }
}
};
int main()
{
  float age;
  aadharid ai;
  cout <<"\n Enter the second age";
  cin >> age;
  aadharid a2 (age);

}



















/*
#include<iostream>

using namespace std;
class addition
{

public:
    void checkage(int age)
    {

        if (age>=18)
        {
            cout << "You are aeligible";

        }
        else
        {
            cout << "You are not eligible";

        }
    }
};
int main()
{
    int age;
    addition ad;
    cout <<"Enter the age";
    cin >> age;
    ad.checkage(age);

}






















/*
#include<iostream>


using namespace std;
class arith
{
public:
       void addition()
   {
       int x,y;
       cout<<"enter the first value....";
       cin>>x;
       cout<<"\n enter the second value...";
       cin>>y;
       cout<<"\n adition value....";
       cout<<(x+y);

   }
   void subraction()
   {
       int x,y;
       cout<<"\n enter the first value....";
       cin>>x;
       cout<<"\n enter the second value...";
       cin>>y;
       cout<<"\n subraction value....";
       cout<<(x-y);

        }
   void multiplication()
   {
       int x,y;
       cout<<"\n enter the first value....";
       cin>>x;
       cout<<"\n enter the second value...";
       cin>>y;
       cout<<"\n multiplication...";
       cout<<(x*y);
   }
    void divition()
   {
       int x,y;
       cout<<"\n enter the first value....";
       cin>>x;
       cout<<"\n enter the second value...";
       cin>>y;
       cout<<"\n aditin value....";
       cout<<(x/y);
   }
    void modulas();
    void increment();
    void decrement();

};
void arith::modulas()
{
    int x,y;
       cout<<"\n enter the first value....";
       cin>>x;
       cout<<"\n enter the second value...";
       cin>>y;
       cout<<"\n modulas value....";
       cout<<(x%y);
}
void arith::increment()
{
     int x;
       cout<<"\n enter the first value....";
       cin>>x;
       cout<<"\n increment value....";
       cout<<(x++);
}
void arith::decrement()
{
     int x;
       cout<<"\n enter the first value....";
       cin>>x;
       cout<<"\n decrement value....";
       cout<<(x--);
}
int main()
{
    arith AOP,ASP,APO;
    AOP.addition();
    AOP.subraction();
    AOP.multiplication();
    AOP.divition();
    AOP.modulas();
    AOP.increment();
    AOP.decrement();
    return 0;
}
/*











/* #include<iostream>


using namespace std;
class fclsmethod
{

    public:   //access specifier
        int a=0;
        void multiply()
        { int x,y;

            cin >>x >>y;
            cout <<(x*y);

        }
};
int addition()
{
    int a,b,c;
    cin>>a >>b;
    c=a+b;
    cout<<c;
    return 0;}




int main()
{
    addition();
    fclsmethod FCM;
    FCM.a;
    FCM.multiply();
    return 0;

}/*






































/*#include <iostream>

using namespace std;

int main()
{
    int value1,value2,total,op;
    cout<<"Enter the value 1 :";
    cin>>value1;
    cout<<"Enter the value 2 :";
    cin>>value2;
    cout<<"operator type :";
    cin>>op;
    switch (op)
    {
     case 1:
       total=value1+value2;
       cout<<"added value"<<total;
       break;
     case 2:
        total=value1-value2;
        cout<<"subtract value"<<total;
        break;

    case 3:
       total=value1*value2;
       cout<<"mul value"<<total;
       break;
     case 4:
        total=value1/value2;
        cout<<"div value"<<total;
        break;
    }
    return 0;
}

#include<iostream>


using namespace std;
int main()
{
    int age;
    cout<<"Enter the age";
    cin>>age;
    if(age>=18,age<=40)
    {
        cout<<"you are eligible for supplyment";
    }
    else if (age<18)
    {
        cout<<"you are under 18 not allowed";
    }
    else
    {
        cout<<"you are 40+not allowed";

    }
    return 0;
}
*/
