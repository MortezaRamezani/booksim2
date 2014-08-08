23:57:50 **** Build of configuration Default for project booksim2 ****
make all 
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c booksim_config.cpp -o booksim_config.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c buffer.cpp -o buffer.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c rng_wrapper.cpp -o rng_wrapper.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c flitchannel.cpp -o flitchannel.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c trafficmanager.cpp -o trafficmanager.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c routefunc.cpp -o routefunc.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c buffer_state.cpp -o buffer_state.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c main.cpp -o main.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c packet_reply_info.cpp -o packet_reply_info.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c flit.cpp -o flit.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c misc_utils.cpp -o misc_utils.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c config_utils.cpp -o config_utils.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c random_utils.cpp -o random_utils.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c injection.cpp -o injection.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c module.cpp -o module.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c credit.cpp -o credit.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c vc.cpp -o vc.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c batchtrafficmanager.cpp -o batchtrafficmanager.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c traffic.cpp -o traffic.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c outputset.cpp -o outputset.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c stats.cpp -o stats.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c rng_double_wrapper.cpp -o rng_double_wrapper.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/maxsize.cpp -o allocators/maxsize.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/loa.cpp -o allocators/loa.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/pim.cpp -o allocators/pim.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/separable_input_first.cpp -o allocators/separable_input_first.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/allocator.cpp -o allocators/allocator.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/separable.cpp -o allocators/separable.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/separable_output_first.cpp -o allocators/separable_output_first.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/selalloc.cpp -o allocators/selalloc.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/islip.cpp -o allocators/islip.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c allocators/wavefront.cpp -o allocators/wavefront.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c arbiters/arbiter.cpp -o arbiters/arbiter.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c arbiters/roundrobin_arb.cpp -o arbiters/roundrobin_arb.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c arbiters/tree_arb.cpp -o arbiters/tree_arb.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c arbiters/matrix_arb.cpp -o arbiters/matrix_arb.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c arbiters/prio_arb.cpp -o arbiters/prio_arb.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/kncube.cpp -o networks/kncube.o
networks/kncube.cpp: In member function 'virtual void KNCube::InsertRandomFaults(const Configuration&)':
networks/kncube.cpp:302:36: warning: 'chan' may be used uninitialized in this function [-Wmaybe-uninitialized]
       OutChannelFault( node, chan );
                                    ^
networks/kncube.cpp:302:36: warning: 'node' may be used uninitialized in this function [-Wmaybe-uninitialized]
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/dragonfly.cpp -o networks/dragonfly.o
networks/dragonfly.cpp: In function 'int dragonfly_port(int, int, int)':
networks/dragonfly.cpp:114:7: warning: variable 'group_dest' set but not used [-Wunused-but-set-variable]
   int group_dest=-1;
       ^
networks/dragonfly.cpp: In member function 'virtual void DragonFlyNew::_BuildNet(const Configuration&)':
networks/dragonfly.cpp:359:9: warning: variable '_grp_num_routers' set but not used [-Wunused-but-set-variable]
     int _grp_num_routers;
         ^
networks/dragonfly.cpp:361:9: warning: variable 'grp_ID2' set but not used [-Wunused-but-set-variable]
     int grp_ID2;
         ^
networks/dragonfly.cpp:224:7: warning: variable '_dim_size' set but not used [-Wunused-but-set-variable]
   int _dim_size=-1;
       ^
networks/dragonfly.cpp: In function 'void ugal_dragonflynew(const Router*, const Flit*, int, OutputSet*, bool)':
networks/dragonfly.cpp:498:23: warning: variable 'min_hopcnt' set but not used [-Wunused-but-set-variable]
   int min_queue_size, min_hopcnt;
                       ^
networks/dragonfly.cpp:499:26: warning: variable 'nonmin_hopcnt' set but not used [-Wunused-but-set-variable]
   int nonmin_queue_size, nonmin_hopcnt;
                          ^
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/fly.cpp -o networks/fly.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/anynet.cpp -o networks/anynet.o
networks/anynet.cpp: In member function 'void AnyNet::readFile()':
networks/anynet.cpp:494:25: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if(node_check[i] != i){
                         ^
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/network.cpp -o networks/network.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/tree4.cpp -o networks/tree4.o
networks/tree4.cpp: In member function 'int Tree4::_WireLatency(int, int, int, int)':
networks/tree4.cpp:288:10: warning: 'L' may be used uninitialized in this function [-Wmaybe-uninitialized]
   return L;
          ^
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/qtree.cpp -o networks/qtree.o
networks/qtree.cpp: In member function 'virtual void QTree::_BuildNet(const Configuration&)':
networks/qtree.cpp:141:12: warning: 'r' may be used uninitialized in this function [-Wmaybe-uninitialized]
  _routers[r]->AddInputChannel( _chan[c],
            ^
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/flatfly_onchip.cpp -o networks/flatfly_onchip.o
networks/flatfly_onchip.cpp: In function 'int find_distance(int, int)':
networks/flatfly_onchip.cpp:1207:7: warning: variable '_dim_size' set but not used [-Wunused-but-set-variable]
   int _dim_size;
       ^
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/cmesh.cpp -o networks/cmesh.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c networks/fattree.cpp -o networks/fattree.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c power/power_module.cpp -o power/power_module.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c power/switch_monitor.cpp -o power/switch_monitor.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c power/buffer_monitor.cpp -o power/buffer_monitor.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c routers/chaos_router.cpp -o routers/chaos_router.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c routers/iq_router.cpp -o routers/iq_router.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c routers/event_router.cpp -o routers/event_router.o
g++ -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -MMD -c routers/router.cpp -o routers/router.o
flex config.l
bison -y -d config.y
cc -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -c lex.yy.c -o lex.yy.o
lex.yy.c:1146:17: warning: 'yyunput' defined but not used [-Wunused-function]
     static void yyunput (int c, register char * yy_bp )
                 ^
lex.yy.c:1187:16: warning: 'input' defined but not used [-Wunused-function]
     static int input  (void)
                ^
cc -Wall -I. -Iarbiters -Iallocators -Irouters -Inetworks -Ipower  -O3 -g -c y.tab.c -o y.tab.o
config.y:10:0: warning: ignoring #pragma warning  [-Wunknown-pragmas]
 #pragma warning ( disable : 4102 )
 ^
config.y:11:0: warning: ignoring #pragma warning  [-Wunknown-pragmas]
 #pragma warning ( disable : 4244 )
 ^
g++  booksim_config.o buffer.o rng_wrapper.o flitchannel.o trafficmanager.o routefunc.o buffer_state.o main.o packet_reply_info.o flit.o misc_utils.o config_utils.o random_utils.o injection.o module.o credit.o vc.o batchtrafficmanager.o traffic.o outputset.o stats.o rng_double_wrapper.o allocators/maxsize.o allocators/loa.o allocators/pim.o allocators/separable_input_first.o allocators/allocator.o allocators/separable.o allocators/separable_output_first.o allocators/selalloc.o allocators/islip.o allocators/wavefront.o arbiters/arbiter.o arbiters/roundrobin_arb.o arbiters/tree_arb.o arbiters/matrix_arb.o arbiters/prio_arb.o networks/kncube.o networks/dragonfly.o networks/fly.o networks/anynet.o networks/network.o networks/tree4.o networks/qtree.o networks/flatfly_onchip.o networks/cmesh.o networks/fattree.o power/power_module.o power/switch_monitor.o power/buffer_monitor.o routers/chaos_router.o routers/iq_router.o routers/event_router.o routers/router.o lex.yy.o y.tab.o -o booksim
