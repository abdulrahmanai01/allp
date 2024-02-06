#include <iostream>

using namespace std;

int main()
{
    int x=2, y=3, z=4;
    int *s=&x, *v=&y, *w=&z;

    cout << "Value of X:" << x << "\n";
    cout << "Address of X:" << s << "\n";
    cout << "Value of X:" << *s << "\n";

    cout << "..........................";

    cout << "\n Value of Y:" << y << "\n";
    cout << "Address of Y:" << v << "\n";
    cout << "Value of Y:" << *v << "\n";

    cout << "..........................";

    cout << "\n Value of Y:" << y << "\n";
    cout << "Address of Y:" << v << "\n";
    cout << "Value of Y:" << *v << "\n";

    cout << "..........................";
    return 0;
}
