BookSim Interconnection Network Simulator (HPCAN)
=========================================

BookSim is a cycle-accurate interconnection network simulator.
Originally developed for and introduced with the [Principles and Practices of Interconnection Networks]
(http://cva.stanford.edu/books/ppin/) book, its functionality has since been continuously extended.
The current major release, BookSim 2.0, supports a wide range of topologies such as mesh, torus and flattened butterfly networks,
 provides diverse routing algorithms and includes numerous options for customizing the network's router microarchitecture.

---

If you use BookSim in your research, we would appreciate the following citation in any publications to which it has contributed:

Nan Jiang, Daniel U. Becker, George Michelogiannakis, James Balfour, Brian Towles, John Kim and William J. Dally. 
A Detailed and Flexible Cycle-Accurate Network-on-Chip Simulator. In *Proceedings of the 2013 IEEE International Symposium on Performance Analysis of Systems and Software*, 2013.

---

### Git Problem:

Remember, to use git-scm on windows with two github account, follow instruction in the following link:

http://kevinpelgrims.com/blog/2012/07/19/setting-up-multiple-github-accounts-on-windows

Note that you shoud use git-scm bash in order to add second ssh-key to git-agent.

### Adding project to Eclipse:

From file->new use Make file project with Existing code, under Toolchain for Indexer Settings
select MinGW GCC, and browse to source code directory from Existing Code Location, then click Finish.

Now, under project properties, in C/C++ Build side menu, go to Builder Settings tab, and change Build Location to this:
${workspace_loc:/booksim2/src}/
  
### Fixed Eclipse Unresolved Symbols:

Go to Project > Properties > C/C++ General > Preprocessor Includes... > Providers and select "CDT GCC Built-in Compiler Settings"

or 

1. Right-click on the probject and select "Properties"
2. Go to "C/C++ General" -> "Paths and Symbols" and select "Includes" tab
3. Select "GNU C++"
4. Press on "Add..."
5. Look for the folder "C:\dev\eclipse\mingw\lib\gcc\mingw32\4.4.1-dw2\include\c++" or similar (I searched for the file "iostream" under c:\dev\eclipse\mingw and found it under that folder)