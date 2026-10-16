#include <iostream>
#include <cstdint>
#include <algorithm>

std::int64_t solve(int n, std::int64_t* a)
{
    std::int64_t s_min, s_max;
    s_min = s_max = a[0];

    std::int64_t v_max = a[0];
    for (int i = 1; i < n; i++)
    {
        v_max = std::max(v_max, std::max(a[i] + s_max, a[i] - s_min));
        s_min = std::min(a[i], a[i] + 2 * s_min);
        s_max = std::max(a[i], a[i] + 2 * s_max);
    }

    return v_max;
}

int main()
{
    int t; 
    std::cin >> t;

    while (t--)
    {
        int n; 
        std::cin >> n;

        std::int64_t a[n];
        for (auto &a_i : a)
        {
            std::cin >> a_i;
        }

        std::cout << solve(n, a) << "\n";
    }
}
