#include "petar.hpp"
#ifdef GPERF_PROFILE
#include <gperftools/profiler.h>
#endif

int main(int argc, char *argv[]){

#ifdef GPERF_PROFILE
    ProfilerStart("prof.out");
#endif
    PeTar petar;

    petar.initialFDPS(argc,argv);
    
    PS::S32 iread = petar.readParameters(argc,argv);
    if (iread<0) return 0;

    auto& inp = petar.input_parameters;

    if (inp.fname_inp.value!="") petar.readDataFromFile();
    else petar.generatePlummer();

    petar.initialParameters();

    petar.initialStep();

#if 0
    PS::F64 dt_break = inp.dt_snp.value;
    PS::F64 dt_end = inp.time_end.value;
    PS::S32 n_loop = dt_end/dt_break;
    PS::F64 time_break = 0.0;
    
    for (int i=0; i<n_loop; i++) {   
        time_break += dt_break;
        int n_interupt = 1;
        while(n_interupt>0) n_interupt = petar.evolveToTime();
    }
#else
    int n_interupt = 1;
    while(n_interupt>0) n_interupt = petar.evolveToTime();
    
#endif

#ifdef GPERF_PROFILE
    ProfilerStop();
#endif

    return 0;

}
