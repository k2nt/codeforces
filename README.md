# Codeforces

Personal Codeforces solutions in multiple languages.

Solutions and helper scripts live in `src/<language>/`. Name solutions by
problem ID, such as `123A.cpp`. Input files can stay beside the source.
Generated binaries go in `build/<language>/`.

## CPP

Requires Bash and GNU GCC 16 (`g++-16`). Uses C++23 by default.

```bash
cd src/cpp
./build 123A.cpp                 # Build only
./run 123A.cpp                   # Build and run
./run 123A.cpp < 123A.inp         # Read input from a file
```

Change the C++ standard or output folder in
[`src/cpp/build-config.ini`](src/cpp/build-config.ini).
Relative output paths start from `src/cpp/`.
Use `CXX` to choose another compiler:

```bash
CXX=g++-16 ./run 123A.cpp
```

Binaries and `.in`, `.inp`, and `.txt` input files are ignored by Git.
