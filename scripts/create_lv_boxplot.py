import numpy as np

def format_data(v, noise):
    N = v.size
    odd = np.mod(N,2)
    v = np.sort(v)

    median = np.median(v)
    twentyfifth = np.percentile(v, 25)
    seventyfifth = np.percentile(v, 75)
    
    iqr = seventyfifth - twentyfifth
    upper_whisker = v[v<=seventyfifth+1.5*iqr].max()
    lower_whisker = v[v>=twentyfifth-1.5*iqr].min()
    
    outliers = np.append(v[v>=seventyfifth+1.5*iqr],v[v<=twentyfifth-1.5*iqr])
    
    #index median box_top box_bottom whisker_top whisker_bottom
    print("\\addplot+[boxplot prepared={"
        "draw position=",noise, 
        ",\n\tlower whisker=", lower_whisker, 
        ",\n\tlower quartile=", twentyfifth,
        ",\n\tmedian=", median,
        ",\n\tupper quartile=", seventyfifth, 
        ",\n\tupper whisker=", upper_whisker,
        "\n}]\ntable[row sep=\\\\,y index=0]{\n\t",
        '\\\\ '.join(str(i) for i in outliers)  ,
        "\\\\\n};",
        "\n\tcoordinates {};",
        sep="") 
#Original Data used unclear config
v1 = np.array(np.mat('0.2856305 0.2527951 0.4051361 0.2465784 0.2455942 0.4887047 0.4211657 0.2865279 0.440599 0.2643942 0.252588 0.2593921 0.2619748 0.2762015 0.2632284 0.4241988 0.3472363 0.3414496 0.2603033 0.244727 0.3346535 0.3742453 0.2576993 0.266997 0.2608555 0.2680436 0.2638888 0.2385651 0.3047493 0.2687269 0.3571159 0.3382794 0.260527 0.247566 0.3384577 0.2322557 0.3600896 0.4223133 0.3160225 0.328033 0.3137034 0.313689 0.2456667 0.4369997 0.3945158 0.2827877 0.2641215 0.2789249 0.3327927 0.2299223 0.2903685 0.2774206 0.2609422 0.3712822 0.3163559 0.367371 0.3518589 0.3644145 0.2786402 0.2563012 0.3095493 0.2814199 0.3216182 0.2448115 0.2717418 0.421418 0.3341893 0.2828011 0.2906771 0.269148 0.335245 0.2722059 0.261399 0.3672368 0.354985 0.2583491 0.2648216 0.2690411 0.2487411 0.2969625 0.2496087 0.2910109 0.3017353 0.246079 0.3030991 0.3291637 0.2691728 0.3760511 0.3937806 0.4708228 0.2533595 0.2743419 0.3298928 0.2420412 0.2598126 0.2409438 0.3258603 0.3454504 0.2653244 0.2312808; 0.2556011 0.4737996 0.570127 0.3884819 0.6024021 0.4027682 0.3075667 0.3027497 0.2414136 0.3995143 0.3072879 0.5350122 0.4813213 0.3574332 0.2551457 0.4857121 0.2294086 0.3463276 0.6847568 0.4264142 0.4867232 0.5511476 0.4690003 0.304967 0.7128653 0.6151197 0.4852761 0.3516806 0.387635 0.4690609 0.383642 0.2727313 0.3453227 0.3706494 0.5613498 0.420734 0.5595453 0.5137639 0.5495918 0.3381367 0.586042 0.4204261 0.3697948 0.3359291 0.6102987 0.3289907 0.6809328 0.357689 0.4008649 0.6461576 0.425569 0.322253 0.3861249 0.4704721 0.5547688 0.5268772 0.3356287 0.4520681 0.3976303 0.2670862 0.2604082 0.3645078 0.3340611 0.4118569 0.3990897 0.5308774 0.3029392 0.3392942 0.6575968 0.2572026 0.7921405 0.2738945 0.4735306 0.3322117 0.4766739 0.2887559 0.5399228 0.511519 0.2731186 0.3132927 0.26142 0.4626712 0.373829 0.2756887 0.6268553 0.2378346 0.2904819 0.6736924 0.2399187 0.321178 0.484735 0.4255026 0.6191676 0.6033852 0.8576454 0.6774582 0.2624391 0.4541386 0.3326103 0.3723241; 0.6689217 0.8095324 0.54787 0.623547 1.013454 0.854979 0.415343 0.6917592 0.5267296 0.6234671 0.3433561 0.4972137 0.4301573 0.515068 0.7732024 0.5581694 0.5454134 0.6939811 0.7541768 0.4337683 0.8126116 0.5505829 0.4803414 0.5828247 0.8704582 0.401598 0.9627637 0.6248099 0.5350505 0.9075554 0.6147807 0.8854855 0.544197 0.669349 0.7621677 0.4286962 0.431452 0.6435797 0.5566281 0.5005513 0.2732016 0.4510028 0.3989816 0.3853682 0.5108346 0.7625935 0.3980839 1.018719 0.9407232 0.2988439 1.139726 0.4037924 0.6365919 0.4614771 0.3256461 0.277619 0.7836923 0.6961633 0.3762556 0.3197999 0.5469005 0.6720416 0.3430148 0.8793944 0.4091085 0.2480013 0.9538377 0.2401913 0.6346527 0.4387384 0.5525506 0.8712074 0.5991834 0.8840948 0.98988 0.2951681 0.6533843 0.6514583 0.5243935 0.6227476 0.8801894 0.3026587 0.2662031 0.4252186 0.3479939 0.6179264 0.2939211 0.2664547 0.3755932 0.8810638 0.3884573 0.9931542 0.4120866 0.609194 0.3253186 0.5671908 0.7837 0.261438 0.4166438 0.6669643; 1.051648 0.6908116 0.7330945 0.6059283 1.136908 0.4826685 0.7877275 0.5500182 0.6788202 1.180386 0.8115508 0.4544584 0.7111043 0.8783014 0.9790371 0.5403778 0.5395982 0.8431496 0.7224262 0.6205266 0.2877193 0.5450222 0.6890784 0.4826332 0.6305372 1.005354 0.5355547 1.327085 1.227901 1.503586 0.3324751 0.4837753 0.8079685 0.6052325 0.36855 0.3098851 1.036452 0.8879197 0.4481609 0.393629 0.7164142 0.5659018 0.4245078 1.140695 0.4841153 0.264927 1.244492 0.2410319 0.8103901 0.5676124 0.6879699 1.133424 0.7836933 1.646182 1.285169 0.3376156 0.8288183 0.5957457 0.696912 0.787446 0.6645463 0.3310814 0.3041486 0.5275971 0.7804148 0.5115834 0.320199 0.28243 0.4726871 0.2676874 0.4834 1.295546 0.7719259 0.5801013 0.3887242 0.718982 0.2998133 0.3560474 0.5128027 0.2967992 0.6203688 0.5001106 0.3439171 0.7354776 0.4392535 0.543344 0.5179444 0.8616717 0.6502152 0.5471939 0.4708871 0.6907378 0.9300779 0.4056645 0.2574905 0.440915 0.3030548 0.2851889 0.6671377 0.7122419; 0.6438571 0.5458405 0.8411136 0.5861369 1.254065 0.6204302 0.6455836 1.51532 0.4151813 1.881673 0.3675511 0.9837913 0.7554937 1.011985 0.4160434 0.3481386 1.083201 0.4151581 0.5255667 0.4754501 1.098317 0.6706058 0.5127693 1.407303 0.287365 0.5063779 1.542343 0.2424234 0.9899599 1.155528 0.8285229 1.402259 0.9655383 2.066857 1.558252 0.3866146 1.06842 0.7358662 0.8845817 1.410049 0.7986338 0.3621085 0.3501248 0.6365287 0.9492652 0.6027272 0.3492671 0.5758975 1.417895 0.299762 0.5851361 1.579274 0.9396942 0.7068127 0.4592841 1.265954 0.3465463 0.4166905 0.6138402 0.3360026 0.764717 0.6122709 0.5823011 0.9102331 0.5069129 0.6658999 0.6087418 1.050066 0.8046144 0.6537405 0.5687993 0.8491621 1.139339 0.4930023 0.4745636 0.5090007 0.3255149 0.3239797 0.6836185 0.879533 0.7407884 0.6039965 1.997292 1.094015 0.5429532 1.402285 0.3717748 1.212742 0.8641747 0.4529464 0.2816749 0.7488232 0.7669383 1.641233 0.6982825 1.460759 0.6180365 2.646267 0.9619395 0.2779011; 0.7787664 0.6042279 1.677909 0.6446455 0.5910341 1.84618 0.244359 1.172587 0.8302398 0.9727417 1.676301 1.141935 2.506458 1.808841 0.439999 1.278999 0.8757203 1.086236 1.680545 0.9363454 0.3951795 0.4011922 0.6203259 1.123168 0.6966485 0.3804728 0.6819542 1.698831 0.337205 0.6906809 0.7290241 1.110766 0.8367211 0.5340958 1.491947 0.3984067 0.4816439 0.717328 0.3803812 0.906961 0.7283868 0.6845563 1.085729 0.5775938 0.7916918 0.7027509 1.242267 0.9580279 0.7631107 0.6695254 1.009243 1.337084 0.5839468 0.2814143 0.5798435 0.349776 0.3680091 0.9853479 1.049569 0.8882334 0.6960694 0.4837371 1.297935 0.6228109 0.3616598 1.67673 1.440904 1.017016 1.206671 0.5318099 0.899635 0.8967425 0.293507 1.976792 1.740032 0.7159508 1.077516 3.253995 0.3022721 0.7124139 1.101211 0.5068628 2.65862 0.5292591 0.4505348 0.5022381 1.725313 1.642275 2.726286 0.2453457 0.6586936 0.7664922 1.259739 1.683809 0.9030974 1.889612 0.4215328 1.247651 0.3212083 0.4190274; 0.4298708 0.4554662 0.7286596 1.301503 0.7924292 0.4133269 0.789394 1.987667 0.3782371 0.7985271 0.8410948 1.284277 0.9685613 0.6115325 1.187522 0.4533649 0.5492083 0.8221219 0.4283617 1.04563 0.846892 0.7891954 1.260751 0.6505084 0.9192736 0.5884049 1.437755 1.109331 0.8742311 0.6800449 1.170939 1.522816 0.2963278 0.6515958 0.652636 0.4154171 1.144454 0.9596332 1.036943 0.7901523 0.556611 1.495332 0.7043902 0.3926788 0.4952499 1.672024 1.17311 1.405301 0.3457497 1.053491 1.028212 0.3056975 0.947058 2.022066 0.8156847 3.929202 1.319461 0.3307056 0.8116997 0.5794001 2.120663 0.6055697 0.5049481 0.5770283 1.9776 1.865971 1.563873 0.2498206 0.7665683 1.47331 1.294713 1.96625 2.202944 0.4804787 1.452756 0.3454404 0.4588361 1.333745 0.8607413 1.281289 1.514885 1.054407 0.4858945 0.9592467 0.2717203 0.8200541 1.409307 0.4340429 0.5598159 1.228932 1.43719 0.5865649 1.784893 1.422368 1.777304 0.8074629 0.4939677 0.631976 1.280428 0.7884768; 1.047887 0.8975468 0.6520413 1.636345 1.258064 0.8737338 0.7732706 1.334569 0.7699519 0.3128436 0.7425002 0.7268948 0.4650111 1.302236 1.101458 1.186344 0.8857896 0.6309868 2.898293 0.787136 0.4251695 2.244135 0.5609747 1.332085 1.604852 0.6966855 0.3827441 1.160883 0.3186521 2.682026 1.073288 0.9166907 1.418209 4.733662 1.504867 0.9127123 1.457708 0.6537849 2.367461 0.6835377 0.5616822 0.6532251 1.023712 2.077561 3.783035 1.762294 0.2552654 0.9894402 1.688898 1.474301 2.256182 2.521355 0.5413562 1.662887 1.23748 0.5001216 1.521813 0.9689062 1.618333 1.693641 1.195372 1.62254 1.084486 0.2783429 1.088547 0.9226557 0.4839235 0.6294222 1.557627 1.396587 0.6545044 2.009648 0.8807901 1.620042 0.9195001 1.242068 0.5411654 1.454273 0.8859452 1.987324 0.3471812 0.8041712 2.131715 0.5622178 1.394999 0.4265159 1.155669 2.204539 0.7823294 2.712348 1.1769 0.7624616 0.6322917 1.766197 1.841663 1.138438 0.5849253 0.6422938 0.87487 1.394521; 5.579464  3.074723   2.20039  1.163646  2.088193  1.079023  2.018292 0.9599566  1.091186  1.533654  1.566148  1.662157  1.784378 0.8389745  2.565443 0.4586224   2.40852  2.093154 0.9377474  1.067143  1.305524 0.8070072  0.930425 0.7520566  1.905143  1.192467 0.8206825  1.213846  1.700009  1.926923 0.5830867  1.950197 0.9753732  1.532142  2.071853 0.2775415  1.743496  1.261119  0.844781  1.887378 0.9202037 0.8027825  2.212625  1.446403  2.019133  1.877956 0.4544384  1.379811    1.5479 0.8813421 0.3478412  1.674708 0.7804708  1.646892 0.6775672  2.163084 0.6289903 0.8782698  2.282645  1.300883  2.025086  1.267158  2.373495 0.6490469  2.767082 0.9978805  1.636098  3.278466 0.8328068  1.844748  1.502163  1.432012 0.6894892  1.425876   1.43165  1.455795 0.6685516  1.481304  1.778105 0.3789204  1.117673 0.7263875  1.391714  2.160052  1.433377  1.742186 0.9734867 0.4859414 0.4167967 0.9671515   1.07717 0.6382016  1.181805 0.7764073 0.9875141  2.381149  1.221023 0.5879182  1.213112  0.552035; 0.9274287  2.089907  1.877205 0.8861349  2.424599 0.3185429   2.18503  2.070162 0.4885245  1.539311  1.690679 0.9743333 0.3755372  1.850153 0.8633046  1.827799 0.7590079  3.410015 0.6872031 0.7667859  0.733409  2.538065  1.695107  2.262615 0.6948822  2.634668 0.7111679  1.443702  1.098169  1.328038   3.71068  1.222027  2.038615  2.333623  1.590247 0.7621437  1.632385  1.580245  1.611964 0.7318596  1.643971  1.982592 0.4055108  1.236829 0.7993353  2.741629  2.400096  1.585156  1.941829 0.8824257 0.5208487 0.9615169  1.066989  1.968598 0.7036318  2.112876    0.8508 0.9195119  2.668824  1.347987  1.846419  1.339442  1.707346 0.6220693  3.254288  1.174975  0.885196  3.377407   1.13301  1.301754  1.026166 0.9135878 0.7644072 0.5484033 0.8098611 0.3072269  1.088428  1.863648  1.024963  4.237982  1.334753  1.856798 0.3377385 0.4809729 0.7750529  1.985536  1.192837   1.41057  2.364495  2.282897  1.665865  3.855673  1.726389  3.875553  1.618238 0.7552292  2.429395 0.5537202  1.736285  2.374539'
));

