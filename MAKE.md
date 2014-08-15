make -r -j6
CCACHE_DIR="C:\Bin\CygWin64\home\morteza\.ccache" CXX="ccache g++" CC="ccache cc"

without ccache:
real    1m9.011s
user    0m0.000s
sys     0m0.000s

with ccache (delete .ccache folder):
real    1m30.202s
user    0m0.015s
sys     0m0.015s

with ccache (.ccache folder exists):
real    0m58.433s
user    0m0.016s
sys     0m0.015s
---
real    0m9.408s
user    0m0.015s
sys     0m0.015s



