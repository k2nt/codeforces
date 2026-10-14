#include <iostream>
#include <vector>

int reflect(int p, int x) 
{
    return 2 * p - x;
}

int solve(int n, std::vector<int> a)
{
    int x = 0;
    for (int i = n - 1; i >= 0; i--)
    {
        x = reflect(a[i], x);
    }

    return x / 2;
}

int main()
{
    int t;
    std::cin >> t;

    while (t--)
    {
        int n;
        std::cin >> n;

        std::vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            std::cin >> a[i];
        }

        std::cout << solve(n, a) << "\n";
    }
}
