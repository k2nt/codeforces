/* First of many */

#include <iostream>
#include <cstdint>

int main()
{
    std::int64_t n, m, a;
    std::cin >> n >> m >> a;
    std::cout << ((n + a - 1) / a) * ((m + a - 1) / a) << '\n';
}
