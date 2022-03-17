import subprocess
import argparse
parser=argparse.ArgumentParser(description="run")
parser.add_argument("--n", type=int)
args = parser.parse_args()
n = args.n
root = 'results_cifar'
coreset = 0.01

# if args.n == 0:
#     for cl in [0,1,2,3,4,5,6,7,8,9]:
#         for load in [32,64,128,256,512]:
#             for inp in [32,64,128,256,512]:
#                 log_name = str(cl) + str(coreset) + str(inp) + str(load)
#                 subprocess.call(f"python train_cifar.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --cifar_normal {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 3:
    for cl in [0]:
        for load in [32,64,128,256,512]:
            for inp in [32]:
                log_name = str(cl) + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train_cifar.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --cifar_normal {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 4:
    for cl in [0]:
        for load in [32,64,128,256,512]:
            for inp in [64]:
                log_name = str(cl) + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train_cifar.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --cifar_normal {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 5:
    for cl in [0]:
        for load in [32,64,128,256,512]:
            for inp in [128]:
                log_name = str(cl) + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train_cifar.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --cifar_normal {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 6:
    for cl in [0]:
        for load in [32,64,128,256,512]:
            for inp in [256]:
                log_name = str(cl) + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train_cifar.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --cifar_normal {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 7:
    for cl in [0]:
        for load in [32,64,128,256,512]:
            for inp in [512]:
                log_name = str(cl) + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train_cifar.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --cifar_normal {cl} --gpu {n} > logs/{log_name}.txt", shell=True)


