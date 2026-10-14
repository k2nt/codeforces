# Codeforces

Repository for personal Codeforces solutions.

## Repository structure

```text
codeforces/
├── src/
│   └── cpp/
│       ├── build
│       ├── run
│       ├── build-config.ini  # C++ standard and binary output directory
│       ├── .gitignore        # Ignore input files
│       ├── 123A.cpp          # Problem ID and letter
│       ├── 123A.inp          # Optional input, beside source
│       └── 123A.out          # Optional expected output
└── build/
    └── cpp/            # Generated binaries, ignored by Git
```

Keep each solution self-contained for submission. Optional input and expected
output files live beside their source; no separate samples folder is needed.
The scripts accept `.cpp` files under `src/cpp/`.

## Build and run

Requires Bash and GNU GCC 16 (`g++-16`), or a compiler selected through `CXX`
that supports the configured C++ standard. Default standard is C++23.
From repository root:

```bash
cd src/cpp

# Compile only
./build 123A.cpp

# Compile and run with keyboard input
./run 123A.cpp

# Read input from a file
./run 123A.cpp < 123A.inp

# Or pipe input
cat 123A.inp | ./run 123A.cpp

# Compare output with an optional expected-output file
./run 123A.cpp < 123A.inp > /tmp/123A.actual
diff -u 123A.out /tmp/123A.actual
```

`build` compiles with `-std=c++<CXX_STANDARD> -O2 -g -Wall -Wextra -Wshadow`
and prints the binary's absolute path. Source paths are relative to your current
directory or absolute. Binaries mirror paths relative to `src/cpp/` under
`BUILD_DIR`: `src/cpp/123A.cpp` produces `build/cpp/123A` with default settings.

Without changing directories, from repository root:

```bash
./src/cpp/build src/cpp/123A.cpp
./src/cpp/run src/cpp/123A.cpp < src/cpp/123A.inp
```

## Build configuration

Edit `src/cpp/build-config.ini` to select the C++ standard and binary output
directory. Default settings:

```ini
CXX_STANDARD=23
BUILD_DIR=../../build/cpp
```

Relative `BUILD_DIR` paths resolve from `src/cpp/`; absolute paths also
work. `run` reads same settings through `build`. Compiler defaults to `g++-16`;
`CXX` environment variable overrides compiler executable.

Settings use plain `KEY=value` lines, with optional blank lines and `#` comments.
Paths are literal: no quotes, shell variable expansion, or `~` expansion.
For example, set `CXX_STANDARD=20` to compile with C++20.

Root `.gitignore` ignores `build/cpp/` output. `src/cpp/.gitignore` ignores
`*.in`, `*.inp`, and `*.txt` input files. If you change `BUILD_DIR`, add that
output directory to root `.gitignore`.

`run` always builds first, then executes only if compilation succeeds. It
preserves standard input/output and forwards arguments after the source path
to the program.

The default compiler is GNU C++ (`g++-16`, GCC 16.2.0). On macOS, install or
upgrade the latest stable GCC with Homebrew:

```bash
brew install gcc
# If GCC is already installed:
brew upgrade gcc
```

Override the compiler with an executable:

```bash
CXX=g++-16 ./src/cpp/run src/cpp/123A.cpp
```

On macOS, unversioned `g++` usually invokes Apple Clang, not GNU GCC.
The versioned GNU compiler supports `<bits/stdc++.h>` and GNU policy-based
data structures. Replace `g++-16` above with your installed executable name.
On macOS, builds use the current SDK reported by `xcrun --show-sdk-path`,
avoiding stale SDK paths embedded in an installed compiler.
The compiler chooses the macOS deployment target by default.
Override it with `MACOSX_DEPLOYMENT_TARGET` if needed.

For bare `build` and `run` commands in the current terminal:

```bash
export PATH="$PWD/src/cpp:$PATH"
build src/cpp/123A.cpp
run src/cpp/123A.cpp < src/cpp/123A.inp

cd src/cpp
run 123A.cpp < 123A.inp
```
