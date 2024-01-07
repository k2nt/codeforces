#include <iostream>

long long int n, m, a;

int main() {
    std::cin >> n >> m >> a;

    auto vn = n / a;
    auto rn = n % a;
    auto vm = m / a;
    auto rm = m % a;

    std::cout << vn * vm + (vn * (rm > 0)) + (vm * (rn > 0)) + (rm > 0 && rn > 0) << "\n";
}