#./bin/prog -s lotka_volterra -t 0:.005:4 -i 0:.005:4 -u .48,.026,.93 -o .05,.05,.05 -y 35,4 -k 100 -n $i -p 15 -b -d 2 > results/lv_results/lv$i.txt

v2 = np.array(np.mat('0.7118773  0.2230614  0.2431492  0.1072756  0.4566155  0.5500206  0.5739519  0.5135515  0.8047767  0.7323138  0.3981608   0.256905   0.473515  0.2505396  0.4775504   0.553978  0.6613587  0.4959745  0.2988283  0.7708964  0.4749307  0.1458151   0.748241  0.3706478   1.080923  0.2778767  0.5113422   0.503239  0.7345342  0.4049006  0.7176048  0.9413247    1.17856   0.776096   0.562898  0.9469979  0.4759262  0.3693376  0.7158494  0.6476348  0.1726162  0.8869544  0.3970757  0.2997402  0.0766692   1.534667 0.08960693  0.3047867  0.6961421   1.036994  0.8562103  0.4011382  0.7389155  0.1782994  0.1252088  0.2700266  0.8926983  0.5867463  0.9554774  0.1988062  0.9170976  0.8723163  0.9085429  0.5475092  0.1430182  0.6133106  0.4676833  0.1298537  0.4877302  0.4075084  0.6413314   0.142468  0.9804687  0.3558704  0.7719787   0.964183  0.5108002  0.1449716  0.9367903  0.2892266  0.8366154  0.5655775  0.2071009  0.7384339  0.4458276  0.4877645  0.2361076   1.012266  0.1549256  0.3382839  0.1108262  0.3665796  0.4270984  0.2110106  0.7594089  0.2179916  0.2547327  0.5798245  0.2048585  0.6262781;1.447704  0.3579249    1.10153  0.5173306  0.6816982   1.057515  0.4943471   1.101557  0.9862156  0.8436087  0.5884479   1.350984  0.2390623  0.2582574   2.704929 0.05671499  0.2942632  0.2263024  0.9571041   1.267283   2.236833  0.4542027  0.9547517  0.6707679    1.56187  0.2021701   1.339236  0.7279154   1.473981  0.1266285    1.39394  0.3726609   1.376326   1.561892  0.3050759  0.5448986  0.5034855  0.4549159   1.028135  0.3665741  0.9734209  0.8378485  0.7474104   1.519543  0.3480408   1.094669   1.488522  0.5789398  0.2252857   1.438491    0.21399    1.23323   1.240251   0.124343   1.025214  0.4369098  0.5278791   1.070827   1.588898  0.5318889  0.2572479  0.1852488  0.6567967  0.5874556   1.269311   1.110335  0.4218562  0.3832697   1.452753  0.7062382  0.8165372   1.070596   1.252994    1.67491   1.352211   1.009772  0.1825667   0.489402  0.9305306   1.937579  0.5558065   1.600931   1.800274   0.374817   1.433446  0.2029945    1.01559  0.7699301  0.6948542   1.463749  0.2684977  0.9874632  0.8321492   1.291776  0.2444434   1.403971   0.620836  0.9139753  0.1815203  0.6045934;0.3615059  1.887546  1.742891   1.85991 0.7300109  0.644624 0.9280638 0.5603135  0.868489 0.6479794 0.3386704  1.041313  1.128659  2.076027 0.4386347  1.426169  2.030911 0.6109051 0.6578493  1.957046 0.6631282  1.642127  1.647345 0.3407026  1.317735 0.4316013  0.576487  1.785574  2.190036 0.9873352 0.2533813 0.3311204  1.046026 0.6699241  2.078316   1.47775 0.4893318 0.6664551  1.974794 0.7440841  1.017383  1.390699  1.675454  2.323068  1.824918  1.294787  1.922011 0.5243795  1.195826  2.734691  3.496187 0.6310146  2.521501  0.683874  1.947057  1.418417 0.4347057 0.9315515   1.17975  2.003257  0.609554 0.5091889   1.43378 0.3055839 0.2377603  1.914356  0.585352  1.150361  1.665228 0.3420242  1.494544 0.6557928 0.9224577 0.1987867  1.262259 0.8261458 0.5405089  1.220491 0.8157173  1.074628 0.5626593 0.5266795  1.586556  1.133108 0.6782815  1.209363  0.144924 0.7880356  0.714085  1.441317 0.6494282 0.6311277 0.7909451  1.199112  1.505776  1.152648  0.566436 0.9231718  1.336385 0.4974168;0.8975288 0.5358719  1.214625 0.7595164   2.85788  1.853471  1.248561 0.9725384 0.9681885  1.099659  1.224314  1.571677  2.108321 0.9102326  2.314174   2.44594 0.6785641  1.468494  2.455068  3.579052 0.7169204  3.472465  0.775894 0.5443974  2.478308  0.694576  1.624048  1.696106   1.74256  2.566339 0.7802106  1.550943  2.015168  2.210848 0.3139086  0.912046  1.559936  2.093004 0.5554207  1.555387 0.9994872  2.366605 0.3557197  1.477484  1.802412 0.5884755  1.179361 0.9977025   1.12043 0.6175968 0.6219156  1.722956  1.365101  1.989828  1.481003 0.2371949 0.9154664 0.5129034   1.08049  0.946168    1.2167 0.7028851  2.443389  1.711006 0.2813505  1.391383 0.6038362  1.115637  1.641785  0.582466  2.560745  1.235005  1.182339  1.634121  1.530022  1.789174 0.9863046 0.5693663  1.648896  0.534057 0.4222173 0.3566858  3.051559 0.9878906 0.6983723 0.1733003 0.5950648  1.395559  1.563313  1.893283 0.4000137  2.121029 0.6035482  0.499942 0.6936798  1.249298  2.432651 0.6343139 0.9221766 0.8672648;3.15575   1.05449  1.840049 0.7786231  2.709015  2.995251  1.233585  1.633921 0.7760726  2.021914  1.337811   1.26249 0.5297314  2.330887  1.076019   1.36585  1.775723  1.298043  1.516126 0.7347317  2.225337  1.600585  2.410281   1.75921 0.3014197  1.047696 0.5527762  2.145402  1.250484 0.7787532  1.047935  2.208096  2.302769  1.633805 0.6417788  1.315139  1.953454 0.6861543  3.249209  1.555395  1.373322  1.945158  1.993093   2.13933  2.452179 0.6039644  1.961641 0.6031393 0.4580119  1.723822  3.838989  1.761976 0.7669154 0.2552248 0.8486055  1.829907  1.328769  2.280099 0.5920234  1.252588 0.8473354  1.239565 0.9644529  1.461839 0.9615882  0.843396  1.042942 0.9843267  1.469216 0.5253361  1.054306 0.4428369    3.7691 0.5921709 0.8405756   1.13655  2.128189  1.600691  2.886458  1.525379  1.077064  1.188085   1.03645  1.773754 0.7322614 0.7325171 0.5201462  1.148257  1.398512  2.512569  1.078509   0.86065 0.8505477 0.6978364 0.2791375 0.7634773  0.119583 0.3438133  2.096346 0.4265751;0.8575984  1.186138  2.691678  2.710815  1.880049 0.6802178  1.519653  2.271731 0.8012886  3.917682  2.017905  1.566452  1.157482  2.445095  2.986771  1.586296  2.280725 0.6828884 0.5069193 0.7076455  4.599205  1.269325 0.8375536 0.9333084  2.254881  1.651533   2.67739 0.7860133  3.046334   1.08983 0.9504095  1.231867  1.679908  3.520395  1.057152  1.918807  1.104397  1.131609   0.55009 0.4786122  2.828456  4.564043  1.725097 0.9654589  2.492108  1.367657  3.422556  1.638822  1.890097  1.493778  1.191796  2.056671  1.056606 0.7985651  0.573011  1.385499  1.612596  3.048554  1.212364 0.9482344  1.099525 0.8026053 0.2586662 0.9786966 0.2127818 0.4628012  2.554153 0.5256947  2.101025  1.876787  4.051368   1.23755  1.305486  1.453273  2.209372  3.293966  3.101244  0.806495  2.218415  5.441806   2.78402  1.137259  1.221329 0.4854069 0.6123785  1.964172  2.835674  3.878156  1.287985 0.6161066  4.203256  1.284908  1.112464 0.5783985 0.3017724  2.816945  1.614572  1.233662 0.5570849 0.5753877;1.172219  1.495689  1.197384  4.095118  1.288244   2.29196  2.177857 0.5782785  1.307025  3.275622  5.425213  1.950095  1.095621  2.864306  1.530902  3.980094  1.856906  2.247033  1.794077  1.667265  2.346657  1.168327 0.8667457 0.6329587  1.121356  1.831445  5.404538  1.347293   1.03739  1.346097 0.9137196  3.855235  1.192851 0.3136573 0.5873702   2.99826 0.6350489  2.399443  2.234506  4.752466  1.494282  1.459808   1.92466  2.522446 0.2489844  3.581037   2.53376 0.8700847  3.279191 0.5390416  1.420305 0.5926894  0.784275  2.334851  1.219314  4.529332  2.827816 0.7796365  5.017889  1.445218  1.285408 0.7366186 0.2854367  3.260853  1.817734  1.372811 0.6667098 0.6079915  2.979097  1.383884  2.001813  3.420365  2.643531  2.638247 0.8239278  2.120642  4.112227  1.543969  3.606431  1.920224  4.899063  1.219588  5.616915  2.374689   4.89721  6.797249  4.177818  1.391406    2.5158  2.207574  3.426952  1.409317 0.9397547  4.878723  1.116086  1.793189  1.458583  1.191946 0.6006774  1.484973;1.405108  1.256843 0.7137158   1.61516 0.7498227     2.706  2.586518  5.495588  1.750615  1.615426  2.161867  2.841452 0.3220459  4.072442  1.204133  1.017754  7.722258 0.5900754  1.386151  1.623032   4.77161 0.9546305  1.444081  3.793315  3.205326  1.578098  5.921401  3.490007  1.460627  2.045334 0.2728868  3.722094  0.534827  1.514928 0.8915161  0.643022  1.990081  1.598452  3.002772  2.244587  2.000083  3.041553  4.602743  2.454164  1.819042  1.792031  3.288515  2.151203    2.0341  1.423354  1.175409  2.752005 0.7080937  5.670859  4.624871  1.536538  2.088045  2.907798  1.872622  1.584564  7.433329  5.660786  1.212812  1.998554  1.098915 0.6540579  2.940589  2.914567  1.263068 0.4738986  1.298092 0.8914547   1.06583  1.461633 0.6972334  4.253012  3.450929  0.997159  7.209414  1.560818  4.282605  1.231748  3.602895  1.906228 0.9659249  3.922314  1.924887  5.959641  1.729805   3.50112  6.448856  1.953656  5.609052 0.8428352  1.169217  1.616746  1.896899  3.886896  3.090692  2.119091;1.814369  2.490192  2.212961  3.325497  1.013495  2.018183  2.037807  4.629904  2.320094  6.495472  1.361576  3.124412  6.502085  5.249603  1.682769  2.317177   2.80782  4.384198    8.7258  1.301486  4.506174  1.967587  1.181322 0.7115295  1.922365  1.380104 0.5772956  1.507234  1.013516  0.911746  1.445029 0.7936181   2.19784  3.877156    1.2712  8.457065  2.591889  1.885952   1.41356  5.673097  2.105753  4.507314  1.164631  2.201074  1.724816  1.900899  3.982574  7.479273  2.236888  6.439914 0.9631125  1.986958  1.266783  3.934134  2.164808  4.381881  3.491182 0.9385015  2.347096  1.355101  5.884211  1.767369  2.166714  2.089277  1.539158 0.5532299  1.501869 0.8968846  1.417479  2.954829  6.935303 0.6552169  10.04047  4.876966  2.442483  2.690952    4.6091 0.9982793   3.79642  1.709123   1.14079  1.588544  1.110437 0.8901923  1.168421  3.984436 0.9795002  4.100367  4.650014  1.666316 0.9047548  4.808564  4.475396  6.144304 0.5096306  1.116084  4.203508 0.9218709  10.77206 0.4001934;9.916251  1.946699   5.46496  2.108925  4.521646  6.416608  1.144197  4.979706  1.312796  7.919196  2.073394  4.386517  8.640228  3.377753  7.346085  4.693433  2.170033  1.365679  4.390567  2.429864  4.897502  3.889978  1.010409   2.57931  1.509659  6.680865  1.993344  2.432767  2.352942 0.4393013  0.580516  15.13695  1.571017    1.8024  7.624232 0.7405288  10.51539  5.453611  2.683963   2.97435  5.160612  1.064098  4.201232  3.706339  1.286305  1.734979  1.264345 0.9671272  1.284314  2.549236  1.090878  4.572949  5.185964  1.869694 0.9605441  5.406644  4.963028  7.021226  2.625212  1.209675  4.671408  1.047162  13.28069  0.418402  2.191671 0.8607383  1.268061  2.102686 0.6521615 0.3542657  3.641477   2.96947   3.01384  13.87071  1.067416   1.96413    1.0109  0.283869  4.467362  1.695277  3.029114  1.731741 0.8818946 0.9243838  4.882961  2.322981  5.322199  4.937537  5.674646  5.455014  0.881601  1.760144  4.130369  6.580417  1.900582 0.5139288  3.383163  4.432921  1.165909  6.650582'));

for i in range(v2.shape[0]):
    format_data(v2[i,:], i+1)
    