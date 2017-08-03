#~/bin/bash
export LD_LIBRARY_PATH=$PWD/build
echo "Running RPE1 Eight Script:"
for i in {2,6,11,16,22,26,33,26,44,60}; do
    ./bin/reg_param_exp1 -s eight_part -t 0:.1:1 -i 0:.1:1 -u 1.0,2.0,2.0,1.0,2.0,1.0,1.0,1.0,2.0,1.0,2.0,1.0,1.0,1.0,2.0,1.0,2.0,1.0,0.1,1.0,0.1,0.1,1.0,0.1,0.1,1.0,0.1,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0 -o 2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5 -y .5,.5,.5,.5,.5,.5,.5,.5 -d $i > results/rpe1/eight$i.txt
    (cd results/rpe1/ && python3 graph.py $i "eight")
done
echo "Finished"